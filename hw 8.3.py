number_list = [1,2,3,4,5,6,7,8,9,10]

def decorator(num):
    #res = [value for value in number_list if value % 2 == 0]
    for value in number_list:
        if value % 2 ==0:
            number_list.remove(value)
    res = number_list
    print(res)

@decorator
def num (number_list):
    return number_list



