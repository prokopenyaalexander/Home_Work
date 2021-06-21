 #Даны три слова. Выяснить, является ли хоть одно из них палиндромом
#("перевертышем"), т. е. таким, которое читается одинаково слева направо и
#справа налево. (Определить функцию, позволяющую распознавать слова
#палиндромы.)

def palindrom(list):
    count = 0
    for value in list:
        if value == value[::-1] :
            count += 1           
    print(count)

words = ["Шалаш", "323","rocket", "bank", "ООО"]

new_words = []
for value in words:
    new_words.append(value.lower())
    
palindrom(new_words)