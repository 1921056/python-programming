# this = "             my name is kishan Tiwari        "
# print(this)
# print(this.strip())

def remove_and_strip(string,word):
    newstr=string.replace(word,"")
    return newstr.strip()

this = "             My name is kishan       "
n=remove_and_strip(this,"kishan")
print(n)
