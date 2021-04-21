# 1. На склад поступил новый товар. Надо пересмотреть склад и исправить ошибки, сделать первую товара букву заглавной.
# Все типы товаров должны быть неизменяемыми, чтобы кто-то случайно не перепутал их снова.
# В овощи забыли добавить капусту. Цифра в категории - это цена товара этого типа. + 
print("############################ TASK 1 ##########################################")
print()
fruit = ('apple', 'pear', 'cherry', 'banana', 12)       #tuple
vegetables = ['tomato', 'onion', 'carrot', 17]          #list
berries = ('blueberry', 'cranberry', 'watermelon', 8)   #tuple

vegetables.insert(3, "cabbage") #добавление капусты к списку овощей

new_fruit = []
new_vegetables = []
new_berries = []

#section fruit
for  value in fruit[0:4] :
    new_fruit.append(value.title())
new_fruit.append(fruit[-1])    
fruit = tuple(new_fruit)
print("Исправленная секция Fruit", fruit, "Тип - ", type(fruit))

#section vegetables
for  value in vegetables[0:4] :
    new_vegetables.append(value.title())
new_vegetables.append(vegetables[-1])    
vegetables = tuple(new_vegetables)
print("Исправленная секция vegetables", vegetables, "Тип - ", type(vegetables))

#section berries
for  value in berries[0:3] :
    new_berries.append(value.title())
new_berries.append(berries[-1])    
berries = tuple(new_berries)
print("Исправленная секция berries", berries, "Тип - ", type(berries))
print()
# 2. Для удобства хранения, нужно объединить все товары в один объект, при этом сохранить структуру типов.
print("############################ TASK 2 ##########################################")
print()
fruit = list(fruit)
vegetables = list(vegetables)
berries = list(berries)

warehouse = {"fruit" : fruit, "vegetables" : vegetables, "berries" : berries }
print("Warehouse - ",warehouse)
print()
# 3. На складе закончились морковка и арбузы. Надо перенести их в категорию "finished".

#fruit = ('apple', 'pear', 'cherry', 'banana', 12)       
#vegetables = ['tomato', 'onion', 'carrot', 'cabbage', 17]          
#berries = ('blueberry', 'cranberry', 'watermelon', 8)
print("############################ TASK 3 ##########################################")
print()
finished = []
#recognize end of carrot
temp = warehouse["vegetables"]
for value in temp:
    if value ==  "Carrot":
        index = temp.index(value)
end_carrot = temp.pop(index)
finished.append(end_carrot)

#recognize end of watermelon

temp = warehouse["berries"]
for value in temp:
    if value ==  "Watermelon":
        index = temp.index(value)
end_carrot = temp.pop(index)
finished.append(end_carrot)

print("Закончившиеся товары - ",  finished)
print()
# 4. Если название продукта длиннее 6 символов, нужно отображать только первые 6.

#fruit = tuple(fruit)
#vegetables = tuple(vegetables)
#berries = tuple(berries)
print("############################ TASK 4 ##########################################")
print()
abbr_fruit = []
for value in fruit[0:4]:
    index_of_value = fruit.index(value)
    if len(value) > 6:
        temp = value[0:6]
        abbr_fruit.append(temp)
    else:
        print("Haven't such condition for -", value, "- from fruit")
print("ABBR_FRUIT",abbr_fruit)

abbr_vegetables = []
for value in vegetables[0:2]:
    index_of_value = vegetables.index(value)
    if len(value) > 6:
        temp = value[0:6]
        abbr_vegetables.append(temp)
    else:
        print("Haven't such condition for - ", value, "- from vegetables")
print("ABBR_VEGETABLES",abbr_vegetables)
 
abbr_berries = []
for value in berries[0:2]:
    index_of_value = berries.index(value)
    if len(value) > 6:
        temp = value[0:6]
        abbr_berries.append(temp)
    
    else:
        print("Haven't such condition for - ", value, "- from beriies") 
print("ABBR_BERRIES",abbr_berries)
print()
print("############################TASK 5 ##########################################")
print()
# 5. На все товары, где есть буква "r", нужно сделать скидку в 20%.
# А если их 2, то 25,5%, и сумму округлить до 2 символов после запятой.
# Рассчитать и вывести на экран стоимость каждого отдельного продукта.

#fruit = ('apple', 'pear', 'cherry', 'banana', 12)       
#vegetables = ['tomato', 'onion', 'carrot', 'cabbage', 17]          
#berries = ('blueberry', 'cranberry', 'watermelon', 8)   

count_of_words_fruit = 0
substr = "r"
price  = 12
for value in fruit[0:4]:
    if substr in value:
        count_of_words_fruit +=1
        print("word with 'r' ", value)
        print("count_of_words_fruit", count_of_words_fruit)
    else:
        print("No letter in word - ", value)
if count_of_words_fruit >= 2:
    discount = price / 100 * 25.5
    print("Your discount for fruits - ", round(discount,2))
else:
    discount = price  / 100 * 20
    print("Your discount for fruits - ", round(discount,2))
print()
print("#################################################################")
count_of_words_vegetables = 0
substr = "r"
price  = 8
for value in vegetables[0:3]:
    if substr in value:
        count_of_words_vegetables +=1
        print("word with 'r' ", value)
        print("count_of_words_vegetables", count_of_words_vegetables)
    else:
        print("No letter in word - ", value)
if count_of_words_fruit >= 2:
    discount = price / 100 * 25.5
    print("Your discount for vegetables - ", round(discount,2))
else:
    discount = price  / 100 * 20
    print("Your discount for vegetables - ", round(discount,2))
print()
print("#################################################################")

count_of_words_berries = 0
substr = "r"
price  = 17
for value in berries[0:2]:
    if substr in value:
        count_of_words_berries +=1
        print("word with 'r' ", value)
        print("count_of_words_berries", count_of_words_berries)
    else:
        print("No letter in word - ", value)
if count_of_words_fruit >= 2:
    discount = price / 100 * 25.5
    print("Your discount for berries - ", round(discount,2))
else:
    discount = price  / 100 * 20
    print("Your discount for berries - ", round(discount,2))
