# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 19:36:26 2024

@author: diemtrinh
"""
a= int(input("Nhập số xe thứ nhất:  "))
b= int(input("Nhập số xe thứ hai:  "))
c= int(input("Nhập số xe thứ ba:  "))
d= int(input("Nhập số xe thứ tư:  "))
e= a+b+c+d
if 0<e<10:
    print(" Số nút từ số xe của bạn là:  ",e)
elif e>= 10:
    sonut=e//10+e%10
    print(" Số nút từ số xe của bạn là:  ",sonut)
else :
    print(" Không hợp lệ")