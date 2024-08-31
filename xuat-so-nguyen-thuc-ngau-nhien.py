# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 19:54:39 2024

@author: diemtrinh
"""
print("Xuất ra một số (nguyên, thực) ngẫu nhiên theo yêu cầu ")
import random
# 0 đến 100
a= random.randint(0,10)
b= random.uniform(0,10)
print(" Số nguyên ngẫu nhiên đươc xuất ra là: ", a)
print(" Số thực ngẫu nhiên đươc xuất ra là: ", b)
# 50 đến 99
a= random.randint(5,99)
b= random.uniform(5,99)
print(" Số nguyên ngẫu nhiên đươc xuất ra là: ", a)
print(" Số thực ngẫu nhiên đươc xuất ra là: ", b)
# -39 đến 79
a= random.randint(-39,79)
b= random.uniform(-39,79)
print(" Số nguyên ngẫu nhiên đươc xuất ra là: ", a)
print(" Số thực ngẫu nhiên đươc xuất ra là: ", b)
# -79 đến -39
a= random.randint(-79,-39)
b= random.uniform(-79,-39)
print(" Số nguyên ngẫu nhiên đươc xuất ra là: ", a)
print(" Số thực ngẫu nhiên đươc xuất ra là: ", b)