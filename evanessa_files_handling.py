""" python file Handling practice """
import os  # check if the file exist in the sys
# r =read
# a= append
# w = write
# x = create

# read error if it doesn't exist
f = open("names.txt")
print(f.read())  # print out alll lines of the file

print(f.read(3)) # print the first 3th character in the file (Dav)

print(f.readline()) # read  one (first) line

# loop through the context of the file
for line in f:
    print(line)

f.close()
# its importeantto close the file in other
# to make the changing you did in the file to be implemented(show up)\
# tryning to read a file that  does not exist
try:
    f = open("name_list.txt")
    print(f.read())
except:
    print("error the file does not exist")
finally:
    f.close()

# appending two file(adding two files)
f = open("names.txt", "a")
f.write("Neil\n") #add something new to the file( add the name "Neil" to the file),
#we can see the name added to the file yet if we run it
f.close()

f = open("names.txt")
print(f.read())  # read the file to print out the changes we made (adding Neilto the file.
f.close()

# write (overwrite)
f = open("context.txt","w")
f.write("I deleted all of the context") # will delete all the content of the file and replace it with the "" conditions?references

f.close()

f = open("context.txt")
print(f.read())
f.close()

# two ways to create a new file:
# opens a file if does exist ,and create a file if does not exist>
f = open("name_list.txt","w")
f.close()

# creates the specified file,but returns an error if the file exists.

if not os.path.exists("dave.txt"):
    f= open("dave.txt","x") # cretae a file using operating system
    f.close()

# delete a file
if os.path.exists("dave.txt"):
    os.remove("dave.txt")
else:
    print("the file you wish to delete does not exist")


with open ("more_names.txt") as f:
    content = f.read()

