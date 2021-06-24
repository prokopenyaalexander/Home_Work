list_str = ['str', 'буква','Машина','имя','555']
list_str.sort()
i = 0
#for value in list_str:
    
    #print(i,value)
    #i += 1
sorted_list = [(i.index(list_str),value) for value in list_str]
print(sorted_list)