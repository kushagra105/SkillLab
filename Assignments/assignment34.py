#assignment 34 : Consider the set and predict the output
fruits = {"apple","orange","banana","apple","pear","papaya","papaya"}
fruit_basket = {"apple","banana","grapes","mango","kiwi"}
print (fruits)
print (fruits & fruit_basket)
print (fruits | fruit_basket)
print (fruits - fruit_basket)
print (fruits ^ fruit_basket)
print (len(fruit_basket))
print ("pear" in fruits)
print ("pear" not in fruit_basket)
print (fruits.issubset(fruit_basket))
print (fruits.issuperset(fruit_basket))
print (fruit_basket.copy())

# ==============OUTPUT==================
# {'banana', 'pear', 'orange', 'apple', 'papaya'}
# {'apple', 'banana'}
# {'banana', 'pear', 'grapes', 'orange', 'kiwi', 'apple', 'papaya', 'mango'}
# {'papaya', 'orange', 'pear'}
# {'papaya', 'pear', 'grapes', 'orange', 'mango', 'kiwi'}
# 5
# True
# True
# False
# False
# {'apple', 'banana', 'grapes', 'mango', 'kiwi'}