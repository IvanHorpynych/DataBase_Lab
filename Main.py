import Engine
import GUI
import sys

class Main:

    def __init__ (self, fileProduct, fileOrder):
        self.fileProduct = fileProduct
        self.fileOrder = fileOrder

    def main(self):
        ui = GUI.GUI()
        main = Engine.Engine(self.fileProduct, self.fileOrder)
        choice = ui.menu()
        while choice != 7:
            if choice == 1:
                self.show_database(ui, main)
            elif choice == 2:
                self.show_table(ui, main)
            elif choice == 3:
                self.insert(ui, main)
            elif choice == 4:
                self.delete(ui, main)
            elif choice == 5:
                self.update(ui, main)
            elif choice == 6:
                self.select(ui, main)
            choice = ui.menu()
        main.pack()
        sys.exit(0)

    def show_database(self, ui, main):
        ui.show_table_athlete('athlete', main.get_athlete())
        ui.show_table_team('team', main.get_team())

    def show_table(self, ui, main):
        table = self.what_table(ui)
        if table == 3:
            return
        if table == 1:
            ui.show_table_athlete('athlete', main.get_athlete())
        else:
            ui.show_table_team('team', main.get_team())

    def insert(self, ui, main):
        table = self.what_table(ui)
        if table == 3:
            return
        if table == 1:
            self.insert_into_athlete(ui, main)
        else:
            self.insert_into_team(ui, main)

    def delete(self, ui, main):
        table = self.what_table(ui)
        if table == 3:
            return
        if table == 1:
            self.delete_from_athlete(ui, main)
        else:
            self.delete_from_team(ui, main)

    def update(self, ui, main):
        table = self.what_table(ui)
        if table == 3:
            return
        if table == 1:
            self.update_athlete(ui, main)
        else:
            self.update_team(ui, main)

    def select(self, ui, main):
        main.select_variant()

    def insert_into_athlete(self, ui, main):
        info = ui.insert_athlete_info()
        if not info:
            return
        if not (info[0] and info[1]and info[2]and info[3]):
            ui.error('Invalid input')
            return
        is_error = main.insert_into_athlete(info[0], info[1], info[2], info[3])
        ui.is_successful(is_error)

    def insert_into_team(self, ui, main):
        info = ui.insert_team_info()
        if not info:
            return
        if not (info[0] and info[1] and info[2]):
            ui.error('Invalid input')
            return
        is_error = main. insert_into_team(info[0], info[1], info[2].strftime("%d/%m/%y"))
        ui.is_successful(is_error)

    def delete_from_athlete(self, ui, main):
        info = ui.delete_athlete_info()
        if info:
            is_error = main.delete_from_athlete(info[0])
            ui.is_successful(is_error)

    def delete_from_team(self, ui, main):
        info = ui.delete_team_info()
        if info:
            is_error = main.delete_from_team(info[0], info[1])
            ui.is_successful(is_error)

    def update_athlete(self, ui, main):
        old_info = ui.update__info_athlete()
        if not old_info:
            ui.error('Invalid input')
            return
        existing_athlete = main.athlete_to_update(old_info[0])
        if type(existing_athlete) == str:
            ui.error(existing_athlete)
            return
        new_info = ui.update_new_info_athlete()
        if new_info:
            is_error = main.update_athlete(old_info[0], new_info[0], new_info[1], new_info[2], new_info[3])
            ui.is_successful(is_error)

    def update_team(self, ui, main):
        old_info = ui.update__info_team()
        if not (old_info and old_info[0]):
            ui.error('Invalid input')
            return
        existing_team = main.team_to_change(old_info[0])
        if type(existing_team) == str:
            ui.error(existing_team)
            return
        new_info = ui.update_new_info_team()
        if new_info:
            is_error = main.update_team(old_info[0], old_info[1], new_info[0], new_info[1], new_info[2])
            ui.is_successful(is_error)

    def what_table(self, ui):
        table = ui.what_table()
        while not table:
            table = ui.what_table()
        return table

if __name__ == '__main__':
    c = Main('athlete.txt', 'team.txt')
    c.main()