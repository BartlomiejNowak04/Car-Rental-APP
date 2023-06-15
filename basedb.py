import sqlite3
import datetime


class Base:
    def __init__(self):
        self.good_format_end = None
        self.good_format_start = None
        self.db = sqlite3.connect("Rental_cars.db")
        self.cursor = self.db.cursor()

        self.name = None
        self.surname = None
        self.phone = None

        self.car_rented = None
        self.begin_date = None
        self.end_data = None

    def create_data_base(self):
        self.cursor.execute('''
        CREATE TABLE Cars(
        id integer  PRIMARY KEY AUTOINCREMENT, 
        name_borrower string,
        surname_borrower string,
        phone_number integer,
        car_rented string,
        begin_date string,
        end_date string)
        ''')
        self.db.commit()
        self.db.close()

    def data(self, name, surname, phone):
        len_phone = []
        self.name = name
        self.surname = surname
        self.phone = phone
        is_correct = self.phone
        while is_correct > 1:
            len_phone.append(int(self.phone % 10))
            is_correct /= 10
        if len(len_phone) != 9:
            raise "Phone number too short or too long"

    def car_data(self, car, start, stop):
        self.car_rented = car
        self.begin_date = start
        self.end_data = stop

    def add_to_table_data(self):
        print(self.checking_good_date())
        if self.checking_good_date():
            self.cursor.execute(f' INSERT INTO Cars (name_borrower, surname_borrower, phone_number,'
                                f' car_rented, begin_date, end_date  )'
                                f"VALUES ('{self.name}', '{self.surname}', '{self.phone}',"
                                f"'{self.car_rented}', '{self.begin_date}', '{self.end_data}')")
            self.db.commit()
        else:
            print("bad data")

    def update_table(self, ids, column, value, ):
        self.cursor.execute(f" UPDATE Cars SET {column}  =  '{value}' WHERE id = {ids} ")
        self.db.commit()

    def deleting_client(self, ids):
        self.cursor.execute(f" DELETE FROM Cars WHERE id = {ids}")
        self.db.commit()

    def checking_good_date(self):
        """if data is not datatime object"""
        # try:
        #     date_begin = self.begin_date.split(',')
        # except ValueError:
        #     date_begin = self.begin_date.split(' ')
        # start_date = datetime.datetime(int(date_begin[0]), int(date_begin[1]), int(date_begin[2]))
        # start_date.strftime('%Y, %m ,%d')

        # try:
        #     date_end = self.end_data.split(',')
        # except ValueError:
        #     date_end = self.end_data.split(' ')
        # date_end = datetime.datetime(int(date_end[0]), int(date_end[1]), int(date_end[2]))
        # date_end.strftime('%d %m %Y')
        # self.good_format_start = date_begin
        # self.good_format_end = date_end

        # if start_date > date_end:
        #     print("Invalid date: first date is greater than second")
        #     return False
        # else:
        #     return True

        if self.begin_date > self.end_data:
            print("Invalid date: first date is greater than second")
            return False
        else:
            return True





