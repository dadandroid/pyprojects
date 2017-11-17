import os
import imp

root=  os.path.abspath(os.sep)

foo = imp.load_source('module.name', '/home/pi/keys.py')
print(foo.ojeto_user)

