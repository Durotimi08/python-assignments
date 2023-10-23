myfile = open("D:\\Backup\\python\\python-assignments\\file.txt", "r")
# myfile.write("\nThis is python file\n the topic is file handling")
if (input("What will you like to do 1, Read news: ") == "1"):
    print(myfile.read(5)); myfile.close()