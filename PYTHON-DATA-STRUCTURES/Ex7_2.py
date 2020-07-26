file_name = input("Enter file name: ")
try:
    file = open(file_name)
except:
    print("Not a valid file name")
    quit()
total = 0
count = 0
for line in file:
    if line.startswith("X-DSPAM-Confidence:"):
        line = line.rstrip()
        line = line.replace(" ", "")
        index = line.find(":")
        no = float(line[index+1:])
        total += no
        count += 1
print("Average spam confidence:", (total/count))
