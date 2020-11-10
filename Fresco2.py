# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 17:34:49 2020

@author: bkkin
"""

import json
from datetime import datetime
import random
import pandas as pd
import glob
import os


def file_operation():
    isDeleted = False
    recall = False
    now = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("date and time =", dt_string)
    # file_path = "C:\Users\bkkin\OneDrive\Desktop\Hackthon"
    name = input("Enter your name : ")
    read_write = input("For Read -> 'R', Add ->'W' & Delete -> D & Recall->RE : ")
    if read_write == 'R':
        print("Wait a moment your file is opening for read........")
    elif read_write == 'D':
        filename = input("Enter a file name you want to delete : ")
        isDeleted = True
        writeToJSONFile(name, dt_string, filename, recall, isDeleted)
        delete_from_file(filename)
    elif read_write == 'RE':
        filename1 = input("Enter a file name you want to Recall : ")
        recall = True
        writeToJSONFile(name, dt_string, filename1, recall, isDeleted)
        write_in_recall_file(filename1)
    else:
        print("Wait a moment your file is opening for write........")
        content = input("Enter a content : ")
        # content_id = random.randint(000000,222222)
        copy_file(name, content, dt_string, recall, isDeleted)


""" This method handle operation related with File operation """


def copy_file(name, content, time, recall, isDeleted):
    with open('variable.txt', 'r') as f:
        value = f.read()
        latest_version = [int(x) for x in value.split()]
        lst = max(latest_version)
        print(lst)
    d = lst
    Directory = './DataFile/'
    filename = Directory + "DataFile_%d.txt" % d
    list_of_files = glob.glob('./DataFile/*')  # * means all if need specific format then *.csv
    latest_file = max(list_of_files, key=os.path.getctime)
    path, file = os.path.split(latest_file)
    print("latest file is:", file)
    lst_file = Directory + file
    print(lst_file)
    with open(lst_file, 'r') as f, open(filename, 'w') as f1:
        f1.writelines(f.readlines())
    f1.close()
    path1, file1 = os.path.split(filename)
    print("This is file :", file1)

    d += 1
    str_d = str(d)
    with open('variable.txt', 'w+') as v:
        v.write(str_d)

    write_in_file(file1, content)
    writeToJSONFile(name, time, filename, isDeleted, recall)


""" This method handle operation related with Write inn text file """


def write_in_file(file1, content):
    '''data = str(content)
    print(data)
    with open(file1, 'a') as lead:
        lead.write(data)'''

    with open(file1, 'w+') as f2:
        f_content = f2.read()
        print(f_content)
        f2.seek(0, 0)
        f2.write(content.rstrip('\r\n') + '\n' + f_content)
        print("content is written !!")


""" This method handle operation related with Delete """


def delete_from_file(filename):
    print("WE ARE HERE")
    cur_path = './DataFile/'
    dest_path = './MovedFile/'

    path1 = cur_path + filename
    path2 = dest_path + filename

    os.rename(path1, path2)
    print("File is Deleted")


""" This method handle operation related with Recall """


def write_in_recall_file(filename1):
    cur_path = './MovedFile/'
    dest_path = './DataFile/'

    path1 = cur_path + filename1
    path2 = dest_path + filename1

    os.rename(path1, path2)
    print("File is Recall")


""" This method handle operation related with json file """


def writeToJSONFile(user_name, time, file_name, recall, isDeleted):
    data = {}
    data['ModifiedBy'] = user_name
    data['ModifiedTime'] = time
    data['current_version'] = file_name
    data['IsRecall'] = recall
    data['IsDeleted'] = isDeleted
    with open('Directory.json', 'a') as outfile:
        json.dump(data, outfile)


if __name__ == "__main__":
    file_operation()
