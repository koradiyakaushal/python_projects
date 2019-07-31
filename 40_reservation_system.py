class Reservation:

    def __init__(self, booking_class, date):
        self.booking_class = booking_class
        self.date = date

    def is_available(self, booking_class):
        return self.get_items(booking_class) > 0

    def make_reservation(self, booking_class, days):
        if self.is_available(booking_class):
            self.decrement_items(booking_class)
            self.get_price(booking_class)
        else:
            print("waiting time is: ", )

    def get_class_name(self):
        return self.__class__.__name__

    def get_items(self, booking_class):
        raise NotImplementedError

    def get_price(self, booking_class):
        raise NotImplementedError

    def decrement_items(self, booking_class):
        raise NotImplementedError

    def get_id_prefix(self):
        raise NotImplementedError
    #
    # def get_waiting_time(self):
    #     raise NotImplementedError


class Airline(Reservation):
    CLASS_BUSINESS = 'Business Class'
    CLASS_FIRST = 'First Class'
    CLASS_PREMIUM_ECONOMY = 'Premium Economy'
    CLASS_ECONOMY = 'Regular Economy'

    def __init__(self, airline_name, booking_class, date):

        # super(Airline, self).__init__()
        super(Airline, self).__init__(booking_class, date)
        self.date = date
        self.airline_name = airline_name
        self.seats = {
            self.CLASS_BUSINESS: 50,
            self.CLASS_FIRST: 50,
            self.CLASS_PREMIUM_ECONOMY: 100,
            self.CLASS_ECONOMY: 150,
        }
        self.prices = {
            self.CLASS_BUSINESS: 2500,
            self.CLASS_FIRST: 2000,
            self.CLASS_PREMIUM_ECONOMY: 1800,
            self.CLASS_ECONOMY: 1500,
        }

    def get_items(self, booking_class):
        # print(self.seats)
        return self.seats[booking_class]

    def decrement_items(self, booking_class):
        self.seats[booking_class] -= 1

    def get_id_prefix(self):
        return 'AIR'

    def get_price(self, booking_class):
        return self.prices[booking_class]

    # def get_waiting_time(self):
    #     return self.date


class Hotel(Reservation):
    CLASS_BUSINESS = 'Business Room'
    CLASS_FIRST = 'First Class Room'
    CLASS_PREMIUM_ECONOMY = 'Premium Economy Room'
    CLASS_ECONOMY = 'Regular Economy Room'

    def __init__(self, hotel_name, booking_class, date):

        # super(Airline, self).__init__()
        super(Hotel, self).__init__(booking_class, date)
        self.date = date
        self.hotel_name = hotel_name
        self.seats = {
            self.CLASS_BUSINESS: 50,
            self.CLASS_FIRST: 50,
            self.CLASS_PREMIUM_ECONOMY: 100,
            self.CLASS_ECONOMY: 150,
        }
        self.prices = {
            self.CLASS_BUSINESS: 2500,
            self.CLASS_FIRST: 2000,
            self.CLASS_PREMIUM_ECONOMY: 1800,
            self.CLASS_ECONOMY: 1500,
        }

    def get_items(self, booking_class):
        # print(self.seats)
        return self.seats[booking_class]

    def decrement_items(self, booking_class):
        self.seats[booking_class] -= 1

    def get_id_prefix(self):
        return 'Hotel'

    def get_price(self, booking_class):
        return self.prices[booking_class]

    # def get_waiting_time(self):
    #     return self.date


a = Airline('Air Force', 'Business Class', 50)
h = Hotel('Taj', 'Business Room', 25)
a.get_items('Business Class')
c = a.get_price('Business Class')
print(c)
a.make_reservation('Business Class', 50)
# print(a.seats)
h.make_reservation('Business Room', 50)
print(h.get_price('Business Room'))

