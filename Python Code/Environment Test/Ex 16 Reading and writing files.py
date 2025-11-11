from sys import argv 

script, filename = argv


print("We're going to erase %r." % filename)
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want to do that, hit RETURN.")

input("?")

print("Opening the file...")
#The w parameter specifies to open a file of the given name or create one with the given name.
#Also truncates the file as it opens it
target = open(filename, 'w')

print("Truncating thee file. Goodbye.")
#target.truncate()

print("Now I'm going to as you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to writee these to the file.")

"""
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
"""

print("%s\n%s\n%s\n" % (line1, line2, line3))
target.write("%s\n%s\n%s\n" % (line1, line2, line3))

print("And finally, we close it.")
target.close()