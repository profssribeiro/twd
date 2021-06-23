# Author: Sergio Ribeiro (2021)

class TWD:
    def __init__(self, DS=[],A=[]):
        self.DS = DS
        self.A = A
    
    def getU(self):
        return set([o for o in range(len(self.DS))])

    def getX(self,Vd):
        X = []
        for o in range(len(self.DS)):
            if self.DS[o][len(self.A)]==Vd:
                X.append(o)
        return set(X)

    def getVa(self,a=""):
        Va = []
        if a in self.A:
            Va = set([i[self.A.index(a)] for i in self.DS])
        elif a=="":
            for a in self.A:
                Va.append( set([i[self.A.index(a)] for i in self.DS]) )
        return Va

    def getVd(self):
        return set([i[len(self.A)] for i in self.DS])

    def getIND(self,P=[]):
        IND  = []
        unique = []
        
        if P == []:
            P = self.A

        for o in range(len(self.DS)):
            Vo = []
            for a in self.A:
                if a in P:
                    Vo.append( self.DS[o][self.A.index(a)] )
            if Vo not in unique:
                unique.append(Vo)
                IND.append([o])
            elif Vo in unique:
                i = unique.index(Vo)
                if isinstance(IND[i], list):
                    IND[i].append(o)
                else:
                    IND[i]=[IND[i]]
                    IND[i].append(o)
        return IND

    def getLowerAX(self,X,IND):
        lowerAX = []
        for i in range(len(IND)):
            if set(IND[i]).issubset(X):
                for n in range(len(IND[i])):
                    lowerAX.append(IND[i][n])
        return set(lowerAX)
    
    def getUpperAX(self,X,IND):
        upperAX = []
        for i in range(len(IND)):
            if len(set(IND[i]).intersection(set(X)))>0:
                for n in range(len(IND[i])):
                    upperAX.append(IND[i][n])
        return set(upperAX)

    def getPOSX(self,X,IND):
        return self.getLowerAX(X,IND)

    def getBNDX(self,X,IND):
        return self.getUpperAX(X,IND) - self.getLowerAX(X,IND)

    def getNEGX(self,X,IND):
        return self.getU()-(self.getPOSX(X,IND).union(self.getBNDX(X,IND)))
    
    def getRules(self,region,P=[]):
        if P == []:
            P = self.A
        rules = ""
        count = 0
        for i in region:
            count+=1
            rule = ""
            for n in range(len(self.A)):
                if not rule:
                    rule += P[n] + " == " + str(self.DS[i][n])
                else:
                    if n > 0:
                        rule += " AND "
                    rule += P[n] + " == " + str(self.DS[i][n])
            if rule not in rules:
                rules += "\n ["+str(count)+"] " + rule
        return rules
        
    def precision(self,X,IND):
        return len(self.getLowerAX(X,IND))/len(self.getUpperAX(X,IND))

    def quality(self,X,IND):
        return (len(self.getPOSX(X,IND))+len(self.getNEGX(X,IND)))/len(self.getU())
    
    def roughness(self,X,IND):
        return len(self.getBNDX(X,IND))/len(self.getU())

    def comb(self,inp, temp=[], ans=[]):
        for i in range(len(inp)):
            current = inp[i]
            remaining = inp[i + 1:]
            temp.append(current)
            ans.append(list(temp))
            self.comb(remaining, temp, ans)
            temp.pop()
        return ans

    def getReduct(self):
        ind = self.getIND()
        red = []
        comb = self.comb(self.A)
        for a in comb:
            if self.getIND(a) == ind and a != self.A:
                red.append(a)
        return red


