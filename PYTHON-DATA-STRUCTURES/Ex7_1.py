file_name = input("Enter the file name")
try:
    file= open(file_name)
except:
    print("Not a valid file name")
    quit()
for line in file:
    line = line.rstrip()
    print(line.upper())