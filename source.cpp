//--------------------
//題名:戦国大戦 Origin
//作者:kamazyou
//--------------------

//--------------------
//作者:kamazyou
//--------------------
#include<iostream>

//--------------------
//作者:kamazyou
//--------------------
using namespace std;

//--------------------
//作者:kamazyou
//--------------------
int flag;
int select;

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
    kgk.imagawa = 600;
    return kgk.imagawa;
  }
  if (a == 5) {
    kgk.takeda = 800;
    return kgk.takeda;
  }
  if (a == 6) {
    kgk.akechi = 600;
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
    bug.imagawa = 300;
    return bug.imagawa;
  }
  if (d == 5) {
    bug.takeda = 400;
    return bug.takeda;
  }
  if (d == 6) {
    bug.akechi = 300;
    return bug.akechi;
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
    hrk.imagawa = 900;
    return hrk.imagawa;
  }
  if (t == 5) {
    hrk.takeda = 1200;
    return hrk.takeda;
  }
  if (t == 6) {
    hrk.akechi = 900;
    return hrk.akechi;
  }
}

//--------------------
//作者:kamazyou
//--------------------
int ougi(int o) {
  tokugi tkg;
  if (o == 1) {
    tkg.oda = 1600;
    return tkg.oda;
  }
  if (o == 2) {
    tkg.toyotomi = 1000;
    return tkg.toyotomi;
  }
  if (o == 3) {
    tkg.tokugawa = 1400;
    return tkg.tokugawa;
  }
  if (o == 4) {
    tkg.imagawa = 1200;
    return tkg.imagawa;
  }
  if (o == 5) {
    tkg.takeda = 1600;
    return tkg.takeda;
  }
  if (o == 6) {
    tkg.akechi = 1200;
    return tkg.akechi;
  }
}

//--------------------
//作者:kamazyou
//--------------------
int tp(int t) {
  point pit;
  if (t == 1) {
    pit.oda = 100;
    return pit.oda;
  }
  if (t == 2) {
    pit.toyotomi = 100;
    return pit.toyotomi;
  }
  if (t == 3) {
    pit.tokugawa = 100;
    return pit.tokugawa;
  }
  if (t == 4) {
    pit.imagawa = 100;
    return pit.imagawa;
  }
  if (t == 5) {
    pit.takeda = 100;
    return pit.takeda;
  }
  if (t == 6) {
    pit.akechi = 100;
    return pit.akechi;
  }
}

//--------------------
//作者:kamazyou
//--------------------
int gensyou(int g) {
  syouhi suh;
  if (g == 1) {
    suh.oda = 40;
    return suh.oda;
  }
  if (g == 2) {
    suh.toyotomi = 25;
    return suh.toyotomi;
  }
  if (g == 3) {
    suh.tokugawa = 35;
    return suh.tokugawa;
  }
  if (g == 4) {
    suh.imagawa = 30;
    return suh.imagawa;
  }
  if (g == 5) {
    suh.takeda = 40;
    return suh.takeda;
  }
  if (g == 6) {
    suh.akechi = 30;
    return suh.akechi;
  }
}

//--------------------
//作者:kamazyou
//--------------------
void menu() {
  flag = 0;
  cout << "********************\n";
  cout << "メニュー\n";
  cout << "--------------------\n";
  cout << "武将選択（数字）\n";
  cout << "--------------------\n";
  cout << "1." + kyarakuta(1) + "\n";
  cout << "2." + kyarakuta(2) + "\n";
  cout << "3." + kyarakuta(3) + "\n";
  cout << "4." + kyarakuta(4) + "\n";
  cout << "5." + kyarakuta(5) + "\n";
  cout << "6." + kyarakuta(6) + "\n";
  cout << "********************\n";
  cout << "->";
  cin >> select;
}

//--------------------
//作者:kamazyou
//--------------------
void seigyo(int s) {
  if (s == 1) {
    hp(1);
    atk(1);
    def(1);
    teshita(1);
    ougi(1);
    tp(1);
    gensyou(1);
  }
  if (s == 2) {
    hp(2);
    atk(2);
    def(2);
    teshita(2);
    ougi(2);
    tp(2);
    gensyou(2);
  }
  if (s == 3) {
    hp(3);
    atk(3);
    def(3);
    teshita(3);
    ougi(3);
    tp(3);
    gensyou(3);
  }
  if (s == 4) {
    hp(4);
    atk(4);
    def(4);
    teshita(4);
    ougi(4);
    tp(4);
    gensyou(4);
  }
  if (s == 5) {
    hp(5);
    atk(5);
    def(5);
    teshita(5);
    ougi(5);
    tp(5);
    gensyou(5);
  }
  if (s == 6) {
    hp(6);
    atk(6);
    def(6);
    teshita(6);
    ougi(6);
    tp(6);
    gensyou(6);
  }
}

//--------------------
//作者:kamazyou
//--------------------
void taisen() {
  if (select == 1) {
    seigyo(1);
    seigyo(2);
    cout << "********************\n";
    cout << kyarakuta(1) + "VS" + kyarakuta(2) + "\n";
    cout << "--------------------\n";
    cout << kyarakuta(2) + "\n";
    cout << teshita(2) + "\n";
    cout << "--------------------\n";
    cout << kyarakuta(1) + "\n";
    cout << teshita(1) + "\n";
    cout << tp(1) + "\n";
    cout << "********************\n";
    cout << "1.攻撃 2.特技\n";
  }
  if (select == 2) {
    cout << kyarakuta(2) + "VS" + kyarakuta(1) + "\n";
  }
}

//--------------------
//作者:kamazyou
//--------------------
int main() {
  menu();
}
