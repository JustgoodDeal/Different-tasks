import Classes_for_Task0  
from datetime import date

with open ("/home/ben/Документы/Python_Developer/HomeWork/Class 13/Files/Team+players_read.txt",'r') as file:   # Считываем из 1-го файла игроков
    file.readline()                                                                                           # и команды и добавляем их в классы
    file.readline()
    data = file.readline().split()
    vse_igroki = dict()
    vse_komandi = dict()
    while data:
        igrok = Classes_for_Task0.Player(data[0],data[1],data[2])
        vse_igroki[data[0] + ' ' + data[1]] = igrok
        if data[3] not in vse_komandi:
            instance_name = Classes_for_Task0.Team(data[3],data[4])
            instance_name(igrok)
            vse_komandi[data[3]] = instance_name
        else:
            vse_komandi[data[3]](igrok)
        data = file.readline().split()

with open ("/home/ben/Документы/Python_Developer/HomeWork/Class 13/Files/Match_read.txt",'r') as file:      # Считываем из 2-го файла матчи
    file.readline()                                                                                         # и добавляем их в классы
    file.readline()
    data = file.readline().split()
    vse_matchi = dict()
    while data:
        chislo = [int (i) for i in data[3].split('.')]
        instance_name = Classes_for_Task0.Match(vse_komandi[data[0]], vse_komandi[data[1]], data[2], date(chislo[0],chislo[1],chislo[2]), data[4], data[5])
        vse_matchi[instance_name.match_name] =  instance_name
        data = file.readline().split(',')
        if '\n' in data[-1]:
            data[-1] = data[-1].replace('\n','')
        for i in data:
            if i in instance_name.team1.team_players or instance_name.team2.team_players:       
                instance_name(vse_igroki[i])
        data = file.readline().split()


date1 = date(*[int (i) for i in input('Set a start date:\n').split()])
date2 = date(*[int (i) for i in input('Set the end date:\n').split()])
file = "/home/ben/Документы/Python_Developer/HomeWork/Class 13/Files/Football_championship.txt"
Classes_for_Task0.matches_search_on_date(date1, date2, **vse_matchi)
Classes_for_Task0.save_to_file(file,vse_komandi,vse_matchi)