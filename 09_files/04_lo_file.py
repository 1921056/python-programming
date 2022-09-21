# with open("log_file.txt") as f:
#     content=f.read().lower()

# if 'python' in content:
#     print("yes python is present")
# else:
#     print("not present")



content= True 
i=1 
with open("log_file.txt") as f:
    while content:
        content =f.readline()
        
        if 'python' in content.lower():
            print(content)
            print(f"yes python is present at line number {i} ")
        i=i+1
            
            
            