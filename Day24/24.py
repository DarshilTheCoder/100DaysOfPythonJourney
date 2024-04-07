#Day24 of learning python Going to learn about file read(),write() using 'with'keyword

# file = open('file.txt')
# content = file.read()
# print(content)
# file.close() #it is very important to close the file as it uses some resources of your computer but many times we forget to close the file so we use 'with' keyword to open file 

with open('C:/pythondemofile/file.txt',mode='r') as file2:
    content2 = file2.read()
    print(content2) 
    #python will close the file automatically

# with open('C:/pythondemofile/file.txt',mode='a') as f:
#     content3 = f.write('\n this is another text understand after absolute and relative file path')
#     print(content3)