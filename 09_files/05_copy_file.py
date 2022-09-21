# with open("sample.txt") as f:
#     content= f.read()

# with open("copy.txt",'w') as f:
#     f.write(content)

file1="copy.txt"
file2="sample.txt"
file3="log_file.txt"

with open(file1) as f:
    f1=f.read()

with open(file2) as f:
    f2=f.read()

with open(file3) as f:
    f3=f.read()
    

if f1==f2:
    print("files are identical with file1")
elif f1==f3:
    print("file is identical with log file")
else: 
    print("files are not identical")