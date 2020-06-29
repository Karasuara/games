#--------------------
#作者：閑徳
#概要:インポート
#--------------------
import random

#--------------------
#作者：閑徳
#概要:武将名
#--------------------
def busyou(b):
    if b==1:
        oda='織田信長'
        return oda
    if b==2:
        toyotomi='豊臣秀吉'
        return toyotomi
    if b==3:
        tokugawa='徳川家康'
        return tokugawa
    if b==4:
        imagawa='今川義元'
        return imagawa
    if b==5:
        takeda='武田信玄'
        return takeda
    if b==6:
        akechi='明智光秀'
        return akechi

#--------------------
#作者：閑徳
#概要:体力
#--------------------
def tairyoku(t):
    if t==1:
        oda_hp=10000
        return oda_hp
    if t==2:
        toyotomi_hp=10000
        return toyotomi_hp
    if t==3:
        tokugawa_hp=10000
        return tokugawa_hp
    if t==4:
        imagawa_hp=10000
        return imagawa_hp
    if t==5:
        takeda_hp=10000
        return takeda_hp
    if t==6:
        akechi_hp=10000
        return akechi_hp

#--------------------
#作者：閑徳
#概要:攻撃力
#--------------------
def kougeki(k):
    if k==1:
        oda_atk=800
        return oda_atk
    if k==2:
        toyotomi_atk=500
        return toyotomi_atk
    if k==3:
        tokugawa_atk=700
        return tokugawa_atk
    if k==4:
        imagawa_atk=400
        return imagawa_atk
    if k==5:
        takeda_atk=600
        return takeda_atk
    if k==6:
        akechi_atk=900
        return akechi_atk

#--------------------
#作者：閑徳
#防御力
#--------------------
def bougyo(b):
    if b==1:
        oda_def=200
        return oda_def
    if b==2:
        toyotomi_def=250
        return toyotomi_def
    if b==3:
        tokugawa_def=175
        return tokugawa_def
    if b==4:
        imagawa_def=200
        return imagawa_def
    if b==5:
        takeda_def=150
        return takeda_def
    if b==6:
        akechi_def=225
        return akechi_def

#--------------------
#作者：閑徳
#概要:素早さ
#--------------------
def subayasa(s):
    if s==1:
        oda_spe=100
        return oda_spe
    if s==2:
        toyotomi_spe=125
        return toyotomi_spe
    if s==3:
        tokugawa_spe=87
        return tokugawa_spe
    if s==4:
        imagawa_spe=100
        return imagawa_spe
    if s==5:
        takeda_spe=75
        return takeda_spe
    if s==6:
        akechi_spe=112
        return akechi_spe

#--------------------
#作者：閑徳
#概要:兵力
#--------------------
def heiryoku(h):
    if h==1:
        oda_hei=1000
        return oda_hei
    if h==2:
        toyotomi_hei=750
        return toyotomi_hei
    if h==3:
        tokugawa_hei=875
        return tokugawa_hei
    if h==4:
        imagawa_hei=600
        return imagawa_hei
    if h==5:
        takeda_hei=750
        return takeda_hei
    if h==6:
        akechi_hei=1125
        return akechi_hei

#--------------------
#作者：閑徳
#概要:特技
#--------------------
def tokugi(t):
    if t==1:
        oda_skl=1800
        return oda_skl
    if t==2:
        toyotomi_skl=1250
        return toyotomi_skl
    if t==3:
        tokugawa_skl=1574
        return tokugawa_skl
    if t==4:
        imagawa_skl=1000
        return imagawa_skl
    if t==5:
        takeda_skl=1350
        return takeda_skl
    if t==6:
        akechi_skl=2024
        return akechi_skl

#--------------------
#作者：閑徳
#概要:特技の容量
#--------------------
def pointo(p):
    if p==1:
        oda_pit=300
        return oda_pit
    if p==2:
        toyotomi_pit=300
        return toyotomi_pit
    if p==3:
        tokugawa_pit=300
        return tokugawa_pit
    if p==4:
        imagawa_pit=300
        return imagawa_pit
    if p==5:
        takeda_pit=300
        return takeda_pit
    if p==6:
        akechi_pit=300
        return akechi_pit

#--------------------
#作者：閑徳
#概要:特技の消費量
#--------------------
def shouhi(s):
    if s==1:
        oda_suh=50
        return oda_suh
    if s==2:
        toyotomi_suh=57
        return toyotomi_suh
    if s==3:
        tokugawa_suh=57
        return tokugawa_suh
    if s==4:
        imagawa_suh=71
        return imagawa_suh
    if s==5:
        takeda_suh=66
        return takeda_suh
    if s==6:
        akechi_suh=44
        return akechi_suh

#--------------------
#作者：閑徳
#概要:メインメニュー
#--------------------
def menu():
    print('********************')
    print('メニュー')
    print('--------------------')
    print('武将選択（数字）')
    print('--------------------')
    print('1.織田信長')
    print('2.豊臣秀吉')
    print('3.徳川家康')
    print('4.今川義元')
    print('5.武田信玄')
    print('6.明智光秀')
    print('********************')

