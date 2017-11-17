import imp
import os

if os.name == 'posix': root = "/home/pi/"    
elif os.name == 'nt': root = os.path.abspath(os.sep)

foo = imp.load_source('module.name', root+'pykeys.py')
print(foo.ojeto_user)
