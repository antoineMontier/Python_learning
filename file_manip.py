import os
print("\n\n")


reader = open("nothing_interesting.txt", "r") 

file_content = reader.read()

"""
for k in reader:
    print(k, end="") #without end="", it prints my text with an additionnal \n 
"""

reader.close()
os.remove("nothing_interesting.txt")
os.mkdir("text_files")
#print(file_content)


writer = open("text_files/starting_by_e.txt", "w")
write = 1
for c in file_content:

    if(c == "e" and write == 1):
        writer.write("\n")
        write = 2
    elif( c == " " or c == "\n"):
        write = 1
    elif(write != 2):
        write = 0
    if(write == 2):
        writer.write(c.upper())
            

writer.close()


print("\n\n")
