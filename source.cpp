//--------------------
//題名:戦国大戦 Origin
//作者:kamazyou
//--------------------

//--------------------
//作者:kamazyou
//--------------------
#include<iostream>
#include<random>

//--------------------
//作者:kamazyou
//--------------------
using namespace std;

//--------------------
//作者:kamazyou
//--------------------
int select;
int sentaku;
int flag;

//--------------------
//作者:kamazyou
//--------------------
struct busyou {
  string oda;
  string toyotomi;
  string tokugawa;
  string imagawa;
  string takeda;
  string akechi;
};

//--------------------
//作者:kamazyou
//--------------------
struct tairyoku {
  int oda;
  int toyotomi;
  int tokugawa;
  int imagawa;
  int takeda;
  int akechi;
};

//--------------------
//作者:kamazyou
//--------------------
struct kougeki {
  int oda;
  int toyotomi;
  int tokugawa;
  int imagawa;
  int takeda;
  int akechi;
};

//--------------------
//作者:kamazyou
//--------------------
struct bougyo {
  int oda;
  int toyotomi;
  int tokugawa;
  int imagawa;
  int takeda;
  int akechi;
};

//--------------------
//作者:kamazyou
//--------------------
struct heiryoku {
  int oda;
  int toyotomi;
  int tokugawa;
  int imagawa;
  int takeda;
  int akechi;
};

//--------------------
//作者:kamazyou
//--------------------
struct tokugi {
  int oda;
  int toyotomi;
  int tokugawa;
  int imagawa;
  int takeda;
  int akechi;
};

//--------------------
//作者:kamazyou
//--------------------
struct point {
  int oda;
  int toyotomi;
  int tokugawa;
  int imagawa;
  int takeda;
  int akechi;
};

struct syouhi {
  int oda;
  int toyotomi;
  int tokugawa;
  int imagawa;
  int takeda;
  int akechi;
};

struct subayasa {
  int oda;
  int toyotomi;
  int tokugawa;
  int imagawa;
  int takeda;
  int akechi;
};

//--------------------
//作者:kamazyou
//--------------------
string kyarakuta(int b) {
  busyou bsu;
  if (b == 1) {
    bsu.oda = "織田信長";
    return bsu.oda;
  }
  if (b == 2) {
    bsu.toyotomi = "豊臣秀吉";
    return bsu.toyotomi;
  }
  if (b == 3) {
    bsu.tokugawa = "徳川家康";
    return bsu.tokugawa;
  }
  if (b == 4) {
    bsu.imagawa = "今川義元";
    return bsu.imagawa;
  }
  if (b == 5) {
    bsu.takeda = "武田信玄";
    return bsu.takeda;
  }
  if (b == 6) {
    bsu.akechi = "明智光秀";
    return bsu.akechi;
  }
}

//--------------------
//作者:kamazyou
//--------------------
int hp(int h) {
  tairyoku trk;
  if (h == 1) {
    trk.oda = 10000;
    return trk.oda;
  }
  if (h == 2) {
    trk.toyotomi = 10000;
    return trk.toyotomi;
  }
  if (h == 3) {
    trk.tokugawa = 10000;
    return trk.tokugawa;
  }
  if (h == 4) {
    trk.imagawa = 10000;
    return trk.imagawa;
  }
  if (h == 5) {
    trk.takeda = 10000;
    return trk.takeda;
  }
  if (h == 6) {
    trk.akechi = 10000;
    return trk.akechi;
  }
}

//--------------------
//作者:kamazyou
//--------------------
int atk(int a) {
  kougeki kgk;
  if (a == 1) {
    kgk.oda = 800;
    return kgk.oda;
  }
  if (a == 2) {
    kgk.toyotomi = 500;
    return kgk.toyotomi;
  }
  if (a == 3) {
    kgk.tokugawa = 700;
    return kgk.tokugawa;
  }
  if (a == 4) {
    kgk.imagawa = 400;
    return kgk.imagawa;
  }
  if (a == 5) {
    kgk.takeda = 600;
    return kgk.takeda;
  }
  if (a == 6) {
    kgk.akechi = 900;
    return kgk.akechi;
  }
}

//--------------------
//作者:kamazyou
//--------------------
int def(int d) {
  bougyo bug;
  if (d == 1) {
    bug.oda = 400;
    return bug.oda;
  }
  if (d == 2) {
    bug.toyotomi = 750;
    return bug.toyotomi;
  }
  if (d == 3) {
    bug.tokugawa = 350;
    return bug.tokugawa;
  }
  if (d == 4) {
    bug.imagawa = 600;
    return bug.imagawa;
  }
  if (d == 5) {
    bug.takeda = 300;
    return bug.takeda;
  }
  if (d == 6) {
    bug.akechi = 450;
    return bug.akechi;
  }
}

//--------------------
//作者:kamazyou
//--------------------
int hayasa(int h) {
  subayasa sbys;
  if (h == 1) {
    sbys.oda = 200;
    return sbys.oda;
  }
  if (h == 2) {
    sbys.toyotomi = 375;
    return sbys.toyotomi;
  }
  if (h == 3) {
    sbys.tokugawa = 175;
    return sbys.tokugawa;
  }
  if (h == 4) {
    sbys.imagawa = 300;
    return sbys.imagawa;
  }
  if (h == 5) {
    sbys.takeda = 150;
    return sbys.takeda;
  }
  if (h == 6) {
    sbys.akechi = 225;
    return sbys.akechi;
  }
}

