import os
import json
import shutil


Person1={
  "Name":"Denu",
  "Contact":12345678,
  "Address": "XYZ"
}
Person2={
  "Name":"Venu",
  "Contact":465735,
  "Address": "ABC"

}
Person3= {
  "Name":"Denu",
  "Contact":156946,
  "Address": "PQR"
}


'''filename = "Version.json"
with open(filename, 'r') as ver:
        new = json.load(ver)
        new['Data1'] = +1
with open('Version.json', 'w') as updated:
        json.dump(new, updated)'''

P1=json.dumps(Person1)
with open("Data1.json","w") as File:
    File.write(P1)
P2 = json.dumps(Person2)
with open("Data2.json", "w") as File:
        File.write(P2)
P3 = json.dumps(Person3)
with open("Data3.json", "w") as File:
        File.write(P3)

filename = "Data1.json"
with open(filename, 'r') as f:
    data = json.load(f)
    data['Name'] = input("Enter the value you want to update in Data1")
    with open('Data1.1.json', 'w') as updated_file:
        json.dump(data, updated_file)
        shutil.copy(filename,"old")
os.remove(filename)

filename = "Data2.json"
with open(filename, 'r') as f:
    data = json.load(f)
    data['Name'] = input("Enter the value you want to update in Data2")
    with open('Data2.1.json', 'w') as updated_file:
        json.dump(data, updated_file)
    shutil.copy(filename, "old")
os.remove(filename)

filename = "Data3.json"
with open(filename, 'r') as f:
    data = json.load(f)
    data['Name'] = input("Enter the value you want to update in Data3")
    with open('Data3.1.json', 'w') as updated_file:
        json.dump(data, updated_file)
        shutil.copy(filename, "old")
os.remove(filename)