#--------------------
#作者：閑徳
#概要:対戦シーン
#--------------------
def taisen():
    select=input('->')
    loop=1
    tt=0 #敵の体力の減少量
    th=0 #敵の兵力の減少量
    ts=0 #敵の特技消費量
    mt=0 #味方の体力の減少量
    mh=0 #味方の兵力の減少量
    ms=0 #味方の特技消費量
    while loop==1:
        if select=='1':
            print('********************')
            print(busyou(1)+'VS'+busyou(2))
            print('--------------------')
            print(busyou(2))
            print('体力')
            print(tairyoku(2)-tt)
            print('兵力')
            print(heiryoku(2)-th)
            print('TP')
            print(pointo(2)-ts)
            print('--------------------')
            print(busyou(1))
            print('体力')
            print(tairyoku(1)-mt)
            print('兵力')
            print(heiryoku(1)-mh)
            print('TP')
            print(pointo(1)-ms)
            print('********************')
            print('1.攻撃 2.特技')
            sentaku=input('->')
            if subayasa(1)>subayasa(2):
                if sentaku==1:
                    if heiryoku(2)>th:
                        th+=kougeki(1)
                    if heiryoku(2)<=th:
                        tt+=kougeki(1)-bougyo(2)
                        if tairyoku(2)<=tt:
                            print('勝利')
                            break
                    randamu=random.randint(1,2)
                    if randamu==1:
                        if heiryoku(1)>mh:
                            mh+=kougeki(2)
                        if heiryoku(1)<=mh:
                            mt+=kougeki(2)-bougyo(1)
                            if tairyoku(1)<=mt:
                                print('敗北')
                                break
                    if randamu==2:
                        if heiryoku(1)>mh:
                            mh+=tokugi(2)
                            ts+=shouhi(2)
                        if heiryoku(1)<=mh:
                            mt+=tokugi(2)-bougyo(1)
                            ts+=shouhi(2)
                            if tairyoku(1)<=mt:
                                print('敗北')
                                break
                if sentaku==2:
                    if heiryoku(2)>th:
                        th+=tokugi(1)
                        ms+=shouhi(1)
                    if heiryoku(2)<=th:
                        tt+=tokugi(1)-bougyo(2)
                        ms+=shouhi(1)
                        if tairyoku(2)<=tt:
                            print('勝利')
                            break
                    randamu=random.randint(1,2)
                    if randamu==1:
                        if heiryoku(1)>mh:
                            mh+=kougeki(2)
                        if heiryoku(1)<=mh:
                            mt+=kougeki(2)-bougyo(1)
                            if tairyoku(1)<=mt:
                                print('敗北')
                                break
                    if randamu==2:
                        if heiryoku(1)>mh:
                            mh+=tokugi(2)
                            ts+=shouhi(2)
                        if heiryoku(1)<=mh:
                            mt+=tokugi(2)-bougyo(1)
                            ts+=shouhi(2)
                            if tairyoku(1)<=mt:
                                print('敗北')
                                break
            if subayasa(1)<subayasa(2):
                randamu=random.randint(1,2)
                if randamu==1:
                    if heiryoku(1)>mh:
                        mh+=kougeki(2)
                    if heiryoku(1)<=mh:
                        mt+=kougeki(2)-bougyo(1)
                        if tairyoku(1)<=mt:
                            print('敗北')
                            break
                    if sentaku==1:
                        if heiryoku(2)>th:
                            th+=kougeki(1)
                        if heiryoku(2)<=th:
                            tt+=kougeki(1)-bougyo(2)
                            if tairyoku(2)<=tt:
                                print('勝利')
                                break
                    if sentaku==2:
                        if heiryoku(2)>th:
                            th+=tokugi(1)
                            ms+=shouhi(1)
                        if heiryoku(2)<=th:
                            tt+=tokugi(1)-bougyo(2)
                            ms+=shouhi(1)
                            if tairyoku(2)<=tt:
                                print('勝利')
                                break
                if randamu==2:
                    if heiryoku(1)>mh:
                        mh+=tokugi(2)
                        ts+=shouhi(2)
                    if heiryoku(1)<=mh:
                        mt+=tokugi(2)-bougyo(1)
                        ts+=shouhi(2)
                        if tairyoku(1)<=mt:
                            print('敗北')
                            break
                    if sentaku==1:
                        if heiryoku(2)>th:
                            th+=kougeki(1)
                        if heiryoku(2)<=th:
                            tt+=kougeki(1)-bougyo(2)
                            if tairyoku(2)<tt:
                                print('勝利')
                                break
                    if sentaku==2:
                        if heiryoku(2)>th:
                            th+=tokugi(1)
                            ms+=shouhi(1)
                        if heiryoku(2)<=th:
                            tt+=tokugi(1)-bougyo(2)
                            ms+=shouhi(1)
                            if tairyoku(2)<tt:
                                print('勝利')
                                break

#--------------------
#作者：閑徳
#プログラム実行部分
#--------------------
menu() #メインメニュー
taisen() #対戦シーン
