str1 = []
for readLine in open("1.txt", encoding="utf-8"):
    str1.append(readLine)
str2 = []
for readLine in open("2.txt", encoding="utf-8"):
    str2.append(readLine)
str3 = []
for readLine in open("3.txt", encoding="utf-8"):
    str3.append(readLine)

str_file = {}
str_file["1.txt"] = str1
str_file["2.txt"] = str2
str_file["3.txt"] = str3

sorted_items = sorted(str_file.items(), key=lambda x: len(x[1]))

str_all = []
for name, strs in sorted_items:
    str_all.append(name+"\n")
    str_all.append(str(len(strs))+"\n")
    for index, s in enumerate(strs):
        str_all.append("Строка номер "+str(index+1)+": "+s)
    str_all.append("\n")

with open('all.txt', 'w', encoding="utf-8") as f:
    for s in str_all:
        f.write(s)