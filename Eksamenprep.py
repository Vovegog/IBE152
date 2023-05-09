def check_sort(chck_lst: list, a:int) -> bool:
    if chck_lst[-1] > a: # Since we're expecting a sorted list, we just need to check against the last number in the list
        return f"List has number larger than {a}"
    else:
        return f"List does not have number larger than {a}"
    
chck_lst = [1,2,4,5,8,9,12,15,16]

# print(check_sort(chck_lst,20))
# print(check_sort(chck_lst,10))

dictlist = [{
    "name": "sas", 
    "rep": "bad"
    },
    {
    "name": "norwegian", 
    "rep": "good"
    }]

def check_keys(lst:list, k:int) -> str:
    counter = 0
    values = {}
    for dicts in lst:
        if k in dicts:
            value = dicts[k]
            values[value] = values.get(value,0) + 1
            print(values)

    for num in values.values():
        if num > 1:
            counter += num
    return counter

my_list = [
{"name": "Alice", "age": 25},
{"name": "Bob", "age": 30},
{"name": "Charlie", "age": 25},
{"name": "Dave", "age": 25},
{"name": "Eve", "age": 30},
{"name": "Edgard", "age": 2}
]

# print(check_keys(my_list, "age"))

employees = { 5: ["English", "Norwegian"], 6: ["Spanish", "English"], 7: ["Japanese", "English"]}

def employee_to_use ( visitor: set, id: int ) -> bool:
    id_languages = employees[id]
    for lang in visitor:
        if lang in id_languages:
            return print(True)
    return print(False)

# employee_to_use({"Japanese", "Spanish"}, 5)
# employee_to_use({"Japanese", "Spanish"}, 6)
# employee_to_use({"Japanese", "Spanish"}, 7)

def total_screwtime(screws:str) -> int:
    iron = screws[:1]
    seconds = 0
    for i in range(len(screws)):
        if i > 0 and screws[i] != iron: # Check if we need to swap irons
            iron = screws[i]
            seconds += 5
        seconds += 1 # Remove screw
        if i != len(screws)-1: # Move to next if not at last
            seconds += 1
    return print(seconds)


# total_screwtime("+++++-")

def num_in_list ( num:int, lst:list ) -> bool:
    for i in range(len(lst)):
        if num == lst[i]:
            return True
    return False

# print(num_in_list(3, [1,2,3,4,5,6]))
# print(num_in_list(1, [1,2,3,4,5,6]))
# print(num_in_list(10, [1,2,3,4,5,6]))

def num_index ( num:int, lst:list ) -> int:
    for i in range(len(lst)):
        if lst[i] == num:
            return print(i)
    return print(-1)

# num_index(3,[1,2,3,4,5,6])
# num_index(10,[1,2,3,4,5,6])
# num_index(6,[1,2,3,4,5,6])

def check_lst_lst ( num:int, lst:list ) -> bool:
    for i in range(len(lst)):
        for nest in lst[i]:
            if nest == num:
                return True
    return False

# print(check_lst_lst(2,[[1,3],[1,4,5],[1,2],[5,6,9]]))
# print(check_lst_lst(7,[[1,3],[1,4,5],[1,2],[5,6,9]]))
# print(check_lst_lst(3,[[1,3],[1,4,5],[1,2],[5,6,9]]))

def equal_tuple ( tple:tuple ) -> bool:
    first_ele = tple[0]
    for ele in tple:
        if ele != first_ele:
            return False
    return True

# print(equal_tuple((1,1,1,1)))
# print(equal_tuple((3,3,3,3,3)))
# print(equal_tuple((1,1,2,1)))

binary = [1,2,3,4,5,6,7,8,9,10,13,15,18,19,20,24,29,31,34,36,39,45,50]

def binary_search ( num:int, lst:list ) -> bool:
    low = 0
    high = len(lst)
    while low != high + 1:
        mid = ( low + high ) // 2
        if num == lst[mid]:
            return True
        elif num > lst[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return False
        
# print(binary_search(10,binary))
# print(binary_search(12,binary))
# print(binary_search(23,binary))
# print(binary_search(38,binary))
# print(binary_search(39,binary))


# text = "This is a nice little string"

# print(text.split(" "))


# Eksamen ______________________

def function(text:str, size:int) -> str:
    """Receive a string, split on space and find the first word that matches the length of the specified size.

    Args:
        text (str): The string you want to test for.
        size (int): The size (length) of the word in characters.

    Returns:
        str: Returns the first occurence of a word matching the specified length.
    """
    word_found = ""
    split_text = text.strip(".").split(" ") # Remove punctuation, and split on space
    for word in split_text:
        if size == len(word):
            word_found = word
            return word_found
    return word_found

# print(function("Hei", 4))


courses = {"IBE152": ["Juan", "Ana", "Claudia"],
           "IBE500": ["Pedro", "Linda", "Maria"],
           "HIST01": ["David", "Laura"]
           }


# Write function that returns all female students (name ends with "a") as a tuple

def is_female(students:dict) -> tuple:
    """Go through a dictionary and find all students whose name ends with an "a".

    Args:
        students (dict): List of students, formed as a dictionary with the keys being the courses they are enrolled in.

    Returns:
        tuple: Return a tuple with all the names of students whose name ends with "a" (presumably female).
    """
    females = []
    for key in students:
        names = students.get(key)
        for name in names:
            if name.endswith("a"):
                females.append(name)
    return tuple(females)

# print(is_female(courses))


# Write function that receives a list of cities containing the names of all cities an airline flies from.
# A list of lists (direct_flights) indicates which cities are connected by which flights, and
# the name of the city. Return a list with the name of the cities connected by flights in either direction
# to the city.

cities = ["Seattle", "Denver", "New York", "Chicago"]

direct_flights = [
    [1, 0, 1, 1], # Seattle
    [0, 1, 1, 0], # Denver
    [1, 1, 1, 1], # New York
    [0, 0, 1, 1] # Chicago
]

def flights(cities:list, direct_flights:list, city:str) -> list:
    """Check for connecting, direct flights from a given city to other cities.

    Args:
        cities (list): A list containing all cities you can depart from.
        direct_flights (list): A nested list with 1's and 0's, correlating to index positions in the "cities" list, specifying which cities have a direct flight connection
        city (str): The city you want to depart from.

    Returns:
        list: Returns a list containing available direct flights from your specified departure city.
    """
    fly_from = cities.index(city) # City we fly from
    available_flights = [] # Cities we can land in
    for index, available in enumerate(direct_flights[fly_from]): # Enumerate and create counter
        if available == 1: # If flight can fly there:
            available_flights.append(cities[index]) # We append the name of the city to our list
    # Now we need to remove the fly_from city from our list, since we don't want to include
    # the opportunity to depart and land in the same city
    available_flights.remove(city)    
    return available_flights

# print(flights(cities, direct_flights, "Chicago"))


# Take two lists of integers as input
# Return a dictionary that maps index positions of each integer
# Index position should be the LAST occurence of every int.
# No break or continue

def find_int_index(list1:list, list2:list) -> dict:
    in_common = set(list1) & set(list2) # Sort out only the numbers that are common to both lists
    dct = {}
    for num in in_common: # Iterate over numbers
        dct[num] = range(len(list1.index(num)),0,-1) # Backwards? Nope, didn't work
    print(dct)

# Not enough time, RIP


find_int_index ([ 1, 0, 3, 4, 5, 3],  [ 3, 4, 5 ])

