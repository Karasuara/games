import random           #乱数用
import os               #コンソール操作用
import Status as Stas   #自作モジュールのインポート

#定数群
NPC_CHARS = [
    {"Id":1, "Name":"織田信長", "Hp":10000, "Atk":800, "Def":400, "Spe":200, "Force":1200, "Skill":2000, "point":300, "Cost":50, "All":14700 },
    {"Id":2, "Name":"豊臣秀吉", "Hp":10000, "Atk":500, "Def":750, "Spe":375, "Force":1250, "Skill":1750, "point":300, "Cost":57, "All":14550 },
    {"Id":3, "Name":"徳川家康", "Hp":10000, "Atk":700, "Def":350, "Spe":175, "Force":1050, "Skill":1750, "point":300, "Cost":57, "All":14150 },
    {"Id":4, "Name":"今川義元", "Hp":10000, "Atk":400, "Def":600, "Spe":300, "Force":1000, "Skill":1400, "point":300, "Cost":71, "All":13700 },
    {"Id":5, "Name":"武田信玄", "Hp":10000, "Atk":600, "Def":300, "Spe":150, "Force":900,  "Skill":1500, "point":300, "Cost":66, "All":136000},
    {"Id":6, "Neme":"明智光秀", "Hp":10000, "Atk":900, "Def":450, "Spe":225, "Force":1350, "Skill":2250, "point":300, "Cost":44, "All":15250 },
]

#グローバル変数群
gPlayer = Stas.clsStatus()

#表示されている画面を奇麗にする
def dispClear():
    os.system("cls")

def dispChars():
    print("********************")
    print("--------------------")
    print("武将選択（数字）")
    print("--------------------")
    for i in range(len(NPC_CHARS)):
        print(str(NPC_CHARS[i].get("Id")) + "." + NPC_CHARS[i].get("Name"))

    print("********************")

def selectChar():
    dispChars()

#メイン関数
def Main():
    selectChar()

    print(NPC_CHARS)
    # dispClear()
    
    # gPlayer.setDatas("aa", 1, 2, 3)
    # gPlayer.dispDatas()

#エントリーポイント
if __name__ == "__main__":
    Main()
