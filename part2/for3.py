list1 = ["lion", "monkey", "dog","fish"]
tuple1 = ("lion", "monkey", "dog","fish")
set1 = {"lion", "monkey", "dog","fish"}
dict1 = {"lion":"land", "monkey":"land", "dog":"land","fish":"water"}

#can also be done by using multiple for loops iterating over elements

for i in range(len(list1)):
    print(list1[i])
    print(tuple1[i])
    print(list(set1)[i])
    print(list(dict1.keys())[i], 'lives in ', list(dict1.values())[i])
