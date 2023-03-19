'''
1.Создать список и заполнить его элементами различных типов данных
'''

type_list = [9, 5/6, True, [1,2], "Hi", {"Song": "Mamma Mia", "Group": "ABBA"},(1,2)]
for i in range (len(type_list)) :
    print(f"Тип переменной в списке: {type(type_list[i])}")

'''
2.Для списка реализовать обмен значений соседних элементов
'''

q = int(input("How many items in list do you want to add?\n\t Enter items quantity: "))
my_lst = []
for i in range(q):
    my_lst.append(input(f"Item # {i + 1} : "))
print(f"Your item list view:\n{my_lst}")
for x in range(0, (len(my_lst) - 1),2):
    my_lst[x], my_lst[x+1] = my_lst[x+1], my_lst[x]
print(f"Your CHANGED item list view:\n{my_lst}")

'''
3.Пользователь вводит месяц в виде целого числа от 1 до 12

'''

month = int(input("Please enter month id from 1 to 12 : "))
mlist = ["зима", "весна", "лето", "осень"]
while True:
    if month > 12 or month <= 0 :
        print(f"\tINCORRECT ID!!! \n\tPlease use number range from 1 to 12 only!")
        month = int(input("Please enter month id from 1 to 12 : "))
        continue
    mlist = ["зима", "весна", "лето", "осень"]
    if month == 12 or (month >= 1 and month < 3):
        print(f"\tSeason related to your Month id#{month}  is '{mlist[0]}'")
        break
    elif month >= 3 and month < 6:
        print(f"\tSeason related to your Month id# {month} is '{mlist[1]}'")
        break
    elif month >= 6 and month < 9:
        print(f"\tSeason related to your Month id# {month} is '{mlist[2]}'")
        break
    elif month >= 9 and month < 12:
        print(f"\tSeason related to your Month id# {month} is '{mlist[3]}'")
        break
'''
4.Пользователь вводит строку из нескольких слов, разделённых пробелами. 

'''

text = input("Please type your text : ")
T = text.split()
for x, y in enumerate (T, start=1) :
    if len(y) > 11 :
        y = y[:10]
        print(x, y)
    else :
        print (x,y)

