# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 18:02:41 2024

@author: diemtrinh
"""
print("Chia lấy phần nguyên và phần dư của a với b ")
a=int(input("Nhập số nguyên dương a="))
b=int(input(" Nhập số nguyên dương b="))
if a >= 0 and b >= 0: 
    c= a//b 
    print(" Chia lấy phần nguyên =", c)
    d= a%b
    print(" chia lấy phần dư= ", d)
else:
    print(" Không hơp lệ")



