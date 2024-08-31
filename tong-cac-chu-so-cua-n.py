# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 18:29:54 2024

@author: diemtrinh
"""
print(" Tổng các chữ số của N")
n=int(input(" Nhập số nguyên N= "))
a=n//10
b=n%10
tong=a+b
if 10 <= n <= 99: print("Tổng các chữ số của N:", tong)
else: print(" Không hợp lệ")
