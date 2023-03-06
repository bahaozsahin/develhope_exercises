names = ['John', 'Tristram', 'Baldwin', 'Wally']
surnames = ['Doe', 'Mcbride', 'Preston', 'Collins']

def greet(name= 'John', surname = 'Doe'):
    print('Hello', name, surname)

for i in range(max(len(names), len(surnames))):
    greet(names[i], surnames[i])
