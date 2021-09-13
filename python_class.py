class Man:
    def __init__(self, name):
        self.name = name
        print("initialnized!")

    def Hello(self):
        print("Hello " + self.name + "!")

    def goodbye(self):
        print("Good-Bye " + self.name + "!")

m = Man("young sic")
m.Hello()
m.goodbye()
        