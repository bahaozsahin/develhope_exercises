import random

def create_rand_list(number = 15):
    random_list= [random.randint(-100,100) for _ in range(number)]
    return random_list


def print_and_sum(number=15):
    random_list = create_rand_list(15)
    print(random_list)
    sum = 0
    for number in random_list:
        sum += number
    print(sum)

    
print_and_sum(15)