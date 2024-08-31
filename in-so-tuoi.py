# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 23:47:15 2024

@author: diemtrinh
"""
print("Nhập vào năm sinh, in ra tuổi.")
a= int(input("Nhập năm sinh của bạn:  "))
if 1<a<=2022:
    sotuoi= 2022-a
    print("Bạn sinh năm",a," vậy bạn",sotuoi,"tuổi")
else :
    print("Không hợp lệ")
