# -----------------------------------------------------------
#Cafedev.vn - Kênh thông tin IT hàng đầu Việt Nam
#@author cafedevn
#Contact: cafedevn@gmail.com
#Fanpage: https://www.facebook.com/cafedevn
#Group: https://www.facebook.com/groups/cafedev.vn/
#Instagram: https://instagram.com/cafedevn
#Twitter: https://twitter.com/CafedeVn
#Linkedin: https://www.linkedin.com/in/cafe-dev-407054199/
#Pinterest: https://www.pinterest.com/cafedevvn/
#YouTube: https://www.youtube.com/channel/UCE7zpY_SlHGEgo67pHxqIoA/
# -----------------------------------------------------------

from thuvien.XL_PhuongTrinhBacHai import *
a,b,c=eval(input('Nhap he so a,b,c'))
XL_PTBHai= XL_PhuongTrinhBacHai(a,b,c)
Nghiem=XL_PTBHai.TimNghiem()
print(XL_PTBHai.a)
setattr(XL_PTBHai,'a',123)
