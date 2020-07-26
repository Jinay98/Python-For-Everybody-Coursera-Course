file_name = input("Enter file name: ")
try:
    file = open(file_name)
except:
    print("Not a valid file name")
    quit()
ans = []

for line in file:
    line = line.rstrip()
    list_of_words = line.split()
    for word in list_of_words:
        if word not in ans:
            ans.append(word)

ans.sort()
print(ans)
