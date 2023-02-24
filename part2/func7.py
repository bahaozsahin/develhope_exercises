my_list= [*range(5)] 
square_evens = lambda x: x**2 if x%2== 0 else x
result = list(map(square_evens, my_list))
print(result)