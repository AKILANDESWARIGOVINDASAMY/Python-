import json
import glob
import os
import shutil
from os.path import splitext


class create():
       def create_files(self):
           person_dict = input("Enter the values to create file")
           with open('person.json', 'w') as json_file:
                json.dump(person_dict, json_file)

       def list_files(self):
           files = glob.glob('*.json')
           print("List of files", files)

class modify:
    def modify_files(self):
      try:
        filename = "Version.json"
        with open(filename, 'r') as ver:
            new = json.load(ver)
            e=new['Data1']
            new['Data1']=e+1
        with open('Version.json', 'w') as updated:
            json.dump(new, updated)
        modifyfile = input("Filename to modify")
        x = splitext(modifyfile)
        with open(modifyfile, 'r') as f:
            data = json.load(f)
            data = input("Enter the value you want to update")
        with open("%s.%d.json" % (x[0], new['Data1']), 'w') as updated:
            json.dump(data, updated)
      except:
          print("No operation")


class move():

        def move_files(self):
            filename=input("Filename want to move")
            try:
                shutil.move(filename, "old")
            except:
                print("NIL")




class delete():
    def delete_files(self):
        filename = input("Filename want to delete")
        try:
            os.remove(filename)
        except:
            print("NIL")

class recall():
    def recall_files(self):
        filename=input("Filename want to recall")
        os.chdir("C:\\Users\\Akila\\AppData\\Roaming\\JetBrains\\PyCharmCE2020.1\\scratches\\Old")
        try:
            shutil.move(filename, "C:\\Users\\Akila\\AppData\\Roaming\\JetBrains\\PyCharmCE2020.1\\scratches")
        except:
            print("No operation")



