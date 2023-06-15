import tkcalendar
import datetime
import tkinter as tk
from tkinter import font
import main
import list_of_car
from is_car_free import good_date
from tkcalendar import Calendar, DateEntry

back_color = "#16161f"
for_color = "#dcdcde"
entry_back = "#111111"


class Gui:
    def __init__(self):
        self.car = None
        self.dates = []
        self.date1 = None
        self.date2 = None
        self.k = 0
        self.selected_data_label_end = None
        self.selected_data_label_first = None
        self.calendar = None
        self.cars_list = None
        self.name_entry = None
        self.surname_entry = None
        self.phone_entry = None
        self.car_entry = None
        self.dates_start_entry = None
        self.dates_end_entry = None
        self.fail_label = tk.Label()

    @staticmethod
    def clear_frame(frame):
        for widget in frame.winfo_children():
            widget.destroy()

    """AD CLIENT BUTTON"""

    def main_page(self):
        """dodać usuwanie framów"""
        main_page.tkraise()
        main_page.pack_propagate(False)
        add_client_button = tk.Button(main_page,
                                      text="ADD CLIENT",
                                      bg=back_color,
                                      foreground=for_color,
                                      font=button_font,
                                      borderwidth=0,
                                      width=15,
                                      height=3,
                                      command=lambda: self.load_add_client_page()
                                      )
        add_client_button.pack(pady=80, padx=120)

        """CHECK FOR AVAILABLE"""
        check_good_date_button = tk.Button(main_page,
                                           text="CHECK IS CAR AVAILABLE",
                                           bg=back_color,
                                           foreground=for_color,
                                           font=button_font,
                                           borderwidth=0,
                                           command=lambda: self.load_is_available()
                                           )
        check_good_date_button.pack(padx=3, pady=100)

    def load_add_client_page(self):
        """DELETING PREVIOUS FRAME"""
        self.clear_frame(main_page)
        add_client.tkraise()
        add_client.pack_propagate(False)

        """MAIN LABEL"""

        info_label = tk.Label(add_client, text="Entry data",
                              font=info_font,
                              foreground=for_color,
                              background=back_color
                              )
        info_label.grid(row=0, column=0, sticky='n', pady=20, padx=350)

        """NAME LABEL AND ENTRY"""

        name_label = tk.Label(add_client,
                              text='Name',
                              font=entry_font,
                              background=back_color,
                              foreground=for_color
                              )
        name_label.grid(row=1, column=0, pady=5)

        self.name_entry = tk.Entry(add_client,
                                   background=entry_back,
                                   foreground='white',
                                   font=entry_inside_font,
                                   borderwidth=0
                                   )
        self.name_entry.grid(row=2, column=0, pady=10)

        """SURNAME LABEL AND ENTRY"""

        surname_label = tk.Label(add_client,
                                 text='Surname',
                                 font=entry_font,
                                 background=back_color,
                                 foreground=for_color
                                 )
        surname_label.grid(row=3, column=0, pady=5)

        self.surname_entry = tk.Entry(add_client,
                                      background=entry_back,
                                      foreground='white',
                                      font=entry_inside_font,
                                      borderwidth=0
                                      )
        self.surname_entry.grid(row=4, column=0, pady=10)

        """PHONE LABEL AND ENTRY"""

        phone_label = tk.Label(add_client,
                               text='Phone',
                               font=entry_font,
                               background=back_color,
                               foreground=for_color
                               )
        phone_label.grid(row=5, column=0, pady=5)

        self.phone_entry = tk.Entry(add_client,
                                    background=entry_back,
                                    foreground='white',
                                    font=entry_inside_font,
                                    borderwidth=0
                                    )
        self.phone_entry.grid(row=6, column=0, pady=10)

        """CAR LABEL AND ENTRY"""

        car_label = tk.Label(add_client,
                             text='Car',
                             font=entry_font,
                             background=back_color,
                             foreground=for_color
                             )
        car_label.grid(row=7, column=0, pady=5)

        self.car_entry = tk.Entry(add_client,
                                  background=entry_back,
                                  foreground='white',
                                  font=entry_inside_font,
                                  borderwidth=0
                                  )
        self.car_entry.grid(row=8, column=0, pady=10)

        """DATES LABEL"""

        dates_label = tk.Label(add_client,
                               text='Dates',
                               font=entry_font,
                               background=back_color,
                               foreground=for_color
                               )
        dates_label.grid(row=9, column=0, pady=2)

        """LABELS IN THE SAME ROW START DATE AND END DATE"""

        dates_label = tk.Label(add_client,
                               text=' Start Date',
                               font=entry_font,
                               background=back_color,
                               foreground=for_color
                               )
        dates_label.grid(row=9, column=0, pady=5, padx=220, sticky='W')
        dates_label = tk.Label(add_client,
                               text='End Date',
                               font=entry_font,
                               background=back_color,
                               foreground=for_color
                               )
        dates_label.grid(row=9, column=0, pady=5, padx=220, sticky='E')

        """DATES START AND END IN THE SAME ROW """

        self.dates_start_entry = tk.Entry(add_client,
                                          background=entry_back,
                                          foreground='white',
                                          font=entry_inside_font,
                                          borderwidth=0
                                          )
        self.dates_start_entry.grid(row=10, column=0, pady=5, padx=110, sticky='W')

        self.dates_end_entry = tk.Entry(add_client,
                                        background=entry_back,
                                        foreground='white',
                                        font=entry_inside_font,
                                        borderwidth=0
                                        )
        self.dates_end_entry.grid(row=10, column=0, pady=5, padx=100, sticky='E')

        """BACK BUTTON"""

        back_button = tk.Button(add_client,
                                text="BACK",
                                bg=back_color,
                                foreground=for_color,
                                font=button_font,
                                borderwidth=0,
                                width=15,
                                height=3,
                                command=lambda: [self.main_page(), self.clear_frame(add_client)]
                                )
        back_button.grid(row=11, pady=40, padx=200, sticky='W')

        """CONFIRM BUTTON"""

        confirm_button = tk.Button(add_client,
                                   text="CONFIRM",
                                   bg=back_color,
                                   foreground=for_color,
                                   font=button_font,
                                   borderwidth=0,
                                   width=15,
                                   height=3,
                                   command=lambda: self.is_data_good()
                                   )
        confirm_button.grid(row=11, pady=40, padx=200, sticky='E')

    """CHECKING DATA"""

    def is_data_good(self):
        print(self.name_entry.get(), self.surname_entry.get(), self.phone_entry.get(),
              self.car_entry.get(), self.dates_start_entry.get(), self.dates_end_entry.get())
        print(type(self.dates_start_entry.get()), type(self.dates_end_entry.get()))

        """SPLITTING DATA TO DATETIME FORM"""

        split_start = self.dates_start_entry.get().split(',')
        data_start = datetime.date(int(split_start[0]), int(split_start[1]), int(split_start[2]))

        split_end = self.dates_end_entry.get().split(',')
        data_end = datetime.date(int(split_end[0]), int(split_end[1]), int(split_end[2]))

        """CONVERT PHONE FROM STRING TO INT"""

        phone = int(self.phone_entry.get())

        print(data_start, data_end)
        print(type(data_start), type(data_end))
        is_good = True
        try:
            main.a.add_client(self.name_entry.get(), self.surname_entry.get(), phone,
                              self.car_entry.get(), data_start, data_end)
        except ValueError:
            is_good = False

        print(is_good)
        if not is_good:
            self.fail_label = tk.Label(add_client,
                                       text='Failed. Date is reserved or client data are wrong ',
                                       font=entry_font,
                                       background=back_color,
                                       foreground=for_color
                                       )
            self.fail_label.grid(row=12, column=0, pady=5, padx=0, sticky='S')
            print(type(self.fail_label))

        else:
            self.fail_label.destroy()
            success_label = tk.Label(add_client,
                                     text='SUCCESS. Client added ',
                                     font=entry_font,
                                     background=back_color,
                                     foreground=for_color
                                     )
            success_label.grid(row=12, column=0, pady=5, padx=0, sticky='S')

    """CHECKING AVAILABILITY"""

    def load_is_available(self):
        self.clear_frame(main_page)
        is_available_car.tkraise()
        is_available_car.pack_propagate(False)

        """ENTER LABEL"""

        main_label = tk.Label(is_available_car,
                              text="ENTER CAR",
                              font=info_font,
                              foreground=for_color,
                              background=back_color
                              )
        main_label.grid(row=0, column=0, sticky='n', pady=90, padx=350)

        """LIST OF CAR"""

        self.cars_list = tk.Listbox(is_available_car,
                                    background=entry_back,
                                    foreground=for_color,
                                    borderwidth=0,
                                    font=entry_font,
                                    width=40,
                                    bd=30,
                                    relief='flat',
                                    name='listbox'
                                    )
        self.cars_list.grid(row=1, pady=0)
        for item in list_of_car.all_cars:
            self.cars_list.insert("end", item)

        select_button = tk.Button(is_available_car,
                                  text="SELECT",
                                  foreground=for_color,
                                  background=entry_back,
                                  font=button_font_big,
                                  borderwidth=0,
                                  command=lambda: [self.select(), self.load_car_calendar()]
                                  )
        select_button.grid(row=2, pady=100)

    def select(self):
        sel = self.cars_list.get('anchor')
        return sel

    def select_date(self):
        data_start_format = None
        data_end_format = None
        if self.k == 0:
            data_start = self.calendar.get_date()
            self.selected_data_label_first['text'] = data_start
            self.k += 1
        elif self.k == 1:
            data_end = self.calendar.get_date()
            self.selected_data_label_end['text'] = data_end
            self.k = 0

    def load_car_calendar(self):
        car_calendar.tkraise()
        car_calendar.pack_propagate(False)

        """MAIN LABEL CAR NAME"""
        self.car = self.select()
        main_label = tk.Label(car_calendar,
                              text=self.select(),
                              font=info_font,
                              foreground=for_color,
                              background=back_color
                              )
        """Because before clearing frame we have to give data from self.select(): car name we want to show"""
        self.clear_frame(is_available_car)
        main_label.grid(row=0, column=0, sticky='n', pady=90, padx=350)

        """CALENDAR"""
        self.calendar = Calendar(car_calendar,
                                 font=entry_font,
                                 borderwidth=0,
                                 selectmode='day',
                                 background="black",
                                 disabledbackground="black",
                                 bordercolor="black",
                                 headersbackground="black",
                                 normalbackground="black",  # tooooo
                                 weekendbackground='black',
                                 foreground='white',
                                 normalforeground='white',
                                 headersforeground='white'
                                 )

        self.calendar.grid(row=1, column=0, sticky='s', pady=10, padx=350, )
        # tk.Canvas.itemconfig(calendar.selection_get(), bacground='red')
        # for item in main.cars.pick_dates(car):
        #     bool_car = main.cars.pick_dates(car)[item]
        #     if not bool_car:
        # tutaj sprawdzać, czy true or false i zmieniać kolor w kalenarzu
        #

        # calendar.config(calendar.get_date(), disableddaybackground='red')
        """First option
        button and two labels with selected dates
        for loop to check from dates from db
        if every dates is true then third label = True"""
        select_date_button = tk.Button(car_calendar,
                                       text="Select data",
                                       font=button_font,
                                       foreground=for_color,
                                       background=back_color,
                                       borderwidth=0,
                                       command=lambda: [self.select_date(), self.on_button_click()]

                                       )
        select_date_button.grid(row=2)
        self.selected_data_label_first = tk.Label(car_calendar,
                                                  text='',
                                                  font=info_font,
                                                  background=back_color,
                                                  foreground=for_color,
                                                  )
        self.selected_data_label_first.grid(row=3, sticky='w', pady=10, padx=300)

        self.selected_data_label_end = tk.Label(car_calendar,
                                                text='',
                                                font=info_font,
                                                background=back_color,
                                                foreground=for_color,
                                                )
        self.selected_data_label_end.grid(row=3, sticky='e', pady=10, padx=300)

        # confirm_button = tk.Button(car_calendar,
        #                            text="CONFIRM",
        #                            font=button_font,
        #                            foreground=for_color,
        #                            background=back_color,
        #                            borderwidth=0,
        #                            border=0,
        #                            # command=self. check_dates()
        #                            )
        # confirm_button.grid(row=4, sticky='n', pady=10, padx=300)

    def on_button_click(self):
        date = self.calendar.get_date()
        if self.date1 is None:
            self.date1 = date
        elif self.date2 is None:
            self.date2 = date

        sp = self.date1.split('/')
        sp[2] = 2000 + int(sp[2])
        data_start_format = datetime.date(int(sp[2]), int(sp[0]), int(sp[1]))
        data_start_format.strftime("%Y, %m, %d")

        sp = self.date2.split('/')
        sp[2] = 2000 + int(sp[2])
        data_end_format = datetime.date(int(sp[2]), int(sp[0]), int(sp[1]))
        data_end_format.strftime("%Y, %m, %d")
        print(self.car, data_start_format, data_end_format, main.cars.pick_dates(self.car))
        great_date = good_date(main.cars.pick_dates(self.car), data_start_format, data_end_format)
        print(great_date)
        if great_date:
            yes_label = tk.Label(car_calendar,
                                 text="Car is free",
                                 font=info_font,
                                 foreground=for_color,
                                 background=back_color
                                 )
            yes_label.grid(row=4, sticky='n', pady=10, padx=300)
        else:
            no_label = tk.Label(car_calendar,
                                text="Car is reserved",
                                font=info_font,
                                foreground=for_color,
                                background=back_color
                                )
            no_label.grid(row=4, sticky='n', pady=10, padx=300)

        exit_button = tk.Button(car_calendar,
                                text="EXIT",
                                font=button_font,
                                foreground=for_color,
                                background=back_color,
                                borderwidth=0,
                                border=0,
                                command=lambda:[self.clear_frame(car_calendar), exit()]
                                )
        exit_button.grid(row=5, sticky='n', pady=10, padx=300)

        """Second option
        tkink how to change color of single dateframe
        for loop with false and true
        print to red reserved dates"""


