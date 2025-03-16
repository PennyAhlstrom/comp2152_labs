import os
import sys
import platform
import socket

import mp

# Lab 9 Question 3.a.a., 3.a.b.
# Machine Type and Processor Type
print(platform.machine())
print(platform.architecture())

# Lab 9 Question 3.a.c, 3.a.d.
# Set and Get socket timeout
print(socket.getdefaulttimeout())
socket.setdefaulttimeout(50)
print(socket.getdefaulttimeout())

# Lab 9 Question 3.a.e
# OS name
print(os.name) # category of OS
print(platform.system())

# Lab 9 Question 3.a.f
# Process ID - Unique to every run
print(os.getpid())

# Lab 9 Question 3.b.a-d
# File Descriptors
# Open (or create) a file names fdpractise.txt
f_name = fdpractise.txt
# with open("fdpractise.txt", "a+") as f:
#     print(f.readline())
#     f.write("Hello, World")

# f1 = open(f_name, "r")
# print(f1)
# f1.close()

f = os.open(f_name, os.O_RDWR | os.O_CREAT) #bitwise operations will do both if needed
print(f)

f_obj = os.fdopen(f, "a+")
print(f_obj)
f_obj.close()

print()

# Lab 9 Question 3.b.e
# Forking (need to follow windows specific instructions for this)

# This will only work for Mac and Linux:
print("Before fork: ", os.getpid())
p = os.fork() # After this running python code in two different processes, first parent then child (typically, can be reconfiged)
print("After fork: ", os.getpid())

if p == 0:
    print("Child process")
    print("Parent process PID:", os.getppid())
else:
    print("Parent process")
    os.wait()
    print("Child process PID:", p)

# for windows - needs mp package installation
# context = mp.get_context('spawn')
# p = context.Process(target=function_name, args=(q,))
# p.start()
# p.join()

print("Last line")