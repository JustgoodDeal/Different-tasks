import uuid
from datetime import date
from random import randint

class Match:
    def __init__(self, team1, team2, result = None, date = date(randint(2018,2019),randint(1,12),randint(1,28)), location = None, id = uuid.uuid4()): 
        self.team1 = team1
        self.team2 = team2
        self.match_name = team1.team_name + '_' + team2.team_name
        self.result = result
        self.date = date
        self.location = location
        self.id = id
        self.match_players = dict()                         # Только те игроки из 2-х команд, которые принимали участие в матче
    def __call__(self, *match_players):
        for i in match_players:
            if i in self.team1.team_players.values() or i in self.team2.team_players.values():    # Чтобы нельзя было добавлять игроков из клубов,
                                                                                                  # не участвующих в матче                
                self.match_players[i.player_name + ' ' + i.player_surname] = i
                i.matches_played[self.match_name] = self
                self.team1.matches[self.match_name] = self
                self.team2.matches[self.match_name] = self
        
class Team:
    def __init__(self, team_name, id = uuid.uuid4()):
        self.team_name = team_name
        self.id = id
        self.team_players = dict()                  # Игроки команды
        self.matches = dict()                       # Матчи, в которых принимала участие команда
    def __call__(self, *players):
        for i in players:
            if i.player_team:                       # Добавляем команде игрока, а игроку - команду. Также удаляем игрока из бывшей команды
                del i.player_team.team_players[i.player_name + ' ' + i.player_surname]
            self.team_players[i.player_name + ' ' + i.player_surname] = i
            i.player_team = self

class Player:
    def __init__(self, player_name, player_surname, id = uuid.uuid4(), player_team = None):
        self.player_name = player_name
        self.player_surname = player_surname
        self.player_team = player_team
        self.id = id
        self.matches_played = dict()                    # Матчи, в которых игрок принимал участие
    def __call__(self, player_team):
        if self.player_team:                            # Добавляем игроку команду, а команде - игрока. Также удаляем игрока из бывшей команды 
            del self.player_team.team_players[self.player_name + ' ' + self.player_surname]
        self.player_team = player_team
        player_team.team_players[self.player_name + ' ' + self.player_surname] = self
    def add_matches (self, *matches):   
        for i in matches:
            if self in i.team1.team_players.values() or self in i.team2.team_players.values():      # Чтобы нельзя было добавлять матчи игрокам из тех
                                                                                                    # команд, которые не участвуют в матче
                    self.matches_played[i.match_name] = i 
                    i.match_players[self.player_name + ' ' + self.player_surname] = self

def matches_search_on_date(date1, date2, **kwargs):
    for v in kwargs.values():
        if date1 <= v.date <= date2:
            print(str(v.date) + ' ' + v.team1.team_name + ' - ' + v.team2.team_name,v.result.replace('_',':')+'\n')
            #for i in v.match_players.keys():
            for k,v in sorted(v.match_players.items(),key=lambda kv:kv[0]):
                print(k)
            print()

def save_to_file(file,vse_komandi,vse_matchi):
    with open (file,'w') as file:
        for k,v in sorted(vse_komandi.items(),key=lambda kv:kv[0]):
            file.write('{} id:{}\n\n'.format(k,v.id))
            for k,v in sorted(v.team_players.items(),key=lambda kv:kv[0]):
                file.write('{} id:{}\n'.format(k,v.id))
            file.write('\n')
        for i in vse_matchi.values():
            file.write('\n{} {} - {} {} {} id:{}\n\n'.format(i.date,i.team1.team_name,i.team2.team_name,i.result.replace('_',':'),i.location,i.id))
            for k,v in sorted(i.match_players.items(),key=lambda kv:kv[0]):
                file.write(v.player_name + ' ' + v.player_surname + '\n')