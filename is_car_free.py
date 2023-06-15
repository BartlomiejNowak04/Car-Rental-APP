import datetime
from car_db import CarsStatus
import json


""" do create dates to upload to database"""


def timerange(start, stop):
    dates = dict()
    for day in range(int((stop - start).days) + 1):
        temp_day = datetime.datetime.strftime(start + datetime.timedelta(day), '%Y, %m, %d')
        dates[temp_day] = True

    return dates


"""List"""


def car_reservation_list(dates, check_start, check_end):
    for day in enumerate(dates):
        if check_start == dates[day[0]][0]:
            for fal_day in range(int((check_end - check_start).days) + 1):
                if dates[day[0] + fal_day][1] is True:
                    dates[day[0] + fal_day][1] = False
                else:
                    return False

    return dates

"""Dictionary working!!!!"""


def car_reservation(dates, check_s, check_end):
    for date in dates.keys():
        if check_s == date:
            for fal_day in range(int((check_end - check_s).days) + 1):
                if dates[date + datetime.timedelta(fal_day)] is True:
                    dates[date + datetime.timedelta(fal_day)] = False
                else:
                    return False

    return dates


def good_date(dates, check_s, check_end):
    for date in dates.keys():
        if check_s == date:
            for fal_day in range(int((check_end - check_s).days) + 1):
                if dates[date + datetime.timedelta(fal_day)] is False:
                    return False
    return True



def add_good_format_data(data, car):
    converted_dict = {}
    for key, value in data.items():
        if isinstance(key, (datetime.datetime, datetime.date)):
            key_str = key.strftime('%Y, %m, %d')
            converted_dict[key_str] = value
        else:
            converted_dict[key] = value

    a.add_dates_working_backup(converted_dict, car)


def is_date_good(is_good) -> bool:
    if is_good is False:
        return False
    else:
        return True


"""to generate clear year with true"""


start_date = datetime.date(2023, 1, 1)
end_date = datetime.date(2024, 1, 1)

check_date_start = datetime.date(2023,1,5)
check_date_end = datetime.date(2023,1,10)
a = CarsStatus()
