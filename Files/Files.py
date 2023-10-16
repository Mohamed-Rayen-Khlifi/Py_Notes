#Open function returns a file object that is iterable by lines
#w: write(overwrite the file), r:read, a:append, r+:read and write
#  First method
File = open('file_path', mode='r')  
File.readlines()
File.close() 
#  Second method: the with keyword automatically closes the file when we're done
with open('file_path', mode='w') as File:
    File.write('First Line')

#Methods of file objects
f.read() #Reads the entire contents of the file
f.readline() #Reads a single line from the file
f.readlines() or list(f) #Reads 
f.write('Text to write\n') 
f.seek()

#Copy files
import shutil
shutil.copy('src', 'dst')



