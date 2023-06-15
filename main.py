from basedb import Base
import list_of_car
import datetime
import is_car_free
import car_db

"""day.now trzeba dodać, żeby jak mija ten okres to zeny sie tabela updatowala, labo wyskakiwało powiadomienie"""


class Rental:
    def __init__(self):
        self.data_base = Base()

    def add_client(self, name, surname, phone, car, start, stop):
        self.data_base.data(name, surname, phone)
        if list_of_car.is_available_car(car):
            if is_car_free.is_date_good(is_car_free.car_reservation(cars.pick_dates(car), start, stop)):
                self.data_base.car_data(car, start, stop)
                self.data_base.add_to_table_data()
                is_car_free.add_good_format_data(is_car_free.car_reservation(cars.pick_dates(car), start, stop), car)

                return "CAR ADDED"
            else:
                raise ValueError('Car is used or is not exist in list')
        else:
            raise ValueError('Car is used or is not exist in list')


cars = car_db.CarsStatus()
a = Rental()
start = datetime.date(2023, 1, 1)
stop = datetime.date(2023, 1, 10)

# print(a.add_client(name='kacper', surname='g', phone=123456789,
                   # car='2022 Skoda Fabia', start=start, stop=stop))


