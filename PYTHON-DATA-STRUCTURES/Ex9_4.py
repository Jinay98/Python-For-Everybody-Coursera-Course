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
        count[list_of_words[1]] = count.get(list_of_words[1], 0)+1

for email, frequency in count.items():
    if max_count is None or frequency > max_count:
        max_count = frequency
        max_email = email
print(max_email,max_count)