//--------------------
//作者:kamazyou
//--------------------
int teshita(int t) {
  heiryoku hrk;
  if (t == 1) {
    hrk.oda = 1200;
    return hrk.oda;
  }
  if (t == 2) {
    hrk.toyotomi = 1250;
    return hrk.toyotomi;
  }
  if (t == 3) {
    hrk.tokugawa = 1050;
    return hrk.tokugawa;
  }
  if (t == 4) {
    hrk.imagawa = 1000;
    return hrk.imagawa;
  }
  if (t == 5) {
    hrk.takeda = 900;
    return hrk.takeda;
  }
  if (t == 6) {
    hrk.akechi = 1350;
    return hrk.akechi;
  }
}

//--------------------
//作者:kamazyou
//--------------------
int ougi(int o) {
  tokugi tkg;
  if (o == 1) {
    tkg.oda = 2000;
    return tkg.oda;
  }
  if (o == 2) {
    tkg.toyotomi = 1750;
    return tkg.toyotomi;
  }
  if (o == 3) {
    tkg.tokugawa = 1750;
    return tkg.tokugawa;
  }
  if (o == 4) {
    tkg.imagawa = 1400;
    return tkg.imagawa;
  }
  if (o == 5) {
    tkg.takeda = 1500;
    return tkg.takeda;
  }
  if (o == 6) {
    tkg.akechi = 2250;
    return tkg.akechi;
  }
}

//--------------------
//作者:kamazyou
//--------------------
int tp(int t) {
  point pit;
  if (t == 1) {
    pit.oda = 300;
    return pit.oda;
  }
  if (t == 2) {
    pit.toyotomi = 300;
    return pit.toyotomi;
  }
  if (t == 3) {
    pit.tokugawa = 300;
    return pit.tokugawa;
  }
  if (t == 4) {
    pit.imagawa = 300;
    return pit.imagawa;
  }
  if (t == 5) {
    pit.takeda = 300;
    return pit.takeda;
  }
  if (t == 6) {
    pit.akechi = 300;
    return pit.akechi;
  }
}

//--------------------
//作者:kamazyou
//--------------------
int gensyou(int g) {
  syouhi suh;
  if (g == 1) {
    suh.oda = 50;
    return suh.oda;
  }
  if (g == 2) {
    suh.toyotomi = 57;
    return suh.toyotomi;
  }
  if (g == 3) {
    suh.tokugawa = 57;
    return suh.tokugawa;
  }
  if (g == 4) {
    suh.imagawa = 71;
    return suh.imagawa;
  }
  if (g == 5) {
    suh.takeda = 66;
    return suh.takeda;
  }
  if (g == 6) {
    suh.akechi = 44;
    return suh.akechi;
  }
}

//--------------------
//作者:kamazyou
//--------------------
void menu() {
  cout << "********************" << endl;
  cout << "メニュー" << endl;
  cout << "--------------------" << endl;
  cout << "武将選択（数字）" << endl;
  cout << "--------------------" << endl;
  cout << "1." << kyarakuta(1) << endl;
  cout << "2." << kyarakuta(2) << endl;
  cout << "3." << kyarakuta(3) << endl;
  cout << "4." << kyarakuta(4) << endl;
  cout << "5." << kyarakuta(5) << endl;
  cout << "6." << kyarakuta(6) << endl;
  cout << "********************" << endl;
  cout << "->";
  cin >> select;
}

//--------------------
//作者:kamazyou
//--------------------
void taisen() {
  if (select == 1) {
    flag = 0;
    int mh;
    int mt;
    int th;
    int tt;
    int me;
    mh = 0;
    mt = 0;
    th = 0;
    tt = 0;
    me = 0;
    while (flag == 0) {
      cout << "********************" << endl;
      cout << kyarakuta(1) << "VS" << kyarakuta(2) << endl;
      cout << "--------------------" << endl;
      cout << kyarakuta(2) << endl;
      cout << "HP:" << hp(2) - th << endl;
      cout << "兵:" << teshita(2) - tt << endl;
      cout << "--------------------" << endl;
      cout << kyarakuta(1) << endl;
      cout << "HP:" << hp(1) - mh << endl;
      cout << "兵:" << teshita(1) - mt << endl;
      cout << "TP:" << tp(1) - me << endl;
      cout << "********************" << endl;
      cout << "1.攻撃 2.特技" << endl;
      cin >> sentaku;
      if (sentaku == 1) {
        if (teshita(2) > tt) {
          tt += atk(1);
        }
        if (teshita(2) <= tt) {
          th += atk(1);
          if (hp(2) <= th) {
            cout << "勝利" << endl;
            flag = 1;
          }
        }
      }
      if (sentaku == 2) {
        if (teshita(2) > tt) {
          tt += ougi(1);
          me += gensyou(1);
        }
        if (teshita(2) <= tt) {
          th += ougi(1);
          me += gensyou(1);
          if (hp(2) <= th) {
            cout << "勝利" << endl;
            flag = 1;
          }
        }
      }
    }
  }
}

//--------------------
//作者:kamazyou
//--------------------
void tekidousa() {
  if (select == 1) {

  }
}

//--------------------
//作者:kamazyou
//--------------------
int main() {
  menu();
  taisen();
}
