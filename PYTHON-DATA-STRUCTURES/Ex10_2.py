file_name = input("Enter file name: ")
try:
    file = open(file_name)
except:
    print("Not a valid file name")
    quit()

count = dict()
max_count = None
max_email = None
for line in file:
    line = line.rstrip()
    if line.startswith("From "):
        list_of_words = line.split()
        list_of_time = list_of_words[5].split(":")
        count[list_of_time[0]] = count.get(list_of_time[0], 0)+1

sorted_list = sorted(count.items())
for value in sorted_list:
    print(value[0],value[1])

