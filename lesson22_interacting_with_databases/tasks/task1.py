"""
Завдання 1:
«Смаки кави» — PostgreSQL + pandas

Підготовка середовища
1. Завантажте й запустіть Docker-контейнер з PostgreSQL.

docker run --name cafe_pg -e POSTGRES_USER=user \
  -e POSTGRES_PASSWORD=pass -p 5433:5432 -d postgres

2. Встановіть psycopg2-binary та sqlalchemy (якщо ще не встановлено).
3. Створіть engine і підключіться до бази даних що створили в попередньому пункті.
4. Використовуючи pandas, завантажте csv-файл coffe_ratings.csv з смаками кави (використовуючи функцію read_csv) у DataFrame.
5. Отриманий DataFrame збережіть у базу даних (таблицю назвіть 'coffee_flavors').
6. За допомогою pd.read_sql_query виведіть середні значення деяких колонок (наприклад, AVG(total_cup_points)).
7. Відсортуйте таблицю за grading date та виведіть перші 10 записів.
"""

import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv('coffe_ratings.csv')
print(df.head())

engine = create_engine('postgresql://user:pass@localhost:5433/postgres')
df.to_sql('coffee_flavors', engine)

print(pd.read_sql_query("SELECT AVG(total_cup_points) FROM coffee_flavors", engine))

print(pd.read_sql_query("SELECT * FROM coffee_flavors ORDER BY grading_date LIMIT 10", engine))
