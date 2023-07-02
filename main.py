class person():
    def __init__(self, *args, **kwargs):
        if len(args) >= 2:
            self.args = args # grabs all args
            self.fname = args[0] # set by args number 1
            self.lname = args[1] # set by args number 2
        else:
            self.fname = 'No first name provided'
            self.lname = 'No last name provided'
        
        self.attributes = {
                        'status': kwargs.get('status', 'unknown'), # set by kwargs keyword
                        'health': kwargs.get('health', 'unknown'), # set by kwargs keyword
                        'powerlevel': args[2] if len(args) >= 3 else 'somewhere near zero'  # set by args number 3
                        }

    def talk(self):
        print(f'I am {self.fname} {self.lname}')

    def introduce(self, *args):
        print('--------------------------------')
        for arg in args:
            if callable(arg):
                arg()
        self.talk()
        print(f'Status: {self.attributes["status"]}')
        print(f'Health: {self.attributes["health"]}')
        print(f'Powerlevel: {self.attributes["powerlevel"]}')


class drummer(person):
    def __init__(self, drummer, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.drummer = drummer
        self.attributes['status'] = 'drummer' if self.drummer else 'not a drummer'


# uses a wrapper saves returned string and prints it after hello
def hello(func):
    def wrapper():
        world = func()
        if isinstance(world, str):  
            print(f'hello{world}!')
        else:
            print('hello...you messed up!')
    return wrapper

# returns a string of ' world'
@hello
def world():
    return ' world'

# prints hello world
def helloworld():
    world()

def mindset():
    print("I've got my mind set on you!")

# creating an object using 3 arguments and 2 keyword arguments
noone = person('no', 'one', '9000', status='invisible', health='transparent')
noone.introduce(helloworld)

# creating an object using no arguments and no keyword arguments
another = person()
another.introduce()

# creating an drummer that inherits from person
ringo = drummer(True, 'Ringo', 'Star', powerlevel='da best')
ringo.introduce()

george = drummer(False, 'George', 'Harrison')
george.introduce(helloworld, mindset)
