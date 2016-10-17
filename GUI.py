import datetime


class GUI:
    def menu(self):
        print '\n[1] Display database'
        print '[2] Display table'
        print '[3] Insert row'
        print '[4] Delete row'
        print '[5] Update the row'
        print '[6] Select best athletes'
        print '[7] Quit'
        try:
            selection = int(raw_input('Choose an option: '))
            if not 1 <= selection <= 7:
                raise ValueError
            return selection
        except ValueError:
            self.error('Invalid input')
            return None

    def show_table_team(self, table_name, table):
        print '{:^10}'.format(table_name + ' table')
        if not table:
            print '{:^10}'.format('empty')
        else:
            columns = table[0].keys()
            print '|{:^30}|{:^30}|{:^30}|{:^30}|'.format(columns[1] ,columns[3], columns[0], columns[2])
            print '-' * 125
            for row in table:
                print '|{:^30}|{:^30}|{:^30}|{:^30}|'.format(row[columns[1]], row[columns[3]], row[columns[0]], row[columns[2]])
            print '-' * 125
    def show_table_athlete(self, table_name, table):
        print '{:^10}'.format(table_name + ' table')
        if not table:
            print '{:^10}'.format('empty')
        else:
            columns = table[0].keys()
            print '|{:^30}|{:^30}|{:^30}|{:^30}|{:^30}|'.format(columns[4], columns[3], columns[2], columns[0],columns[1])
            print '-' * 156
            for row in table:
                print '|{:^30}|{:^30}|{:^30}|{:^30}|{:^30}|'.format(row[columns[4]], row[columns[3]], row[columns[2]], row[columns[0]], row[columns[1]])
            print '-' * 156

    def delete_athlete_info(self):
        row = list()
        print '\nDeleting athlete'
        athlete_id = int(raw_input("Enter athlete_id: "))
        row.append(athlete_id)
        return row

    def delete_team_info(self):
        row = list()
        print '\nDeleting team'
        try:
            row.append(raw_input("Enter team_name: "))
            row.append(raw_input("Enter kind_of_sport: "))
            return row
        except ValueError:
            self.error('Invalid input')
            return None

    def insert_athlete_info(self):
        row = list()
        print '\nInserting athlete'
        try:
            row.append(raw_input("Enter athlete_name: "))
            row.append(raw_input('Enter age: '))
            row.append(raw_input('Enter medal: '))
            row.append(int(raw_input('Enter team_id: ')))
            return row
        except ValueError:
            self.error('Invalid input')
            return None

    def insert_team_info(self):
        row = list()
        print '\nInserting team'
        try:
            row.append(raw_input("Enter team_name: "))
            row.append(raw_input("Enter kind of sport: "))
            date_str = raw_input("Enter found date (dd/mm/yy): ")
            if not date_str:
                raise ValueError
            row.append(datetime.datetime.strptime(date_str, "%d/%m/%y").date())
            return row
        except ValueError:
            self.error('Invalid input')
            return None

    def update__info_athlete(self):
        row = list()
        print '\nUpdating athlete'
        row.append(int(raw_input("Enter athlete_id to update: ")))
        return row

    def update__info_team(self):
        row = list()
        print '\nUpdating team'
        try:
            row.append(int(raw_input("Enter team_id to update: ")))
            return row
        except ValueError:
            self.error('Invalid input')
            return None

    def update_new_info_athlete(self):
        row = list()
        try:
            row.append(raw_input("Enter new athlete_name (press Enter if you don't want to update this attribute): "))
            row.append(int(raw_input("Enter new age (press '0' if you don't want to update this attribute): ")))
            row.append(int(raw_input("Enter new medal (press '0' if you don't want to update this attribute): ")))
            row.append(int(raw_input("Enter new team (press '0' if you don't want to update this attribute): ")))
            return row
        except ValueError:
            self.error('Invalid input')
            return None

    def update_new_info_team(self):
        row = list()
        try:
            row.append(raw_input("Enter new team_name (press Enter if you don't want to update this attribute): "))
            row.append(raw_input("Enter new kind_of_sport (press Enter if you don't want to update this attribute): "))
            date_str = raw_input(
                "Enter new found date (dd/mm/yy) (press Enter if you don't want to update this attribute): ")
            if not date_str:
                row.append(date_str)
            else:
                row.append(datetime.datetime.strptime(date_str, "%d/%m/%y").date())
            return row
        except ValueError:
            self.error('Invalid input')
            return None

    def is_successful(self, error_message):
        if not error_message:
            print '\nSuccess'
        else:
            self.error(error_message)

    def what_table(self):
        print '\nChoose the table: '
        print '[1] athlete'
        print '[2] team'
        print '[3] Back to menu'
        try:
            selection = int(raw_input('Choose an option: '))
            if not 1 <= selection <= 3:
                raise ValueError
            return selection
        except ValueError:
            self.error('Invalid input')
            return None

    def error(self, message):
        print '\n'+message