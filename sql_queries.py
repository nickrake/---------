import sqlite3

connection = sqlite3.connect("Artists.db")



# Запитання 1. Інформація про скількох художників представлена у базі даних?
cursor = connection.cursor()
cursor.execute('''SELECT Name FROM artists''')

data = cursor.fetchall()
print(len(data))

# Запитання 2. Скільки жінок (Female) у базі?
cursor.execute('''SELECT Name FROM artists WHERE Gender = "Female"''')

data = cursor.fetchall()
print(len(data))

# Запитання 3. Скільки людей у базі даних народилися до 1900 року?


# Запитання 4. Додати в базу даних ще двох художників

# Запитання 5. Надрукувати список усіх художників з Швеції (Swedish)


# Додаткове завдання* Як звати  наймолодшого художника?
