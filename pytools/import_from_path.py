import imp

root = os.path.abspath(os.sep)
foo = imp.load_source('module.name', root+'keys.py')
print(foo.ojeto_user)
