import math
class XL_PhuongTrinhBacHai():
    def __init__(self,_a,_b,_c):
        self.a=_a
        self.b=_b
        self.c=_c        
    def TimNghiem(self):
        nghiem=''
        if self.a==0:
            nghiem='Phuong trinh khong hop le'
        else:
            delta=self.b*self.b-4*self.a*self.c
            if delta<0:
                nghiem='Phuong trinh vo nghiem'
            elif delta==0:
                nghiem='Phuong trinh co nghiem kep x1 = x2 = '+ str(((-self.b)/(2*self.a)))
            else:
                x1=((-self.b+math.sqrt(delta))/(2*self.a))
                x2=((-self.b-math.sqrt(delta))/(2*self.a))
                nghiem='Phuong trinh co hai nghiem phan biet \n'
                nghiem+='x1 = ' + str(x1)
                nghiem+='x2 = ' + str(x2)
        return nghiem
    def __del__(self):
              
    