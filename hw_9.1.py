import csv

rows = []
age_rows = []
with open("/home/alex/Загрузки/lesson_9-20210630T194138Z-001/lesson_9/file.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader) 
    for row in csvreader:
        rows.append(row)
    for value in rows:
        for value in value:
            if value.isdecimal():
                age_rows.append(value)
    

    first_age_group = []
    second_age_group = []
    thirth_age_group = []
    fourth_age_group = []
    fifth_age_group = []
    result_list = []

    for value in age_rows:
        value = int(value)
        if int(value) >= 1 and value <= 12:
            first_age_group.append(value)
        elif int(value) >= 13 and value <= 18:
            second_age_group.append(value)
        elif int(value) >= 19 and value <= 25:
            thirth_age_group.append(value)
        elif int(value) >= 26 and value <= 40:
            fourth_age_group.append(value)
        elif int(value) > 40:
            fifth_age_group.append(value)
    result_list.append(first_age_group)
    result_list.append(second_age_group)
    result_list.append(thirth_age_group)
    result_list.append(fourth_age_group)
    result_list.append(fifth_age_group)


fields = ['First group', 'Second group', 'Third group', 'Fourth grooup', 'Fifth group']
with open("/home/alex/Загрузки/lesson_9-20210630T194138Z-001/lesson_9/report.csv", 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(result_list)
    







    #print("Количество строк: %d" % (csvreader.line_num))
    #col = []
    #for col in fields:
        #print("%10s" % col, end='')
        #print()
    #for row in rows:
        #for col in row:
            #print("%10s"%col, sep='', end=' ')
        #print()