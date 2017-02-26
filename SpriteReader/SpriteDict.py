#!/usr/bin/python
# coding: utf-8

u""" 各ROMにおけるスプライトのアドレスを示すオフセットテーブル

このオフセットテーブルの直前にもテーブルが存在し，その一つ目のデータがオフセットテーブルの先頭アドレスになっている
続くデータは各タイプ（ナビ，攻撃エフェクト，置物，etc.）の先頭スプライトのアドレス？
"""

ROCKEXE6_GXX = {
"startAddr":0x032CA8,
"endAddr":0x033967,
"classHeadAddr":[0x032CE0, 0x032D60, 0x032DBC, 0x032F60, 0x0330D0, 0x033150, 0x0332D0, 0x033554, 0x0336D8],
"ignoreAddr":[0x4EA2E4, 0x4EA9DC, 0x506328]
}

MEGAMAN6_GXX = {
"startAddr":0x31CEC,
"endAddr":0x329A8,
"classHeadAddr":[],
"ignoreAddr":[]
}

ROCKEXE6_RXX = {
"startAddr":0x032CA8,
"endAddr":0x033964,
"classHeadAddr":[],
"ignoreAddr":[]
}

MEGAMAN6_FXX = {
"startAddr":0x31CEC,
"endAddr":0x329A4,
"classHeadAddr":[],
"ignoreAddr":[]
}

ROCKEXE5_TOB = {
"startAddr":0x0326E8,
"endAddr":0x033147,
"classHeadAddr":[],
"ignoreAddr":[]
}

ROCKEXE5_TOC = {
"startAddr":0x0326EC,
"endAddr":0x03314B,
"classHeadAddr":[],
"ignoreAddr":[]
}

ROCKEXE4_5RO = {
"startAddr":0x02B39C,
"endAddr":0x02BC73,
"classHeadAddr":[],
"ignoreAddr":[0x50B268]
}

ROCKEXE4_RS = {
"startAddr":0x02787C,
"endAddr":0x028218,
"classHeadAddr":[],
"ignoreAddr":[]
}

ROCKEXE4_BM = {
"startAddr":0x027880,
"endAddr":0x02821F,
"classHeadAddr":[],
"ignoreAddr":[]
}

ROCKMAN_EXE3 = {
"startAddr":0,
"endAddr":0,
"classHeadAddr":[],
"ignoreAddr":[]
}

ROCK_EXE3_BK = {
"startAddr":0x248E0,
"endAddr":0x251B4,
"classHeadAddr":[],
"ignoreAddr":[0x441060, 0x6A5F20]
}

ROCKMAN_EXE2 = {
"startAddr":0x1E9D4,
"endAddr":0x1F1A8,
"classHeadAddr":[],
"ignoreAddr":[]
}

ROCKMAN_EXE = {
"startAddr":0x12614,
"endAddr":0x12B74,
"classHeadAddr":[],
"ignoreAddr":[]
}

ROCK = {
"startAddr":0,
"endAddr":0,
"classHeadAddr":[],
"ignoreAddr":[]
}

