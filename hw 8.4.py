number_list = [1,2,3,4,5,6,7,8,9,10]

def decorator(num):
    number_list.sort(reverse=True)
    res = number_list
    print(res)

@decorator
def num (number_list):
    return number_list
