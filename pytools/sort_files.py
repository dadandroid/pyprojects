import os

search_dir = "/home/pi/pypics/"
os.chdir(search_dir)
files = filter(os.path.isfile, os.listdir(search_dir))
files = [os.path.join(search_dir, f) for f in files] # add path to each file
#files.sort(key=lambda x: os.path.getmtime(x))
sortedfiles = sorted(files,key=lambda x: os.path.getmtime(x))

print(files) 
print("_____________________________")
print(sortedfiles)
