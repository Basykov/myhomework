# Make a class called Person.
#  Make the __init__() method take firstname, lastname, and age as parameters and add them as attributes.
#  Make another method called talk() which makes prints a greeting from the person containing, for example like this:
#   "Hello, my name is Carl Johnson and I’m 26 years old".



class Person():
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
    def talk(self):
        print (f"Hello, my name is {self.firstname} {self.lastname} and I’m {self.age} years old")

if __name__ == '__main__':
    gg = Person("Jhon", "Rebell", 23)

    print(gg.firstname)
    print(gg.lastname)
    print(gg.age)
    gg.talk()


# Create a class Dog with class attribute 'age_factor' equals to 7.
#  Make __init__() which takes values for a dog’s age.
# Then create a method `human_age` which returns the dog’s age in human equivalent.



class Dog():
    age_factor = 7
    def __init__(self,age):
        self.age = age
    def human_age(self):
        b = self.age * self.age_factor
        return b
    
if __name__ == '__main__':

    Bobby = Dog(3)
    print(Bobby.human_age())


# Create a simple prototype of a TV controller in Python. It’ll use the following commands:

#     first_channel() - turns on the first channel from the list.
#     last_channel() - turns on the last channel from the list.
#     turn_channel(N) - turns on the N channel. Pay attention that the channel numbers start from 1, not from 0.
#     next_channel() - turns on the next channel. If the current channel is the last one, turns on the first channel.
#     previous_channel() - turns on the previous channel. If the current channel is the first one, turns on the last channel.
#     current_channel() - returns the name of the current channel.
#     exists(N/'name') - gets 1 argument - the number N or the string 'name' and returns "Yes",
#     if the channel N or 'name' exists in the list, or "No" - in the other case.



class TVController():
    def __init__(self, channels):
        self.channels = channels
        self.current_channel_index = 0
    def first_channel(self):
        self.current_channel_index = 0
        return self.current_channel_index
    def last_channel(self):
        self.current_channel_index = -1
        return self.current_channel_index
    def turn_channel(self,a):
        self.current_channel_index = a-1
        return self.current_channel_index
    def next_channel(self):
        if len(self.channels) > self.current_channel_index +1:
            self.current_channel_index +=1
            return self.current_channel_index
        else:
            self.current_channel_index = 0
            return self.current_channel_index
    def previous_channel(self):
        if self.current_channel_index == 0:
            self.current_channel_index = len(self.channels) - 1
            return self.current_channel_index
        else:
            self.current_channel_index -= 1
            return self.current_channel_index
    def current_channel(self):
        return f"You are watching {self.channels[self.current_channel_index]}"
    def exists(self,name):
        if name in self.channels:
            return ("Yes")
        elif type(name) == int  and name <= len(self.channels):
            return ("Yes")
        else:
            return("no")

if __name__ == '__main__':
        
    CHANNELS = ["BBC", "Discovery", "TV1000"]

    controller = TVController(CHANNELS)
    print(controller.channels)

    print(controller.current_channel())

    controller.last_channel()
    print(controller.current_channel())

    controller.turn_channel(2)
    print(controller.current_channel())

    controller.next_channel()
    print(controller.current_channel())

    controller.previous_channel()
    print(controller.current_channel())

    print(controller.exists("BBC"))
    print(controller.exists("Discovery"))
    print(controller.exists("TV1000"))
    print(controller.exists(1))
    print(controller.exists(2))
    print(controller.exists(3))
    print(controller.exists("sdaaw"))
    print(controller.exists(4))
