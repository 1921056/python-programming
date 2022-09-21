# with open("sample.txt") as f:
#     content=f.read()

# content= content.replace("donkey","&%^$#%@")

# with open("sample.txt",'w') as f:
#     f.write(content)
list=["chor","motta","donkey","monkey"]

with open("sample.txt") as f:
    content=f.read()

for word in list:
    content= content.replace(word,"&%^$#%@")

with open("sample.txt",'w') as f:
    f.write(content)