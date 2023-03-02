
# O1

def float_divide( n1 : float, n2 : float ) -> float :
    return n1 / n2

print(float_divide(100.0, 200.0))

# O2

def seconds_to_hms( n : int ) -> str :
    h = str(int(n//3600))
    m = str(int(n//60%60))
    s = str(int(n%3600%60))
    return (f"{h}:{m}:{s}")

print(seconds_to_hms(3600*1.57))

# O3

def check_sum( a : int, b : int, c : int) -> bool :
    if c > a + b or c % 2 == 0 :
        return True
    else :
        return False
    
print(check_sum(5, -8, -20))

# O4

def find_index(lst : list, number : int) -> int :
    if number in lst :
        return lst.index(number)
    else :
        return -1
    
print(find_index([0,1,2,3,4,5], 2))

# O5

def kg_to_lbs(kgs : float ) -> float :
    return kgs * 2.2

print(kg_to_lbs(3.5))

# O6

def triangle_length(a : int, b : int, c : int) -> str :
    if a + b < c or b + c < a or a + b < c :
        triangle = str("Not a triangle.")
    elif a == b == c :
        triangle = str("Equilateral triangle.")
    elif a == b or a == c or b == c :
        triangle = str("Isosceles triangle.")
    else :
        triangle = str("Scalene triangle.")
    return triangle

print(triangle_length(2,7,12))

# O7

def miles_to_meters ( miles : float ) -> float :
    return miles * 1609.344

print(miles_to_meters(0.5))

# O8

def isPosDiv( number : int ) -> bool :
    if number // 10 and number > 0 :
        return True
    else :
        return False
    
print(isPosDiv(10))

# O9

this_list = [45, 9362, 87, 0, -5, "Cow"]

def check_list ( lst : list, studentnr : int ) -> list :
    lst.insert(int(lst.index(9362))+1, studentnr)
    lst.pop(-1)
    return lst

print(check_list(this_list, 221271))

# O10

def mary( petals : int ) -> int :
    if petals % 2 == 1 :
        return 1
    else :
        return 2
    
print(mary(20))

# O11

def secret( paragraph : str, pairs : list ) -> str :
    pair1 = paragraph[pairs[0][0]:pairs[0][1]+1]
    pair2 = paragraph[pairs[1][0]:pairs[1][1]+1]
    pair3 = paragraph[pairs[2][0]:pairs[2][1]+1]
    return pair1 + pair2 + pair3

print(secret("Batman will try", [[0,0], [4,4], [9,10]]))
print(secret('Snow or chocolate is the question', [[1, 3], [17, 20], [13, 16]]))

# O12

def afford_kayak( budget : int, participants : int ) -> bool :
    lunch_cost = participants * 5
    if participants % 2 == 1 :
        cost_kayaks = ((participants // 2) * 20) + 15
    else :
        cost_kayaks = (participants // 2) * 20
    if participants <= 5 :
        basic_cost = 100
    elif participants >= 6 and participants <= 10 :
        basic_cost = 120
    else :
        basic_cost = 130
    return lunch_cost + cost_kayaks + basic_cost <= budget

print(afford_kayak(299, 11))

# O13
