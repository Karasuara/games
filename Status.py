class clsStatus:
    #イニシャライズ
    def __init__(self):
        self.Name = "" #名前
        self.Hp = 0    #ヒットポイント
        self.Atk = 0   #攻撃力
        self.Def = 0   #防御力
        self.Spe = 0   #スピード　ターンに関係ある？
        self.Force = 0 #兵力
        self.Skill = 0 #スキル　何に使うのかなぞ　説明求む
        self.Point = 0 #ポイント　何に使うのかなぞ　説明求む
        self.Cost = 0  #コスト
        self.All = 0   #総合力

    #一括ですべてのステータスに値を入れる
    def setDatas(self, pName, pHp, pAtk, pDef, pSpe, pForce, pSkill, pPoint, pCost, pAll):
        self.Name = pName
        self.Hp = pHp
        self.Atk = pAtk
        self.Def = pDef
        self.Spe = pSpe
        self.Force = pForce
        self.Skill = pSkill
        self.Point = pPoint
        self.Cost = pCost
        self.All = pAll

    #name
    def get_name(self):
        return self.Name
    def set_name(self,pName):
        self.Name = pName
        
    #hp
    def get_hp(self):
        return self.Hp
    def set_hp(self,pHp):
        self.Hp = pHp
       
    #atk 
    def get_atk(self):
        return self.Atk
    def set_atk(self,pAtk):
        self.Atk = pAtk
        
    #def
    def get_def(self):
        return self.Def
    def set_def(self,pDef):
        self.Def = pDef
        
    #spe
    def get_spe(self):
        return self.Spe
    def set_spe(self,pSpe):
        self.Spe = pSpe

    #force
    def get_force(self):
        return self.Force
    def set_force(self,pForce):
        self.Force = pForce
        
    #skill
    def get_skill(self):
        return self.Skill
    def set_skill(self,pSkill):
        self.Skill = pSkill

    #point
    def get_point(self):
        return self.Point
    def set_point(self,pPoint):
        self.Point = pPoint
        
    #cost
    def get_cost(self):
        return self.Cost
    def set_cost(self,pCost):
        self.Cost = pCost
        
    #all
    def get_all(self):
        return self.All
    def set_all(self,pAll):
        self.All = pAll

    #必要データの出力
    def dispDatas(self):
        print("名前\t" + self.Name)
        print("体力\t" + str(self.Hp))
        print("兵力\t" + str(self.Force))
        print("総合\t" + str(self.All))