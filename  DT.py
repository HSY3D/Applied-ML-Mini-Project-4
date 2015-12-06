# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 19:14:49 2015

@author: hannansyed
"""
from datetime import datetime
from sklearn import tree

import numpy
import csv
import re

train_inputs=[]
with open('train.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    next(reader, None)  # skip the header
    for row in reader:
        train_inputs.append(row)

train_outputs=[]
with open('train_outputs.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    next(reader, None)  # skip the header
    for row in reader:
        train_outputs.append(row)

#clf = tree.DecisionTreeClassifier()
#clf = clf.fit(train_inputs, train_outputs)

########### HELPER ###########    
def date(column):
    date_format = "%Y-%m-%d"
    for date_string in column:
        date_object = datetime.strptime(date_string,date_format)
        print date_object

def trap(column):
    new_column=[]
    for trap in column:
        trap_number = trap[1:]
        new_column.append(trap_number)
    return new_column

def species(column):
    new_column = []
    specie_list = []    
    for specie in column:
        if specie not in specie_list:
            specie_list.append(specie)
            new_column.append(specie_list.index(specie))
        else:
            new_column.append(specie_list.index(specie))
    return new_column   
    
def getColumn(train_inputs, column_num):
    column=[]    
    for row in range(len(train_inputs)):
        column.append(train_inputs[row][column_num])
    return column

print species(getColumn(train_inputs, 2))