GXX_Sprite_List = {
"0x1d8000":"ロックマン（戦闘）",
"0x1df420":"ヒートビースト（戦闘）",
"0x1e7cc8":"エレキビースト（戦闘）",
"0x1f1414":"スラッシュビースト（戦闘）",
"0x1fa9e8":"キラービースト（戦闘）",
"0x204108":"チャージビースト（戦闘）",
"0x20cd4c":"アクアビースト（戦闘）",
"0x214808":"トマホークビースト（戦闘）",
"0x21c354":"テングビースト（戦闘）",
"0x223c48":"グランドビースト（戦闘）",
"0x22cc50":"ダストビースト（戦闘）",
"0x233728":"グレイガビースト（戦闘）",
"0x23b768":"ファルザービースト（戦闘）",
"0x4ea2e4":"白玉",
"0x241ec4":"メットール（戦闘）",
"0x242e94":"アーバルボーイ（戦闘）",
"0x244164":"メガリア（戦闘）",
"0x2455b0":"スウォーディン（戦闘）",
"0x246a24":"キラーズアイ（戦闘）",
"0x2489c8":"クエイカー（戦闘）",
"0x2492fc":"キャタック（戦闘）",
"0x249c7c":"チャンプル（戦闘）",
"0x24ac94":"ウインドボックス（戦闘）",
"0x24b254":"ララパッパ（戦闘）",
"0x24d23c":"ダルスト（戦闘）",
"0x24dc7c":"ドルダーラ（戦闘）",
"0x24eaf4":"ヤカーン（戦闘）",
"0x252558":"センボン（戦闘）",
"0x2533f4":"ヒトデスタ（戦闘）",
"0x253f88":"ツボリュウ（戦闘）",
"0x257994":"カカジー（戦闘）",
"0x25859c":"パルフォロン（戦闘）",
"0x258ff8":"グラサン（戦闘）",
"0x25a0d8":"ボムコーン（戦闘）",
"0x25ad90":"モリキュー（戦闘）",
"0x25b860":"ハニホー（戦闘）",
"0x25bfc4":"ガンナー（戦闘）",
"0x25c9ac":"ゼロプレーン（戦闘）",
"0x25dfb4":"アサシンメカ（戦闘）",
"0x25f2c8":"スナーム（戦闘）",
"0x260f88":"アルマン（戦闘）",
"0x262cec":"レムゴン（戦闘）",
"0x263484":"ナイトメア（戦闘）",
"0x2647e4":"トーテム様（戦闘）",
"0x264fa0":"ヒートマン（戦闘）",
"0x26faf0":"エレキマン（戦闘）",
"0x278ebc":"スラッシュマン（戦闘）",
"0x28324c":"キラーマン（戦闘）",
"0x28f18c":"チャージマン（戦闘）",
"0x296f40":"アクアマン（戦闘）",
"0x29d818":"トマホークマン（戦闘）",
"0x2a5af0":"テングマン（戦闘）",
"0x2b0690":"グランドマン（戦闘）",
"0x2ba7bc":"ダストマン（戦闘）",
"0x2c7550":"ブルース（戦闘）",
"0x2ced74":"ブラストマン（戦闘）",
"0x2d2ac8":"ダイブマン（戦闘）",
"0x2d6fe4":"サーカスマン（戦闘）",
"0x2dabc8":"ジャッジマン（戦闘）",
"0x2dd9a8":"エレメントマン（戦闘）",
"0x2e0114":"カーネル（戦闘）",
"0x2e4050":"フォルテ（戦闘）",
"0x2e8470":"グレイガ（戦闘）",
"0x4ea9dc":"白玉",
"0x2ef3c0":"ハクシャク（戦闘）",
"0x2f279c":"ソード（戦闘）",
"0x2f6314":"キャノン（戦闘）",
"0x2f7ff0":"ボム（戦闘）",
"0x2f9820":"バスター（戦闘）",
"0x2fc620":"ヒートクロス（戦闘）",
"0x2ff368":"獣化（戦闘）",
"0x300ccc":"マズルフラッシュ（戦闘）",
"0x301058":"オーラ（戦闘）",
"0x3022b0":"センシャホウ（戦闘）",
"0x303650":"ビーストカーソル（戦闘）",
"0x3038c4":"ファルザービーストの羽（戦闘）",
"0x306388":"ヨーヨー（戦闘）",
"0x306e70":"ヨーヨー手元（戦闘）",
"0x307054":"トマホーククロス（戦闘）",
"0x30b054":"炎（戦闘）",
"0x30b980":"ジャンゴ（戦闘）",
"0x30db4c":"アクアショット（戦闘）",
"0x30ee28":"ダストクロス（戦闘）",
"0x311fb4":"バスターアップ（戦闘）",
"0x312f6c":"スチールパニッシュ？（戦闘）",
"0x313c64":"ソード系（戦闘）",
"0x315da8":"ドリームソード（戦闘）",
"0x317008":"トルネード手元（戦闘）",
"0x317ad4":"トルネード（戦闘）",
"0x3183e4":"エアショット（戦闘）",
"0x319e2c":"スプレッドガン（戦闘）",
"0x31b13c":"バブルショット（戦闘）",
"0x31be60":"ガード（戦闘）",
"0x31d440":"炎（戦闘）",
"0x31e110":"バルカン（戦闘）",
"0x31e67c":"アクアクロス（戦闘）",
"0x3213c4":"ヒートショット（戦闘）",
"0x321618":"バブルスター（戦闘）",
"0x32319c":"フェザーシュート（戦闘）",
"0x3233e0":"エアホッケー（戦闘）",
"0x323560":"カウントボム（戦闘）",
"0x3245a4":"ブラックボム（戦闘）",
"0x324810":"カンケツセン（戦闘）",
"0x32606c":"フウジンラケット手元（戦闘）",
"0x327440":"フウジンラケット（戦闘）",
"0x327ff4":"ヘルズバーナー？（戦闘）",
"0x328248":"トレインアロー（戦闘）",
"0x328d14":"コーンショット（戦闘）",
"0x329108":"カモンスネーク（戦闘）",
"0x3294d0":"影？（戦闘）",
"0x329934":"風（戦闘）",
"0x329b58":"カワリミ（戦闘）",
"0x32a0e0":"ポイズン（戦闘）",
"0x32a7b4":"リュウセイグン（戦闘）",
"0x32aa14":"パネルシュート（戦闘）",
"0x32ade0":"ワラニンギョウ（戦闘）",
"0x32b244":"オジゾウサン（戦闘）",
"0x32c4e0":"フレイムソード（戦闘）",
"0x32e848":"アクアソード（戦闘）",
"0x330f38":"エレキソード（戦闘）",
"0x3334e8":"ガンデルソル（戦闘）",
"0x333be8":"ガンデルソル放射（戦闘）",
"0x3343e8":"バリア？（戦闘）",
"0x335550":"マシンガン（戦闘）",
"0x335ac8":"エアホイール（戦闘）",
"0x336310":"ゴスペルキャノン（戦闘）",
"0x336dd8":"バンブーランス（戦闘）",
"0x336fa4":"フレイムフック（戦闘）",
"0x337e70":"ガンデルソルEX放射（戦闘）",
"0x3387e8":"ラッシュ（戦闘）",
"0x33962c":"オテンコ（戦闘）",
"0x339cbc":"ビート（戦闘）",
"0x33a5a4":"タンゴ（戦闘）",
"0x33b4d0":"光球？（戦闘）",
"0x33bf04":"バットキャノン（戦闘）",
"0x33d320":"ロール（戦闘）",
"0x33e0c8":"エレキクロス（戦闘）",
"0x341018":"スラッシュクロス（戦闘）",
"0x344550":"テングクロス（戦闘）",
"0x347c74":"キラークロス（戦闘）",
"0x34ae00":"チャージクロス（戦闘）",
"0x34e030":"ドリルアタッカー（戦闘）",
"0x34e97c":"ワイドショット（戦闘）",
"0x34f2b8":"テングラケット（戦闘）",
"0x34f730":"ローリングログ（戦闘）",
"0x350044":"リスキーハニー（戦闘）",
"0x350480":"エレキパルス（戦闘）",
"0x350854":"ドールサンダー（戦闘）",
"0x350da0":"マグネコイル（戦闘）",
"0x351068":"メテオナックル（戦闘）",
"0x3518a0":"グランドクロス（戦闘）",
"0x354df0":"サンアンドムーン（戦闘）",
"0x3557d8":"ファルザー（戦闘）",
"0x357204":"ファルザーの羽ショット（戦闘）",
"0x357464":"グレイガ（戦闘）",
"0x3592a4":"ストーン（戦闘）",
"0x35a9c4":"ストーンの破片（戦闘）",
"0x35ad7c":"ドルダーラの炎（戦闘）",
"0x35c0d8":"ショックウェーブ（戦闘）",
"0x35d1c0":"岩？（戦闘）",
"0x35d728":"エアホッケー（戦闘）",
"0x35d90c":"ブーメラン（戦闘）",
"0x35e76c":"岩（戦闘）",
"0x35eb58":"グレイガの頭（戦闘）",
"0x35f110":"センシャホウの爆風（戦闘）",
"0x35fd24":"キャノンの爆風（戦闘）",
"0x36052c":"ミステリーデータ（戦闘）",
"0x362060":"ヘルズローリング（戦闘）",
"0x3637b8":"デルタレイエッジ（戦闘）",
"0x364354":"キラキラ？（戦闘）",
"0x364ecc":"ブラッドレイン（戦闘）",
"0x3651b0":"発光？（戦闘）",
"0x365448":"ドールサンダーの電撃（戦闘）",
"0x366c80":"エレキマンのオプション（戦闘）",
"0x367e40":"サンダーボール（戦闘）",
"0x3691ec":"アクアニードル（戦闘）",
"0x369c18":"ヒートマンの炎（戦闘）",
"0x3705d8":"ヒートウェーブ（戦闘）",
"0x371ce4":"ヒートバーナー（戦闘）",
"0x374438":"コーンショット（戦闘）",
"0x3745a8":"カーネルアーミー（戦闘）",
"0x3753f8":"アクアホース（戦闘）",
"0x376dc4":"アクアホースの水（戦闘）",
"0x377820":"アクアマンの水（戦闘）",
"0x377b48":"アクアシャワー（戦闘）",
"0x379afc":"アクアショット（戦闘）",
"0x37a004":"マグマ（戦闘）",
"0x37a9e0":"泡（戦闘）",
"0x37b1a0":"シューティングバスター（戦闘）",
"0x37bcc4":"サーチカーソル（戦闘）",
"0x37c03c":"マズルフラッシュ（戦闘）",
"0x37c88c":"イーグルの止まり木（戦闘）",
"0x37cb00":"イーグル（戦闘）",
"0x37f0f4":"トマホーク（戦闘）",
"0x37f7b4":"衝撃波？（戦闘）",
"0x3805c4":"℃（戦闘）",
"0x380884":"スパイラル？（戦闘）",
"0x382ad4":"スクリーンディバイド（戦闘）",
"0x386670":"レムゴンの腕（戦闘）",
"0x3878dc":"リスキーハニー（戦闘）",
"0x388070":"電撃？（戦闘）",
"0x388b28":"ローリングログ（戦闘）",
"0x389364":"ワイドショット（戦闘）",
"0x38a0d0":"グレイガクロー（戦闘）",
"0x38b080":"スラッシュマンのクナイ（戦闘）",
"0x38b6b8":"ワイドスラッシュ？（戦闘）",
"0x38c428":"",
"0x38e0e4":"",
"0x38e3d8":"",
"0x38f284":"スラッシュエックス（戦闘）",
"0x38ffd4":"",
"0x390bdc":"",
"0x39122c":"テングストーム（戦闘）",
"0x393738":"",
"0x393ef0":"",
"0x3941c8":"",
"0x3946c0":"",
"0x395158":"キラーカーソル？（戦闘）",
"0x3955f4":"キラーマンの使い魔（戦闘）",
"0x396f24":"キラーズデスビーム（戦闘）",
"0x3974dc":"キラーテイルアロー（戦闘）",
"0x397990":"グランドマンのキャタピラ（戦闘）",
"0x399634":"グランドマンのブースター（戦闘）",
"0x399cd4":"",
"0x399d54":"キラーズビーム（戦闘）",
"0x39abd0":"フラッシュボム（戦闘）",
"0x39b20c":"",
"0x39be70":"",
"0x39ddc4":"",
"0x39e3f0":"",
"0x39f3e0":"",
"0x39ff50":"",
"0x3a0dd8":"",
"0x3a2308":"爆発（戦闘）",
"0x3a3848":"爆発（戦闘）",
"0x3a4750":"不発（戦闘）",
"0x3a5a6c":"プラグイン（マップ）",
"0x3a8d9c":"",
"0x3a9b38":"",
"0x3aebc0":"",
"0x3af53c":"トラップ（戦闘）",
"0x3b1f20":"チャージ（戦闘）",
"0x3b4f38":"ブラインド（戦闘）",
"0x3b51c0":"爆発（戦闘）",
"0x3b5cd8":"混乱（戦闘）",
"0x3b6600":"",
"0x3b7044":"移動（戦闘）",
"0x3b83e8":"",
"0x3b8e88":"",
"0x3b9820":"",
"0x3bb224":"エナジーボム爆発（戦闘）",
"0x3bc984":"",
"0x3bd19c":"",
"0x3bd874":"",
"0x3becd4":"シンクロリング（戦闘）",
"0x3c2044":"",
"0x3c25b4":"",
"0x3c3c40":"",
"0x3c4740":"",
"0x3c56b0":"",
"0x3c5f70":"",
"0x3c6528":"",
"0x3c79b0":"バグライズ（戦闘）",
"0x3c900c":"熱斗（マップ）",
"0x3d6874":"メイル（マップ）",
"0x3d9228":"デカオ（マップ）",
"0x3dc76c":"やいと（マップ）",
"0x3df34c":"炎山（マップ）",
"0x3e24c0":"パパ（マップ）",
"0x3e63a8":"ママ（マップ）",
"0x3e9408":"デブ（マップ）",
"0x3eb1ec":"小さい男の子（マップ）",
"0x3ebe48":"男の子（マップ）",
"0x3ee8f8":"女の子（マップ）",
"0x3f124c":"男（マップ）",
"0x3f4c80":"女（マップ）",
"0x3f8214":"おじさん（マップ）",
"0x3fcac4":"研究者男（マップ）",
"0x3ffb24":"アイリス（マップ）",
"0x403430":"マッハ（マップ）",
"0x40727c":"まり子先生（マップ）",
"0x407f68":"コジロー（マップ）",
"0x40c2a0":"研究者女（マップ）",
"0x40f344":"小さい女の子（マップ）",
"0x40fcec":"おばさん（マップ）",
"0x411660":"おじいさん（マップ）",
"0x4120b4":"おばあさん（マップ）",
"0x4137bc":"メイド（マップ）",
"0x413f00":"名人（マップ）",
"0x4146a4":"ワイリー（マップ）",
"0x4187f4":"ヒノケン（マップ）",
"0x419a70":"エレキ婦人（マップ）",
"0x419f14":"パクチー（マップ）",
"0x41ab64":"鉄国男（マップ）",
"0x41b02c":"キリサキ（マップ）",
"0x41b444":"クロヒゲ（マップ）",
"0x41f044":"チロル（マップ）",
"0x4229f4":"フード（マップ）",
"0x425f78":"六方（マップ）",
"0x429760":"入道（マップ）",
"0x42e22c":"バレル（マップ）",
"0x433be4":"ケイン（マップ）",
"0x437074":"明日太（マップ）",
"0x439ae8":"ジャンゴ（マップ）",
"0x43a388":"オテンコ（マップ）",
"0x43c40c":"ハクシャク（マップ）",
"0x43cec4":"ロックマン（マップ）",
"0x446f3c":"ロール（マップ）",
"0x447818":"ガッツマン（マップ）",
"0x44832c":"グライド（マップ）",
"0x448bc4":"ブルース（マップ）",
"0x44eaf4":"プログラムくん（マップ）",
"0x452790":"緑ナビ（マップ）",
"0x458910":"悪ナビ（マップ）",
"0x460720":"女の子ナビ（マップ）",
"0x46344c":"ヒートマン（マップ）",
"0x46b90c":"エレキマン（マップ）",
"0x4710b0":"スラッシュマン（マップ）",
"0x47d090":"チャージマン（マップ）",
"0x484e80":"キラーマン（マップ）",
"0x48e020":"ブラストマン（マップ）",
"0x48fe24":"ダイブマン（マップ）",
"0x492a4c":"カーネル（マップ）",
"0x49c7c4":"サーカスマン（マップ）",
"0x4a1f0c":"ジャッジマン（マップ）",
"0x4a2660":"エレメントマン（マップ）",
"0x4a47d0":"グレイガビースト（マップ）",
"0x4a6200":"フードブルース（マップ）",
"0x4a6fe0":"フォルテ（マップ）",
"0x4a7934":"",
"0x4a7f38":"",
"0x4a9674":"",
"0x4aaa5c":"",
"0x4ac0d0":"",
"0x4ac8c8":"",
"0x4ace30":"",
"0x4ad2dc":"",
"0x4ad968":"",
"0x4ae024":"",
"0x4ae340":"",
"0x4ae76c":"",
"0x4ae9dc":"",
"0x4af558":"",
"0x4afc18":"",
"0x4b0054":"",
"0x4b0318":"",
"0x4b05f0":"",
"0x4b0d00":"",
"0x4b141c":"",
"0x4b153c":"",
"0x4b18d4":"",
"0x4b1eac":"",
"0x4b293c":"",
"0x4b3224":"",
"0x4b36b0":"",
"0x4b39b4":"",
"0x4b3cb4":"",
"0x4b3f24":"",
"0x4b44b4":"",
"0x4b4a34":"",
"0x4b4fd0":"",
"0x4b536c":"",
"0x4b5814":"",
"0x4b59f8":"",
"0x4b5f64":"",
"0x4b6054":"",
"0x4b68d4":"",
"0x4b6eec":"",
"0x4b752c":"",
"0x4b771c":"",
"0x4b77c4":"",
"0x4b7b7c":"",
"0x4b7f2c":"",
"0x4ba618":"",
"0x4babec":"",
"0x4bbfbc":"",
"0x4be44c":"",
"0x4c0b98":"",
"0x4c10e4":"",
"0x4c1ae4":"",
"0x4c1fe0":"",
"0x4c24c4":"",
"0x4c2b58":"",
"0x4c2ff0":"",
"0x4c3cc0":"",
"0x4c5460":"",
"0x4c6cc0":"",
"0x4c7054":"",
"0x4c76a4":"",
"0x4c7928":"",
"0x4c7fb0":"",
"0x4c8320":"",
"0x4c8974":"",
"0x4c8d7c":"",
"0x4c9100":"",
"0x4c9ca8":"",
"0x4ca0e8":"",
"0x4ca680":"",
"0x4cb1d0":"",
"0x4cb588":"",
"0x4cb7f8":"",
"0x4cbd7c":"",
"0x4cc7d4":"",
"0x4cc91c":"",
"0x4cf3b8":"",
"0x4d0314":"",
"0x4d05d8":"",
"0x4d0a30":"",
"0x4d1818":"",
"0x4d22d8":"",
"0x4d25a0":"",
"0x4d36a8":"",
"0x4d3c38":"",
"0x4d3ee8":"",
"0x4d4270":"",
"0x4d4768":"",
"0x4d4aec":"",
"0x4d4da0":"",
"0x4d5030":"",
"0x4d5328":"",
"0x4d5614":"",
"0x4d5be0":"",
"0x4d5dac":"",
"0x4d62cc":"",
"0x4d6870":"",
"0x4d7800":"",
"0x4d9264":"",
"0x4d9734":"",
"0x4db8f4":"",
"0x4dba40":"",
"0x4dbdf0":"",
"0x4dbf54":"",
"0x4dc188":"",
"0x4dd0cc":"",
"0x4dd4f0":"",
"0x4dd744":"",
"0x4dd898":"",
"0x4de5a0":"",
"0x4de7ac":"",
"0x4dead4":"",
"0x4df248":"",
"0x4df3a4":"",
"0x4df924":"",
"0x4dfc6c":"",
"0x4e0008":"",
"0x4e0258":"",
"0x4e0540":"",
"0x4e07a0":"",
"0x4e096c":"",
"0x4e1678":"",
"0x4e24d8":"",
"0x4e2ae8":"グレイブヤード入り口（マップ）",
"0x4e301c":"",
"0x4e3ccc":"",
"0x4e43dc":"",
"0x4e4714":"",
"0x4e4894":"",
"0x4e4fc0":"",
"0x4e53f8":"",
"0x4e5978":"",
"0x4e62a0":"",
"0x4e68d4":"",
"0x4e6ad4":"",
"0x4e7480":"",
"0x4e7688":"",
"0x4e7864":"",
"0x4e7bf8":"",
"0x4e7e68":"",
"0x4e7ff8":"",
"0x4e84b8":"",
"0x4e8d68":"じくうのひずみ",
"0x4e9404":"",
"0x4e96fc":"",
"0x4e9e30":"",
"0x4eabf8":"熱斗（会話）",
"0x4eb380":"メイル（会話）",
"0x4eba60":"デカオ（会話）",
"0x4ec270":"やいと（会話）",
"0x4ec8d0":"炎山（会話）",
"0x4ecf90":"パパ（会話）",
"0x4ed5b0":"ママ（会話）",
"0x506328":"",
"0x4edc10":"デブ（会話）",
"0x4ee25c":"小さい男の子（会話）",
"0x4ee83c":"毛の男の子（会話）",
"0x4eed58":"男の子（会話）",
"0x4ef358":"女の子（会話）",
"0x4ef9dc":"男（会話）",
"0x4effd4":"女（会話）",
"0x4f0594":"おじさん（会話）",
"0x4f0c34":"科学者男（会話）",
"0x4f1270":"アイリス（会話）",
"0x4f1890":"マッハ（会話）",
"0x4f1eb0":"まり子先生（会話）",
"0x4f2590":"コジロー（会話）",
"0x4f2bf0":"研究者男（会話）",
"0x4f31f0":"研究者女（会話）",
"0x4f37a8":"小さい女の子（会話）",
"0x4f3dac":"おばさん（会話）",
"0x4f43ac":"おじいさん（会話）",
"0x4f4a6c":"おばあさん（会話）",
"0x4f50b8":"メイド（会話）",
"0x4f57d8":"名人（会話）",
"0x4f5d74":"ワイリー（会話）",
"0x4f63d4":"ヒノケン（会話）",
"0x4f6b74":"エレキ婦人（会話）",
"0x4f7334":"パクチー（会話）",
"0x4f799c":"国鉄男（会話）",
"0x4f80bc":"キリサキ（会話）",
"0x4f869c":"クロヒゲ（会話）",
"0x4f8e7c":"チロル（会話）",
"0x4f953c":"フード（会話）",
"0x4f9a18":"六方（会話）",
"0x4f9f34":"入道（会話）",
"0x4fa5ac":"バレル（会話）",
"0x4fab64":"ケイン（会話）",
"0x4fb270":"明日太（会話）",
"0x4fb9dc":"ジャンゴ（会話）",
"0x4fc15c":"オテンコ（会話）",
"0x4fc734":"ハクシャク（会話）",
"0x4fcea4":"ロックマン（会話）",
"0x4fd5a4":"ロール（会話）",
"0x4fdc70":"ガッツマン（会話）",
"0x4fe468":"グライド（会話）",
"0x4fe994":"ブルース（会話）",
"0x4fee70":"プログラムくん（会話）",
"0x4ff68c":"緑ナビ（会話）",
"0x4ffbd0":"青ナビ（会話）",
"0x50013c":"茶ナビ（会話）",
"0x5006a8":"悪ナビ（会話）",
"0x500b0c":"ピンクナビ（会話）",
"0x501048":"ヒートマン（会話）",
"0x5017c0":"エレキマン（会話）",
"0x501d78":"スラッシュマン（会話）",
"0x5028f0":"チャージマン（会話）",
"0x502d34":"キラーマン（会話）",
"0x5033e4":"ブラストマン（会話）",
"0x503950":"ダイブマン（会話）",
"0x503ef4":"カーネル（会話）",
"0x5045b0":"サーカスマン（会話）",
"0x504cd4":"ジャッジマン（会話）",
"0x505118":"エレメントマン（会話）",
"0x5055e8":"グレイガビースト（会話）",
"0x505a2c":"フードナビ（会話）",
"0x505ee4":"フォルテ（会話）",
"0x6ebc28":"",
"0x6ec1e8":"",
"0x6ed4bc":"",
"0x6e6bc4":"",
"0x6e705c":"",
"0x6e7464":"",
"0x6e77f0":"",
"0x6e7a0c":"バトルチップ（UI）",
"0x6edf54":"",
"0x6ee66c":"",
"0x6eebe4":"",
"0x6eed78":"",
"0x7ec1d0":"",
"0x6e2710":"",
"0x6efd54":"",
"0x7f530c":"",
"0x7f54dc":"",
"0x6f3d5c":"",
"0x6f3fbc":"",
"0x6f4604":"",
"0x6f46b0":"",
"0x6f4888":"",
"0x6f4b58":"",
"0x7ebaa4":"",
"0x6f9bb8":"",
"0x6f9da0":"",
"0x6fd698":"",
"0x6fdcd0":"",
"0x6fa65c":"",
"0x6fa72c":"",
"0x6fcea4":"",
"0x6fd024":"",
"0x6f85fc":"",
"0x7e0df8":"ソウルウェポン（UI）",
"0x7e3a40":"",
"0x7e172c":"",
"0x7e469c":"",
"0x7e4ac8":"",
"0x7e5eec":"",
"0x7e68b4":"",
"0x7ec888":"",
"0x6f9624":"改造（UI）",
"0x6fbb08":"対戦（UI）",
"0x6fc4a0":"",
"0x6fc358":"",
"0x6e0d28":"",
"0x7e6efc":"",
"0x7e71e0":"",
"0x7e7578":""
}