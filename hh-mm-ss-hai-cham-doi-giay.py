# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 18:18:34 2024

@author: diemtrinh
"""
print("Nhập vào giờ, phút và giây theo định dạng hh:mm:ss. Hãy đổi ra giây ")
a=int(input(" Nhập số giờ: "))
b=int(input(" Nhập số phút: "))
c=int(input(" Nhập số giây: "))
print(f"{a}:{b}:{c}")
tong_giay = a * 3600 + b * 60 + c
print(" Tổng số giây= ",tong_giay)