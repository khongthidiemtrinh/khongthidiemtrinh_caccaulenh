# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 19:01:26 2024

@author: diemtrinh
"""
d= int(input("Nhập ngày sinh của bạn: "))
m= int(input("Nhập tháng sinh của bạn: "))
y = int(input("Nhập năm sinh của bạn: "))
#Ngày/tháng/năm
print(f"{d}/{m}/{y}")
#Ngày/tháng/năm
z=y%100
print(f"{d}/{m}/{z}")
#Năm/tháng/ngày 
print(f"{y}/{m}/{d}")
