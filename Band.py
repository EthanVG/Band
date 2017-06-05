import random

class Musician(object):
    def __init__(self, sounds):
        self.sounds = sounds

    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)]) #end=" " is not working, removed for now
        print()

class Bassist(Musician): # The Musician class is the parent of the Bassist class
    def __init__(self):
        # Call the __init__ method of the parent class
        super(Bassist, self).__init__(["Twang", "Thrumb", "Bling"])

class Guitarist(Musician):
    def __init__(self):
        # Call the __init__ method of the parent class
        super(Guitarist, self).__init__(["Boink", "Bow", "Boom"])

    def tune(self):
        print("Be with you in a moment")
        print("Twoning, sproing, splang")

class Drummer(Musician):
    def __init__(self):
        super(Drummer, self).__init__(["Crash", "Tick", "Thack"])
    
    def count(self):
        start = ["One", "Two", "Three", "Four"]
        for i in start:
            print(i)
        print()
    
    def spontaneousCombustion(self):
        print("SWOOSH")
        print("sssssss.....")
        print("The drummer has been replaced with a pile of ashes.")
        
class Band(object):
    def __init__(self, group):
        self.group = group
    
    def hire(self, Musician):
        self.group.append(Musician)
        
    def fire(self, Musician):
        self.group.remove(Musician)
        
    def play(self):
        for i in self.group:
            if (isinstance(i, Drummer)):
                i.count()
        for i in self.group:
            if (isinstance(i, Drummer)) == False:
                i.solo(random.randint(1,6))

Tom = Bassist()
Dick = Guitarist()
Harry = Drummer()
Nick = Guitarist()
friends = [Tom, Dick, Harry]

P3 = Band(friends)
P3.hire(Nick)
P3.fire(Dick)
P3.play()


        

        