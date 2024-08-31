# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 18:43:19 2024

@author: diemtrinh
"""
print(" Cộng, trừ 2 giờ")
a= int(input("Nhập só giờ thứ nhất: "))
b= int(input("Nhập só phút thứ nhất: "))
c= int(input("Nhập só giây thứ nhất: "))
print(f"{a}giờ {b}phút {c}giây")
A= int(input("Nhập só giờ thứ hai: "))
B= int(input("Nhập só phút thứ hai: "))
C= int(input("Nhập só giây thứ hai: "))
print(f"{A}giờ {B}phút {C}giây")
x=a-A
y=b-B
z=c-C
print(f" Trừ hai giờ ta được {x}giờ {y}phút {z}giây")
X=a+A
Y=b+B
Z=c+C
print(f" Cộng hai giờ ta được {X}giờ {Y}phút {Z}giây")