from random import sample
from sys import exit

class Engine(object):
    
    def __init__ (self, world):
        self.gamename = "The Game of Posit"
        self.world = world
        self.player = self.world.people.get('PLAYER')
        for person in world.people:
            self.send_person(person, 'house_' + person)
        while True:
            print self.gamename
            print len(self.gamename) * '-'
            self.run_menu([])
    
    def show_location(self):
        print "You (%s) are at %s %s." % (self.player.name, \
                                        self.player.current_loc.prep, \
                                        self.player.current_loc.name)
    
    def run_menu(self, menu):
        menu = self.world.people.get('PLAYER').current_loc.menu
        #menu.append(('Exit', 'exit(0)'))
        for option in menu:
            print "[%s] %s" % ((menu.index(option) + 1), option[0])
        main_menu = self.main_menu()
        menu_select = raw_input("-->")
        try:
            menu_select = int(menu_select) - 1
            menu_select = 'self.player.current_loc.' + \
                                menu[menu_select][1]   
        except:
            menu_select = str(menu_select)
            for option in main_menu:
                if option[0] == menu_select.upper():
                    menu_select = 'self.' + option[3]
          
        exec menu_select
        
    def main_menu(self):
        main_menu = [('L', 'Location', 'show_location()')]     
        print len(self.gamename) * '-'
        for option in main_menu:
            print "[%s] %s" % (option[0], option[1])
        return main_menu
            
    def send_person(self, person, location):
        """Send a person somewhere."""
        self.world.people.get(person).current_loc = self.world.locations.get(location)
    
    def send_random_group(self, location, n):
        """Picks n random people to go somewhere."""
        if n > len(world.people):
            n = len(world.people)
        for person in sample(world.people.keys(), n):
            self.send_person(person, location)
            
class Location(object):
    
    def enter(self):
        print "Subclass this class and implement enter()."
        exit(1)

class School(Location):
        
    def __init__ (self):
        self.name = "Canterlot High School"
        self.prep = "at"
        
    def enter(self):
        pass

class Car(Location):
    
    def __init__ (self):
        self.name = "Car"
        self.menu = ['Start Car', 'Honk Horn']
        self.prep = "in a"
        
    def enter(self):
        pass
        
class Chatroom(Location):
    
    def __init__ (self):
        self.name = "Chatroom"
        self.prep = "in a"

    def enter(self):
        pass

class House(Location):
    
    def __init__(self, owner):
        self.name = owner.name + "'s House"
        self.menu = [('Test', 'test()'),
                    ('Add Floor', 'add_floor()')
                    ]
        self.floor = 2
        self.prep = "at"
        
    def add_floor(self):
        self.floor += 1
        print "Floors:", self.floor

    def enter(self):
        pass

class World(object):

    def __init__(self, names):
        self.people = self.get_player_name() # Get the player's name.
        for name in names[0:20]: # Create 20 people.
            self.people[(name[0])] = Person(name[0], name[1], self)
        
        self.locations = { # Add generic locations.
            'school': School(),
            'car': Car(),
            'chatroom': Chatroom(),
        }
        
        for person in self.people: # Give each person a house to live in.
            self.locations['house_' + person] = House(self.people.get(person))
    
    def get_player_name(self):
        #name = raw_input("Name ->") or 'Player'
        #gender = raw_input("Gender (m/f) ->")
        name = 'Dan'
        gender = 'm'
        player = {'PLAYER': Person(name, gender, self, True)} 
        return player
    
    def gps(self): # For debugging, show's everyone's current location.
        for person in self.people:
            print person, "-", self.people.get(person).current_loc.name

class Person(object):
    
    def __init__(self, name, gender, world, player=False):
        self.name = name
        self.gender = gender
        self.res = 0.5
        self.happiness = 0.5
        self.pop = 0.5
        self.player = True
            
names = (
        ('Michael', 'm'), ('Christopher', 'm'), ('Jason', 'm'), ('David', 'm'),
        ('James', 'm'), ('Matthew', 'm'), ('Joshua', 'm'), ('John', 'm'),
        ('Robert', 'm'), ('Joseph', 'm'), ('Daniel', 'm'), ('Brian', 'm'),
        ('Justin', 'm'), ('William', 'm'), ('Ryan', 'm'), ('Eric', 'm'),
        ('Nicholas', 'm'), ('Jeremy', 'm'), ('Andrew', 'm'), ('Timothy', 'm'),
        ('Jennifer', 'f'), ('Amanda', 'f'), ('Jessica', 'f'), ('Melissa', 'f'),
        ('Sarah', 'f'), ('Heather', 'f'), ('Nicole', 'f'), ('Amy', 'f'),
        ('Elizabeth', 'f'), ('Michelle', 'f'), ('Kimberly', 'f'),
        ('Angela', 'f'), ('Stephanie', 'f'), ('Tiffany', 'f'),
        ('Christina', 'f'), ('Lisa', 'f'), ('Rebecca', 'f'), ('Crystal', 'f'),
        ('Kelly', 'f'), ('Erin', 'f')
)

world = World(names)
play = Engine(world)
#play.send_random_group('school', 10)
#play.send_person('Kelly', 'car')
#world.gps()
play.send_person('PLAYER', 'car')
print world.people.get('PLAYER').current_loc.name