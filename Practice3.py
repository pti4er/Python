# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.


m_list = [int(input("Введите месяц в виде целого числа от 1 до 12 (list): "))]
if m_list == [1] or m_list == [2] or m_list == [12]:
    print ("Зима")
elif m_list == [3] or m_list == [4] or m_list == [5]:\
    print ("Весна")
elif m_list == [6] or m_list == [7] or m_list == [8]:
    print ("Лето")
elif m_list == [9] or m_list == [10] or m_list == [11]:
    print ("Осень")
else:
    print ("Error: Вы ввели не верное число")

m_dict = {"month": int(input("Введите месяц в виде целого числа от 1 до 12 (dict): "))}

if m_dict["month"] == 1 or m_dict["month"] == 2 or m_dict["month"] == 12:
    print ("Зима")
elif m_dict["month"] == 3 or m_dict["month"] == 4 or m_dict["month"] == 5:
    print ("Весна")
elif m_dict["month"] == 6 or m_dict["month"] == 7 or m_dict["month"] == 8:
    print ("Лето")
elif m_dict["month"] == 9 or  m_dict["month"] == 10 or m_dict["month"] == 11:
    print ("Осень")
else:
    print ("Error: Вы ввели не верное число")

