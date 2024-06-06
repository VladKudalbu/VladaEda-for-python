print(f"{'-' * 11}\nMY.SHOP.RU\n{"-" * 11}")

#Система проверки возраста
age = input("Укажите ваш возраст: ")


if int(age) > 100:
    print("Скорее всего вы мертвы или врете. Доступ воспрещен")
    input("Чтобы выйти нажмите Enter ")
    exit()
elif int(age) >= 18:
    print("Доступ разрешен!")
else:
    print("Вы не совершеннолетний. Доступ воспрещен")
    input("Нажмите Enter чтобы выйти ")
    exit()

#Система регистрации и входа
#Sign-up
print("\nПеред началом покупок, пожалуйста зарегестрируйтесь")
Sign_up = input("Введите логин: ")
password_Reg = input("Введите пароль: ")
print(f"Запишите свои данные: Логин: {Sign_up} Пароль: {password_Reg}")

#Log-in
print("Теперь подтвердите вход")
print("\nПожалуйста войдите в свой аккаунт")
login = input("Введите логин: ")
password = input("Введите свой пароль: ")

if login == Sign_up and password == password_Reg:
    print("\nВы успешно вошли в свой аккаунт 'VladProjects'")
else:
    print("Неверный пароль или логин!")
    input("Чтобы выйти нажмите Enter: ")
    exit()
#end Log-in


#Система стоимости
cost = 0 #intenger

#Система поиска и покупки
print("\nЧтобы найти товары введите в поиске категории, указанные ниже")
categories = ["Цифровая техника", "Бытовая техника", "книги"]
print(categories)


search =input("\nВведите поисковой запрос: ")

if search == "цифровая техника":
    print("По данному запросу найдено: ")
    print(["Iphone 11 pro|37.999/1641/", "Xiaomi Mi 11t|23.400/342/", "Iphone 15|106.000/712/", "Iphone 15 pro|125.000/732/"])
elif search == "бытовая техника":
    print("По данному запросу найдено: ")
    print(["Стиральная машина Beko|36.000/120/", "Духовой шкаф Hotpoint|56.000/134/", "Пылесос Electrolux|32.000/142/"])
elif search == "книги" :
    print("По данному запросу найдено: ")
    print(['Майкл Доусонов "Програмируем на пайтон"/100/|793'])
else:
    print("Неккоректная категория")
    input("Чтобы выйти нажмите Enter ")
    exit()


bucket = input("Введите индекс товара. Пример(/000/): ")


if int(bucket) == 100:
    print("Вы добавили в корзину товар - Майкл Доусонов 'Програмируем на пайтон'")
    print(f"Итого {793 + cost}рублей")
    cost = 793
elif int(bucket) == 732:
    print("Вы добавили в корзину товар - Iphone 15 pro max")
    print(f"Итого {cost + 125000}Рублей")
    cost = 125000
elif int(bucket) == 712:
    print("Вы добавили в корзину товар - Iphone 15")
    print(f"Итого {cost + 106000}Рублей")
    cost = 106000
elif int(bucket) == 342:
    print("Вы добавили в корзину товар - Xiaomi Mi 11t")
    print(f"Итого {cost + 23400}Рублей")
    cost = 23400
elif int(bucket) == 1641:
    print("Вы добавили в корзину товар - Iphone 11 pro")
    print(f"Итого {cost + 37999}Рублей")
    cost = 37999
elif int(bucket) == 120:
    print("Вы добавили в корзину товар - Стиральная машина Beko")
    print(f"Итого {cost + 36000}Рублей")
    cost = 36000
elif int(bucket) == 134:
    print("Вы добавили в корзину товар - Духовой шкаф Hotpoint")
    print(f"Итого {cost + 56000}Рублей")
    cost = 56000
elif int(bucket) == 142:
    print("Вы добавили в корзину товар - Пылесос Electrolux")
    print(f"Итого {cost + 32.000}Рублей")
    cost = 32000
else:
    print("Неверный индекс")
    input("Нажмите Enter чтобы выйти: ")
    exit()
#end
#Cистема выдачи чека
def check(username, cost, email, adress):
    return f"\n\n{"-" * 10}Электронный чек:{"-" * 10}\nИмя получателя {username}\nПокупка произведена на MY.SHOP.RU\nИтого: {cost}\nЭл.адрес: {email}.\nАдрес доставки: {adress}\nСпасибо за покупку!\n{"-" * 36}"
#Конец функции

buy = input("Чтобы начать оформление заказа нажмите 1, если нет то любую клавишу: ")

if int(buy) == 1:
    print("\nЧтобы оформить заказ укажите данные ниже: ")
    name = input("Ваше имя: ")
    elmail = input("Ваша эл.почта: ")
    adress = input("Адрес доставки: ")
    input("Чтобы продолжить нажмите Enter ")
    print(check(name, cost, elmail, adress))
else:
    print("оформление заказа было успешно отменено!")
    input("Нажмите Enter для выхода")
    exit()