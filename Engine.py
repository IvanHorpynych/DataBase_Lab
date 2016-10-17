import pickle

class Engine:

    def __init__(self, fileteam, fileAthlete):
        try:
            self.fileteam = fileteam
            self.fileAthlete = fileAthlete
            DB = open(fileteam, 'rb')
            self.athlete = pickle.load(DB)
            DB.close()
            DB = open(fileAthlete, 'rb')
            self.team = pickle.load(DB)
            DB.close()
        except:
            self.athlete = list()
            self.team = list()

    def get_athlete(self):
        return self.athlete

    def get_team(self):
        return self.team

    def insert_into_athlete(self, athlete_name, age, medal, team_id):
        if not self.team_id_in_table(team_id):
            return 'No such team'
        if not self.athlete:
            athlete_id = 1
        else:
            athlete_id = len(self.athlete)+1
        if self.athlete_name_in_table(athlete_name):
            return 'Such athlete already exists'
        self.athlete.append({'athlete_id': athlete_id, 'athlete_name': athlete_name, 'age': age, 'medal': medal, 'team_id': team_id})

    def insert_into_team(self, team,kind_of_sport, found_date):

        if self.team_name_in_table(team):
            return 'Such team already exists'
        if not self.team:
            team_id = 1
        else:
            team_id = len(self.team)+1
        self.team.append({'team_id': team_id, 'team_name': team, 'kind_of_sport': kind_of_sport, 'date_of_found': found_date})

    def delete_from_athlete (self, athlete_id):
        existing_athlete = self.athlete_id_in_table(athlete_id)
        if not existing_athlete:
            return 'No such athlete'
        self.athlete.remove(existing_athlete[0])

    def delete_from_team (self, team_id, kind_of_sport):
        if filter(lambda x: x['team_id'] == team_id, self.athlete):
            return 'Cannot delete an team'
        team = self.team_to_change(team_id)
        '''
        if type(team) == str:
            return team
            '''
        self.team.remove(team)

    def athlete_to_update(self, athlete_id):
        existing_athlete = self.athlete_id_in_table(athlete_id)
        if not existing_athlete:
            return 'No such athlete'

    def update_athlete(self, athlete_id, new_athlete_name, new_age, new_medal, new_team):

        existing_athlete = self.athlete_id_in_table(athlete_id)
        if new_athlete_name:
            existing_athlete[0]['athlete_name'] = new_athlete_name
        if new_age:
            existing_athlete[0]['age'] = new_age
        if new_medal:
            existing_athlete[0]['medal'] = new_medal
        if filter(lambda x: x['team_id'] == new_team, self.athlete):
            existing_athlete[0]['team_id'] = new_team
        else: return 'No such team'

    def team_to_change(self, team_id):
        existing_team = self.team_id_in_table(team_id)
        if not existing_team:
            return 'No such team'
        if filter(lambda x: x['team_id'] == team_id, self.athlete):
            return 'Cannot update an team'
        return existing_team[0]

    def update_team(self, team, kind_of_sport, new_team, new_kind, new_found):
        if new_team and new_kind and self.team_in_table(new_team, new_kind):
            return 'Such team already exists'
        existing_team = self.team_in_table(team, kind_of_sport)
        if new_team:
            existing_team[0]['team_name'] = new_team
        if new_kind:
           existing_team[0]['kind_of_sport'] = new_kind
        if new_found:
            existing_team[0]['date_of_found'] = new_found.strftime("%d/%m/%y")

    def select_variant(self):
        best_player = dict()
        for player in self.athlete:
            if player['team_id'] in best_player.keys():
                if player['medal'] > best_player[player['team_id']]['medal']:
                    best_player[player['team_id']] = player
            else:
                best_player[player['team_id']] = player
        for team in best_player.keys():
            print 'Team:', team, 'Name: ', best_player[team]['athlete_name']


    def pack(self):
        DB = open(self.fileteam, 'wb')
        pickle.dump(self.athlete, DB)
        DB.close()
        DB = open(self.fileAthlete, 'wb')
        pickle.dump(self.team, DB)
        DB.close()

    def team_name_in_table(self, team_name):
        return filter(lambda x: x['team_name'] == team_name, self.team)

    def athlete_name_in_table(self, athlete_name):
        return filter(lambda x: x['athlete_name'] == athlete_name, self.athlete)

    def athlete_id_in_table(self, athlete_id):
        return filter(lambda x: x['athlete_id'] == athlete_id, self.athlete)

    def team_in_table(self,team, kind_of_sport):
        return filter(lambda x: x['team_name'] == team and x['kind_of_sport'] == kind_of_sport, self.team)

    def team_id_in_table(self,team_id):
        return filter(lambda x: x['team_id'] == team_id, self.team)