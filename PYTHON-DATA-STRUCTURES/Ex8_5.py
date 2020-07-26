file_name = input("Enter file name: ")
try:
    file = open(file_name)
except:
    print("Not a valid file name")
    quit()

count = 0
for line in file:
    line = line.rstrip()
    if line.startswith("From "):
      list_of_words = line.split()
      print(list_of_words[1])
      count+=1
print("There were", count, "lines in the file with From as the first word")