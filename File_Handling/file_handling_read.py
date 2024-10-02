file = open("/Users/sushmitadhawni/PycharmProjects/pythonProjectc/My_first_repo"
            "/files/sample.txt","r")

#print(file.read())
#read 15 chracters
#print(file.read(15))

#readlines
lines= file.readlines()
print(lines)  #print in list format
for line in lines:
    print(line)

file.close()
