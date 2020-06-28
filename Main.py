import random           #乱数用
import os               #コンソール操作用
import Status as Stas   #自作モジュールのインポート


# #定数群
# NPC_NOB


oda = {"name":"織田信長", "hp":10000, "atk":800, "def":400, "spe":200, "force":1200, "skill":2000, "point":300, "cost":50, "all":14700}
hideyosi = {"name":"豊臣秀吉","hp":10000, "atk":500, "def":750, "spe":375, "force":1250, "skill":1750, "point":300, "cost":57, "all":14550}
ieyasu = {"name":"徳川家康", "hp":10000, "atk":700, "def":350, "spe":175, "force":1050, "skill":1750, "point":300, "cost"57, "all"14150}
imakawa = {"name","今川義元", "hp":10000, "atk":400, "def":600, "spe"300, "force":1000, "skill":1400, "point":300, "cost":71, "all":13700}
singen ={"name":"武田信玄", "hp":10000, "atk":600, "def":300, "spe":150, "force":900,  "skill":1500, "point":300, "cost":66, "all":136000}
aketi = {"neme":"明智光秀", "hp":10000, "atk":900, "def":450, "spe"225, "force":1350, "skill":2250, "point":300, "cost":44, "all"15250}

#グローバル変数群
gPlayer = Stas.clsStatus()

#表示されている画面を奇麗にする
def dispClear():
    os.system("cls")

#メイン関数
def Main():
    dispClear()
    
    gPlayer.setDatas("aa", 1, 2, 3)
    gPlayer.dispDatas()

#エントリーポイント
if __name__ == "__main__":
    Main()
