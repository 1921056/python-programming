
fruits = ["apple", "mango", "banana", "papaya", "orange",
          "pineapple", "lichi", "grapes", "pomogranate"]

i = 1
while i < len(fruits):

    print(str(i) + "." + fruits[i].upper())
  
    print(" *" + fruits[i].lower())
    print(" *" + fruits[i].capitalize())
    i = i+1
