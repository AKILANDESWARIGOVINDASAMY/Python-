import glob
import os
import json
import shutil
from os.path import splitext


print("List of files", glob.glob('*.json'))
filename = "Version.json"
with open(filename, 'r') as ver:
        new = json.load(ver)
        e= new['Data1']+1
with open('Version.json', 'w') as updated:
        json.dump(new, updated)
modifyfile=input("Filename to modify")
x = splitext(modifyfile)
with open(modifyfile, 'r') as f:
    data = json.load(f)
    data = input("Enter the value you want to update")
with open("%s.%d.json"%(x[0], new['Data1']), 'w') as updated:
    json.dump(data, updated)



'''
filename = "Version.json"
with open(filename, 'r') as ver:
        new = json.load(ver)
        e= new['Data1']
        new['Data1']=e+1
with open('Version.json', 'w') as updated:
            json.dump(new, updated)
modifyfile=input("Filename to modify")
x = str(splitext(modifyfile))
with open(modifyfile, 'r') as f:
    data = json.load(f)
    data['Name'] = input("Enter the value you want to update")
with open("%s%s.json"%(x, new['Data1']), 'w') as updated:
    json.dump(data, updated)'''



'''
P1=json.dumps(Person1)
with open("Data.%s.json" % new['Data1']%filename,"w") as File:
    File.write(P1)
P2 = json.dumps(Person2)
with open("Data2.json", "w") as File:
        File.write(P2)
P3 = json.dumps(Person3)
with open("Data3.json", "w") as File:
        File.write(P3)


#updateing versions
def func1():
        filename = "Version.json"
        with open(filename, 'r') as ver:
            new = json.load(ver)
            e= new['Data1']
            new['Data1']=e+1
            with open("Data1.%s.json" % new['Data1'], 'w') as updated_file:
                json.dump(data, updated_file)
            shutil.copy(filename, "old")
        with open('Version.json', 'w') as updated:
            json.dump(new, updated)

def func2():
    filename = "Version.json"
    with open(filename, 'r') as ver:
        new = json.load(ver)
        e = new['Data2']
        new['Data2'] = e + 1
        with open("Data2.%s.json" % new['Data2'], 'w') as updated_file:
            json.dump(data, updated_file)
            shutil.copy(filename, "old")
        with open('Version.json', 'w') as updated:
            json.dump(new, updated)

def func3():
    filename = "Version.json"
    with open(filename, 'r') as ver:
        new = json.load(ver)
        e = new['Data3']
        new['Data3'] = e + 1
        with open("Data3.%s.json" % new['Data3'], 'w') as updated_file:
            json.dump(data, updated_file)
            shutil.copy(filename, "old")
        with open('Version.json', 'w') as updated:
            json.dump(new, updated)



filename1 = input("Enter the filename want to edit")
with open(filename1, 'r') as f:
    data = json.load(f)
    data['Name'] = input("Enter the value you want to update")
    func1()



filename = "Data2.json"
with open(filename, 'r') as f:
    data = json.load(f)
    data['Name'] = input("Enter the value you want to update in Data2")
    func2()

filename = "Data3.json"
with open(filename, 'r') as f:
    data = json.load(f)
    data['Name'] = input("Enter the value you want to update in Data3")
    func3()'''

