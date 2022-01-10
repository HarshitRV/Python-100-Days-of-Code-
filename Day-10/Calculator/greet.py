import datetime

class Greet:
    def __init__(self, name):
        self.name = name
        self.time_ = datetime.datetime.now()
        self.greet()

    def greet(self):
        if int(self.time_.strftime("%H")) > 00 and int(self.time_.strftime("%H")) < 12:
            print(f"Good Morning {self.name}. Let's start calculating !\n")
        elif int(self.time_.strftime("%H")) > 12 and int(self.time_.strftime("%H")) < 16:
            print(f"Good Afternoon {self.name}. Let's start calculating!\n")
        elif int(self.time_.strftime("%H")) > 16 and int(self.time_.strftime("%H")) < 21:
            print(f"Good Evening {self.name}. Let's start calculating!\n")
        else:
            print(f"Good Night {self.name} You should be sleeping. Anyway Let's calculate!")
