# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 18:04:47 2024

@author: diemtrinh
"""
print("Nhập hai số a, b. Sau đó, tính toán biểu thức ")
a=float(input(" Nhập sô a= "))
b=float(input(" Nhập sô b= "))
A= ((a+b)/((a**1/3)+(b**1/3)))/((a**1/3)-(b**1/3))**2
print(" Kết quả của biểu thức là: ",A)