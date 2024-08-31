# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 18:34:25 2024

@author: Admin
"""
print("Đổi từ giờ/phút/giây thành giây. ")
a=int(input(" Nhập số giờ: "))
b=int(input(" Nhập số phút: "))
c=int(input(" Nhập số giây: "))
print(f"{a}g{b}p{c}s")
tong_giay = a * 3600 + b * 60 + c
print(" Tổng số giây= ",tong_giay)
