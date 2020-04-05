import os
file_read = open("Readme","a")
file_read = open("Readme")
file_write = open("Readme[复制]","w")
while True:
    text = file_read.readline()
    if not text:
        break
    file_write.write(text)
file_read.close()
file_write.close()
os.remove("Readme")
os.remove("Readme[复制]")

