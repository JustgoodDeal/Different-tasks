import json

class Baza:
    def __init__(self, Number, Name,Surname,Sex,Age):
        self.Number = Number
        self.Name = Name
        self.Surname = Surname
        self.Sex = Sex
        self.Age = Age

    @classmethod
    def open_txt (cls):
        with open("/home/ben/Документы/Python_Developer/HomeWork/Class 11/Files/File_for_Task1.txt",'r') as file:
            all_instanses = cls.create_instanses_txt(file)
        return all_instanses

    @classmethod
    def open_json (cls):
        with open("/home/ben/Документы/Python_Developer/HomeWork/Class 11/Files/File_for_Task1.json",'r') as file:
            all_instanses = cls.create_instanses_json(file)
        return all_instanses

    @classmethod
    def create_instanses_txt(cls,file):
        info = file.readline()
        count = 0
        all_instanses = []
        while info:
            count +=1
            person = info.split()
            info = file.readline()
            instance_name = Baza(count, person[0],person[1],person[2],int(person[3]))
            all_instanses.append(instance_name)
        return all_instanses
    
    @classmethod
    def create_instanses_json(cls,file):
        people = json.load(file)
        count = 0
        all_instanses = []
        for i in people:
            count +=1
            instance_name = Baza(count, i['Name'],i['Surname'],i['Sex'],int(i['Age']))
            all_instanses.append(instance_name)    
        return all_instanses

    @classmethod
    def search_for_men(cls,all_instanses, parametr2):
        to_print = []
        for i in all_instanses:
            if i.Sex == 'male':        
                to_print.append ([i.Number,i.Name,i.Surname])
        if parametr2 == 'json':
            cls.write_to_json(to_print)
        elif parametr2 == 'txt':
            cls.write_to_txt(to_print)
        return to_print

    @classmethod
    def write_to_json (cls, men):
        result_dict = dict()
        for i in range (len(men)):
            result_dict[men[i][0]] = [men[i][1], men[i][2]]
        with open("/home/ben/Документы/Python_Developer/HomeWork/Class 11/Files/File_for_Task1(result).json",'w') as file:
            json.dump(result_dict,file)

    @classmethod
    def write_to_txt (cls, men):
        with open("/home/ben/Документы/Python_Developer/HomeWork/Class 11/Files/File_for_Task1(result).txt",'w') as file:
            for i in men:
                file.write(' '.join([str(j) for j in i])+'\n')