root = tk.Tk()
root.title("RENTAL")
root.eval("tk::PlaceWindow . center")

"""FONTS"""

button_font = font.Font(
    family='Courier',
    size=10,
    weight='bold',
    slant='roman',
    underline=False,
    overstrike=False,
)
button_font_big = font.Font(
    family='Courier',
    size=30,
    weight='bold',
    slant='roman',
    underline=False,
    overstrike=False,
)
info_font = font.Font(
    family='Courier',
    size=32,
    weight='bold',
    slant='roman',
    underline=False,
    overstrike=False,
)

entry_font = font.Font(
    family='Courier',
    size=10,
    weight='bold',
    slant='roman',
    underline=False,
    overstrike=False,
)
entry_inside_font = font.Font(
    family='Courier',
    size=20,
    weight='bold',
    slant='roman',
    underline=False,
    overstrike=False,
)

"""Frame main_page """
main_page = tk.Frame(root, width=900, height=700, bg=back_color)
main_page.grid(row=0, column=0)

"""Frame add_client"""
add_client = tk.Frame(root, width=900, height=700, bg=back_color)
add_client.grid(row=0, column=0, sticky="nesw")

"""Frame check_car"""
is_available_car = tk.Frame(root, width=900, height=700, bg=back_color)
is_available_car.grid(row=0, column=0, sticky='nesw')

"""CAR CALENDAR"""
car_calendar = tk.Frame(root, width=900, height=700, background=back_color)
car_calendar.grid(row=0, column=0, sticky='nesw')

"""STARTING APP"""
start = Gui()
start.main_page()

"""run app"""
root.mainloop()
