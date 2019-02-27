import hashlib

class File:
    def __init__(self, files):
        self.files = files
    def calc(self):
        with open("/home/ben/Документы/Python_Developer/HomeWork/Class 14/Manifest.txt", 'w') as mani:
            for i in self.files:
                with open(i, 'r') as file:
                    data = file.read()
                    hash = hashlib.md5(data.encode('utf-8')).hexdigest()
                mani.write(i + ' : ' + hash + '\n')

class Manifest:
    def __init__(self, manifest):
        self.manifest = manifest
    def check(self):
        with open(self.manifest, 'r') as mani:
            data = mani.readline().split(' : ')
            while len(data)>1:
                if '\n' in data[-1]:
                    data[-1] = data[-1].replace('\n','')
                with open(data[0], 'r') as file:
                    mani2 = file.read()
                    hash = hashlib.md5(mani2.encode('utf-8')).hexdigest()
                if hash == data[1]:
                    print(data[0],'Ok')
                else:
                    print(data[0],'Failed')
                data = mani.readline().split(' : ')

ins = File(["/home/ben/Документы/Python_Developer/HomeWork/Class 2/Task3.py","/home/ben/Документы/Python_Developer/HomeWork/Class 2/Task4.py"])
ins2 = Manifest("/home/ben/Документы/Python_Developer/HomeWork/Class 14/Manifest.txt")
ins.calc()
ins2.check()