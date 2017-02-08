#!/usr/bin/python
# coding: utf-8

u""" Map Modder ver 0.1 by ideal.exe

    Python3用
"""

from PIL import Image
from PIL.ImageQt import ImageQt
from PyQt4 import QtCore, QtGui
#import PyQt5
import binascii
import numpy as np
import os
import struct
import sys

import UI_MapModder as designer

from logging import getLogger,StreamHandler,INFO,DEBUG
logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(INFO)
logger.setLevel(INFO)
logger.addHandler(handler)

import argparse
parser = argparse.ArgumentParser(description=u"入力ファイルに対して指定の処理を行います")
parser.add_argument("file", help=u"処理対象のファイル")
args = parser.parse_args()


u""" Map Modder
"""
class MapModder(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = designer.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.graphicsView.scale(2,2)
        self.graphicsScene = QtGui.QGraphicsScene()
        self.graphicsScene.setSceneRect(-120,-80,240,160)    # gbaの画面を模したシーン（ ビューの中心が(0,0)になる ）
        self.ui.graphicsView.setScene(self.graphicsScene)


    def openFile(self, *args):
        u""" ファイルを開くときの処理
        """
        if len(args) != 0:
            u""" 引数がある場合はそれをファイル名にする
            """
            filename = args[0]
        else:
            u""" 引数がない場合はファイルを開く
            """
            filename = QtGui.QFileDialog.getOpenFileName( self, _("Open File"), os.path.expanduser('./') )   # ファイル名がQString型で返される
            filename = unicode(filename)

        try:
            with open( filename, 'rb' ) as romFile:
                self.romData = romFile.read()
        except:
            logger.info( _(u"ファイルの選択をキャンセルしました") )
            return -1    # 中断

        [title, code] = self.getRomHeader(self.romData)
        listName = code + "_" + title + ".txt"
        if os.path.exists("./lists/" + listName):
            print(u"リストファイルを読み込みました")
        else:
            print(u"リストファイルを作成しました")

        self.palData = self.parsePaletteData(self.romData, 0x745a4c)
        image = self.makeMapImage(self.romData, 0x715bcc, 7, 6)
        self.drawMap(image)



    def getRomHeader(self, romData):
        title = romData[0xA0:0xAC].decode("utf-8")
        code = romData[0xAC:0xB0].decode("utf-8")
        print("Title:\t" + title)
        print("Code:\t" + code)
        return [title, code]


    def drawMap(self, image):
        u''' マップ画像を描画する
        '''

        item = QtGui.QGraphicsPixmapItem(image)
        item.setOffset(image.width()/2*-1, image.height()/2*-1)
        imageBounds = item.boundingRect()
        self.graphicsScene.addItem(item)
        #self.graphicsScene.addRect(imageBounds)


    def parsePaletteData(self, romData, palAddr):
        u""" パレットデータの読み取り

            入力：ROMデータ，パレットのアドレス
            処理：ROMデータからのパレット読み込み，GUIのパレットリスト更新，RGBAカラー化
        """
        PALETTE_SIZE = 0x20
        COLOR_SIZE = 2

        readAddr = palAddr
        endAddr = readAddr + PALETTE_SIZE

        palData = []    # パレットデータを格納するリスト
        self.ui.palList.clear()
        palCount = 0
        while readAddr < endAddr:
            color = romData[readAddr:readAddr+COLOR_SIZE]
            color = struct.unpack("<H", color)[0]

            binColor = bin(color)[2:].zfill(15) # GBAのオブジェクトは15bitカラー（0BBBBBGGGGGRRRRR）
            b = int( binColor[0:5], 2 ) * 8  #   文字列化されているので数値に直す（255階調での近似色にするため8倍する）
            g = int( binColor[5:10], 2 ) * 8
            r = int( binColor[10:15], 2 ) * 8

            if palCount == 0:
                palData.append( {"color":[r, g, b, 0], "addr":readAddr } ) # 最初の色は透過色
            else:
                palData.append( {"color":[r, g, b, 255], "addr":readAddr } )

            colorStr = hex(color)[2:].zfill(4).upper() + "\t(" + str(r).rjust(3) + ", " + str(g).rjust(3) + ", " + str(b).rjust(3) + ")"  # GUIに表示する文字列
            colorItem = QtGui.QListWidgetItem(colorStr)
            colorItem.setBackgroundColor( QtGui.QColor(r, g, b) )  # 背景色をパレットの色に
            colorItem.setTextColor( QtGui.QColor(255-r, 255-g, 255-b) )    # 文字は反転色
            self.ui.palList.addItem(colorItem) # フレームリストへ追加

            palCount += 1
            readAddr += COLOR_SIZE

        return palData


    def makeMapImage(self, romData, startAddr, width, height):
        u''' マップ画像を生成する

            グラフィックデータは4bitで1pxを表現する．アクセス可能な最小単位は8*8pxのタイルでサイズは32byteとなる
        '''

        TILE_WIDTH = 8
        TILE_HEIGHT = 8
        TILE_DATA_SIZE = TILE_WIDTH * TILE_HEIGHT / 2

        logger.debug("Image Width:\t" + str(width) + " Tile")
        logger.debug("Image Height:\t" + str(height) + " Tile")

        imgDataSize = TILE_DATA_SIZE * width * height
        imgData = romData[startAddr:startAddr+imgDataSize]  # 使う部分を切り出し
        imgData = binascii.hexlify(imgData).upper()   # バイナリ値をそのまま文字列にしたデータに変換（0xFF -> "FF"）
        imgData = list(imgData) # 1文字ずつのリストに変換
        # ドットの描画順（0x01 0x23 0x45 0x67 -> 10325476）に合わせて入れ替え
        for i in range(0, len(imgData))[0::2]:  # 偶数だけ取り出す（0から+2ずつ）
            imgData[i], imgData[i+1] = imgData[i+1], imgData[i] # これで値を入れ替えられる

        imgArray = []
        imgDotNum = len(imgData)
        # 色情報に変換する
        readAddr = 0
        while readAddr < imgDotNum:
            currentPixel = int(imgData[readAddr], 16)    # 1ドット分読み込み，文字列から数値に変換
            imgArray.append(self.palData[currentPixel]["color"])    # 対応する色に変換
            readAddr += 1

        imgArray = np.array(imgArray)   # ndarrayに変換
        imgArray = imgArray.reshape( (-1, TILE_WIDTH, 4) )  # 横8ドットのタイルに並べ替える（-1を設定すると自動で縦の値を算出してくれる）
        u""" 現在の状態

            □
            □
            ︙
            □
            □
        """

        tileNum = width * height  # 合計タイル数

        # タイルの切り出し
        tile = []  # pythonのリストとして先に宣言する（ndarrayとごっちゃになりやすい）
        for i in range(0, tileNum):
            tile.append(imgArray[TILE_HEIGHT*i:TILE_HEIGHT*(i+1), 0:TILE_WIDTH, :])    # 8x8のタイルを切り出していく

        # タイルの並び替え
        h = []  # 水平方向に結合したタイルを格納するリスト
        for i in range(0, height):
            h.append( np.zeros_like(tile[0]) )    # タイルを詰めるダミー
            for j in range(0, width):
                h[i] = np.hstack( (h[i], tile[i*width + j]) )
            if i != 0:
                h[0] = np.vstack((h[0], h[i]))
        img = h[0][:, 8:, :]    # ダミー部分を切り取る（ださい）

        dataImg = Image.fromarray( np.uint8(img) )  # 色情報の行列から画像を生成（PILのImage形式）
        qImg = ImageQt(dataImg) # QImage形式に変換
        pixmap = QtGui.QPixmap.fromImage(qImg)  # QPixmap形式に変換
        return pixmap


u""" Main
"""
def main():
    app = QtGui.QApplication(sys.argv)

    mapModder = MapModder();
    mapModder.show()

    if len(sys.argv) >= 2:
        mapModder.openFile(sys.argv[1])

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
