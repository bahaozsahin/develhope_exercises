class Animal:
    def __init__(self, legs):
        print("Animal object was created")
        self.legs = legs
        self.runs_flag = False

    def runs(self):
        self.runs_flag = True
        print("Running started")

dog = Animal(4)
dog.runs()