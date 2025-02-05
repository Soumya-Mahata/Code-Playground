from random import randint

class Train:
    def __init__(self, train_no):
        self.train_no = train_no
    def tickit_booking(self, start, stop):
        print(f'Tickit is booked: \nTrain no: {self.train_no} \nFrom: {start} \nTo: {stop}')
    def get_fare(self, start, stop):
        print(f'Tickit fair is: {randint(100, 500)} \nTrain no: {self.train_no} \nFrom: {start} \nTo: {stop}')
    def get_status(self):
        print(f'Train no {self.train_no} is running on time.')

t = Train(12345)
t.tickit_booking('Adra', 'Dhanbad')
t.get_fare('Adra', 'Dhanbad')
t.get_status()