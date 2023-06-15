import datetime
import sqlite3
import list_of_car
import json


class CarsStatus:
    def __init__(self):
        self.db = sqlite3.connect("Cars_status.db")
        self.cursor = self.db.cursor()
        self.info_dates_base = None
        self.car = None

    def create_table(self):
        self.cursor.execute('''
               CREATE TABLE Cars_status(
               id integer  PRIMARY KEY AUTOINCREMENT, 
               name string,
               dates string)
               ''')
        self.db.commit()
        self.db.close()

    def add_cars(self, cars):
        car = ""
        for car in cars:
            self.cursor.execute(f' INSERT INTO Cars_status (name)'
                                f"VALUES ('{car}')")
            self.db.commit()

    def add_dates(self, dates, car):
        for i in range(0, len(list_of_car.all_cars)+1):
            self.cursor.execute(f" UPDATE Cars_status SET dates = '{dates}' WHERE name = '{car}'")
            self.db.commit()

    def add_dates_working_backup(self, dates, car):
        for i in range(0, len(list_of_car.all_cars)+1):
            self.cursor.execute(f" UPDATE Cars_status SET dates = '{json.dumps(dates)}' WHERE name = '{car}'")
            self.db.commit()

    def add_dates_(self, dates, car):
        for i in range(0, len(list_of_car.all_cars)+1):
            self.cursor.execute(f" UPDATE Cars_status SET dates ='{dates}' "
                                f" WHERE name = '{car}'")
            self.db.commit()

    def pick_dates(self, car):
        self.car = car
        self.cursor.execute(f" SELECT dates FROM Cars_status WHERE name = '{car}'")
        tes = self.cursor.fetchone()
        self.info_dates_base = json.loads(tes[0])

        keys_to_change = list(self.info_dates_base.keys())
        for old_key in keys_to_change:
            x = old_key.split(',')
            new_key = datetime.date(int(x[0]), int(x[1]), int(x[2]))
            self.info_dates_base[new_key] = self.info_dates_base.pop(old_key)

        return self.info_dates_base






