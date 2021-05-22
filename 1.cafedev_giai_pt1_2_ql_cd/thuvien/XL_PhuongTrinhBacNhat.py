class XL_PhuongTrinhBachNhat():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def TimNghiem(self):
        if self.a==0 and self.b==0:
            return 'Phuong trinh vo so nghiem'
        elif self.a==0 and self.b!=0:
            return 'Phuong trinh vo nghiem'
        else:
            return 'Nghiem cua phuong trinh : ' + str((-self.b/self.a))            
            