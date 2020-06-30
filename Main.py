import random           #乱数用
import os               #コンソール操作用
import Status as Stas   #自作モジュールのインポート

#定数群
NPC_CHARS = [
    {"Id":1, "Name":"織田信長", "Hp":10000, "Atk":800, "Def":400, "Spe":200, "Force":1200, "Skill":2000, "Point":300, "Cost":50, "All":14700 },
    {"Id":2, "Name":"豊臣秀吉", "Hp":10000, "Atk":500, "Def":750, "Spe":375, "Force":1250, "Skill":1750, "Point":300, "Cost":57, "All":14550 },
    {"Id":3, "Name":"徳川家康", "Hp":10000, "Atk":700, "Def":350, "Spe":175, "Force":1050, "Skill":1750, "Point":300, "Cost":57, "All":14150 },
    {"Id":4, "Name":"今川義元", "Hp":10000, "Atk":400, "Def":600, "Spe":300, "Force":1000, "Skill":1400, "Point":300, "Cost":71, "All":13700 },
    {"Id":5, "Name":"武田信玄", "Hp":10000, "Atk":600, "Def":300, "Spe":150, "Force":900,  "Skill":1500, "Point":300, "Cost":66, "All":136000},
    {"Id":6, "Name":"明智光秀", "Hp":10000, "Atk":900, "Def":450, "Spe":225, "Force":1350, "Skill":2250, "Point":300, "Cost":44, "All":15250 },
]

#グローバル変数群
gPlayer = Stas.clsStatus()  #プレイヤーの選択したキャラ
gEndChar = []               #戦ったキャラのIDを保管する

#表示されている画面を奇麗にする
def dispClear():
    os.system("cls")

#NPC_CHARSの要素を一括で変数に代入
def setCharToItem(pChar, pItem):
    pChar.setDatas(pItem.get("Name"), pItem.get("Hp"), pItem.get("Atk"), pItem.get("Def"), \
        pItem.get("Spe"), pItem.get("Force"), pItem.get("Skill"), pItem.get("Point"), pItem.get("Cost"), pItem.get("All"))


#キャラクター選択用の表示
def dispChars():
    print("********************")
    print("メニュー")
    print("--------------------")
    print("武将選択（数字）")
    print("--------------------")
    for aItem in NPC_CHARS:
        print(str(aItem.get("Id")) + "." + str(aItem.get("Name")))

    print("********************")

#対戦形式で表示
def dispCharVsChar(pPlayer, pNpc):
    print("********************")
    print(pPlayer.get_name() + "VS" + pNpc.get_name())
    print("--------------------")
    print(pNpc.get_name())
    print("体力")
    print(pNpc.get_hp())
    print("兵力")
    print(pNpc.get_force())
    print("TP")
    print(pNpc.get_point())
    print("--------------------")
    print(pPlayer.get_name())
    print("体力")
    print(pPlayer.get_hp())
    print("兵力")
    print(pPlayer.get_force())
    print("TP")
    print(pPlayer.get_point())
    print("********************")
    print("1.攻撃 2.特技")
    return

#キャラクター選択
def selectChar():
    dispChars()

    #既定の値が入力されるまで無限ループ
    while True:
        aInp = input("->")
        #入力された値が数値か
        if aInp.isnumeric() == True:
            #入力された数値がキャラクターリストに存在するか
            for aItem in NPC_CHARS:
                if aItem.get("Id") == int(aInp):
                    #プレイヤーに選択されたキャラの情報を入れる
                    setCharToItem(gPlayer, aItem)
                    gEndChar.append(aItem.get("Id"))
                    return

#次の対戦相手を取得する
def initNpc(pNpc):
    aRndFlag = False
    while aRndFlag != True:
        aRnd = random.randint(1,len(NPC_CHARS))
        aFlag = False
        for aItem in gEndChar:
            if aRnd == aItem:
                aFlag = True
                break

        if aFlag != True:
            for aItem in NPC_CHARS:
                if aRnd == aItem.get("Id"):
                    setCharToItem(pNpc, aItem)
                    return

#バトル画面
def battleStart():
    #NPC生成
    aNpc = Stas.clsStatus()

    #NPCにランダムな値を入れる
    initNpc(aNpc)

    aEndFlag = False
    while gPlayer.get_hp() >= 0 and aEndFlag == False:
        dispCharVsChar(gPlayer, aNpc)
        input("->")
        #
        #
        #
        #
        #
        #
        #
        #
        #
        #
        #
        #
        #
        #
        #ここだけ
        #
        #
        #
        #
        #
        #
        #
        #
        #
        #
        #
        #
        #
        aEndFlag = True

    for aItem in NPC_CHARS:
        if aNpc.get_name() == aItem.get("Name"):
            gEndChar.append(aItem.get("Id"))
    
    return not aEndFlag

#メイン関数
def Main():
    #ゲームだからきれいなほうがいい
    dispClear()

    #プレイヤーのキャラクターを選択させる
    selectChar()

    #戦闘入る前に画面をクリアする
    dispClear()

    #戦闘開始
    while len(gEndChar) != len(NPC_CHARS) - 1:
        if battleStart() != True:
            print("敗北")
            return

        #間をあける
        for i in range(3):
            print("\r\n")

    print("勝利")

#エントリーポイント
if __name__ == "__main__":
    Main()
