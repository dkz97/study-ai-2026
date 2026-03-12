"""
    #define a function
    def functionName (parameter):
        function body
        ...
        return result

    Optional : parameter 、 return

    # call a function
    function(parameter)

    # parameter
    *args -> tuple
    **kwargs -> dict
"""

def out_line():
    print("Hello Function")

out_line()


def def_tmp(*args, **kwargs):
    print(args)
    print(kwargs)

def_tmp(1,3,3,5)
def_tmp(1,3,3,5, a=1,b=2)


# Case 1: Calculate the area of triangle using the base an height
def area_triangle(base, height):
    return base * height / 2

print(area_triangle(3,4))


# Case 2: Count vowels in a given string
def vowels_count(s):
    num = 0
    vowels = "aeiou"
    for v in s:
        if v.lower() in vowels:
            num += 1
    return num

print(vowels_count("aeiouACMDKA"))


# Case 3: Calculate the maximum, minimun, and average score from a list
def cal_score(score_list):
    maximun = score_list[0]
    minimun = score_list[0]
    total = 0
    for num in score_list:
        if num > maximun: maximun = num
        if num < minimun: minimun = num
        total += num
    
    return maximun, minimun, total / len(score_list)

print(cal_score(range(1,8)))


# Case 4: Sum
def sum_num(*args):
    return sum(args)

print(sum_num(1,54,5,2,56,2))


# Case 5: Check if a number even or odd
def check_num(num):
    if num % 2 == 0: 
        return "even"
    return "odd"

print(check_num(3))
