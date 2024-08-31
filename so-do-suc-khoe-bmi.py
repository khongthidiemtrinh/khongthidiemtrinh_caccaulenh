# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 19:02:16 2024

@author: diemtrinh
"""
print(" Tính số đo kiểm tra sức khỏe BMI.")
a= float(input(" Nhập cân nặng của bạn nhaa(kg):  "))
b= float(input(" Nhập chiều cao của bạn đi nè(m):  "))
BMI= a/b**2
print(" Chỉ số BMI của bạn là:  ", BMI)
if BMI<16:
    print(" Ôi không!! Bạn gầy độ III")
elif 16<=BMI<17:
    print(" Hmm.. Bạn gầy độ II nhée")
elif 17<=BMI<18.5:
    print(" Ô!. Bạn gầy độ I nhée")
elif 18.5<=BMI<25:
    print(" Chúc mừng! Bạn ở mức độ bình thường nèe")
elif 25<=BMI<30:
    print(" Hmm.. Bạn hơi thừa cân rồi")
elif 30<=BMI<35:
    print(" Bạn béo phì độ I")
elif 35<=BMI<40:
    print(" Hmm.. Bạn béo phì độ II nhée")
elif BMI<=40:
    print(" Bạn béo phì độ III rồi giảm cân thôi")jjjjj