#import mammal
# - imports entire module then need to refer to module name
from mammal import Mammal
# only import for specific member that i ask yfor, dontr need to put name of module first.
# can just put name of class or method etc.import
from person_week12 import Person

from tick import Tick
# self is passed implicitly

from puma import Puma

m = Mammal(10)
m.speak() # shorthand method
#Mammal.speak(m) # Same thing, What python does in the background
#d = m.__str__() # prints the same as below
#d = str(m)
#print(d) can do this but expecting to do what's below
print(m)

p = Person("John Doe", 20, 6)
p.speak()
print(p)
p.heart.beat()
print(p.heart)

# print(m.heart == p.heart)

t = Tick()
t.suck_blood()
print(t) # output would be: <tick.Tick object at 0x000002466D0676B0>

pm = Puma(5, t)
pm.tick.suck_blood()
print(pm)
pm.claw()

pm2 = Puma(3)
pm2.claw()
