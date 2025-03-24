# -*- coding: utf-8 -*-
"""
Created on Mon Mar 24 23:25:18 2025

@author: asus
"""
noktalar= [(2,3),(5,3),(5,7),(8,9),(10,7)]
def euclideanDistance(tuple1,tuple2):
    if tuple1[0]==tuple2[0] and tuple1[1]!=tuple2[1]:
        mesafe = abs(tuple1[1]-tuple2[1])
    elif tuple1[1]==tuple2[1] and tuple1[0]!=tuple2[0]:
        mesafe = abs(tuple1[0]-tuple2[0])
    elif tuple1[1]==tuple2[1] and tuple1[0]==tuple2[0]:
        mesafe = 0
    else:
        mesafe = ((tuple1[0]-tuple2[0])**2 + (tuple1[1]-tuple2[1])**2 )**(1/2)
    return mesafe

distances = []
for i in range(len(noktalar)):
    j=i+1
    while j<len(noktalar):
        distances.append(euclideanDistance(noktalar[i], noktalar[j]))
        j = j+1
        