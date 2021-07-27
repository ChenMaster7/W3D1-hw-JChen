'''
Excercise 1: Filter out empty strings
Output: ['Argentina', 'San Diego', 'Boston', 'New York']
'''
places = [" ","Argentina", " ", "San Diego","","  ","","Boston","New York"]
print(list(filter(lambda word: False if word == "" or word.isspace() else True, places)))



'''
Exercise 2: Write an anonymous function that sorts this list by last name
Output: ['Victor aNisimov', 'Gary A.J. Bernstein', 'Andrew P. Garfield', 'David hassELHOFF', 'Shoha Tsuchida']
'''
author = ["Shoha Tsuchida", "Victor aNisimov", "Andrew P. Garfield","David hassELHOFF","Gary A.J. Bernstein"]
author.sort(key=lambda name: name.lower().split()[-1])



'''
Exercise 3: Convert the list below from Celsius to Fahrenheit, using the map function with a lambda
Output: [('Nashua', 89.6), ('Boston', 53.6), ('Los Angelos', 111.2), ('Miami', 84.2)]
'''
# F = (9/5)*C + 32
places = [('Nashua',32),("Boston",12),("Los Angelos",44),("Miami",29)]
print(list(map(lambda city_temp: (city_temp[0], (9/5)*city_temp[1]+32), places)))




'''
Exercise 4: Write a recursion function to perform the fibonacci sequence up to the number passed in.
Output for fib(5) => 
Iteration 0: 1
Iteration 1: 1
Iteration 2: 2
Iteration 3: 3
Iteration 4: 5
Iteration 5: 8
'''

# Can't figure out a local counter that can +1 per iteration. Also not updating the correct number.
def fib(num):
    if num <= 1:
        return num
    else:
        print(f'Iteration: {num}')
        return num+fib(num-1)

fib(5)
