# Практичне завдання — `transform` та `apply` («Кур’єрська служба»)

**Мета:** закріпити прийоми розповсюдження групових метрик через `transform()` та узагальнену обробку підтаблиць через `apply()`.

---

## 0) Створення даних (запустіть як є)

```python
import numpy as np
import pandas as pd

np.random.seed(24)

n = 48
cities   = np.random.choice(['Kyiv','Lviv','Odesa'], size=n)
couriers = np.random.choice(['C1','C2','C3'], size=n)
package_id = np.arange(1001, 1001+n)

# ваги посилок (кг) і відстані (км)
weights = np.round(np.random.uniform(0.3, 12.0, size=n), 2)
dist_km = np.round(np.random.gamma(shape=2.2, scale=4.5, size=n), 2)

# ймовірність вчасної доставки трішки відрізняється між містами
p_on_time = np.where(cities=='Kyiv', 0.88, np.where(cities=='Lviv', 0.83, 0.86))
on_time = np.random.rand(n) < p_on_time

couriers_df = pd.DataFrame({
    'package_id': package_id,
    'city': cities,
    'courier': couriers,
    'weight_kg': weights,
    'distance_km': dist_km,
    'on_time': on_time
})

couriers_df.head()
```

> Кожен рядок — одна доставка. Ключі групування, які будемо використовувати: `city`, `courier`, а також пара `['city','courier']`.

---

## 1) Частка дистанції кур’єра в місті (`transform`)

**Завдання:** для кожного міста порахуйте загальну дистанцію **всіх** кур’єрів (`distance_km`), а для кожного рядка обчисліть його **частку** від міського підсумку. Додайте дві колонки: `city_distance_sum` та `city_distance_share` (останню округліть до 3 знаків).

*Методи для орієнтиру:* `groupby('city')['distance_km'].transform('sum')`.

---

## 2) Z‑score дистанції всередині кур’єра (`transform`)

**Завдання:** для груп `['city','courier']` обчисліть `zscore_distance = (distance_km - mean)/std` і додайте як нову колонку. Перевірте, що середнє `zscore_distance` в межах кожної групи ≈ 0.

*Методи:* `transform('mean')`, `transform('std')` по `groupby(['city','courier'])`.

---

## 3) Рівень вчасності на рівні міста (`transform`)

**Завдання:** створіть колонку `city_on_time_rate` — частка `on_time=True` у відповідному місті. (Потім виведіть по 3 рядки з кожного міста, щоб візуально перевірити однаковість значення в межах групи.)

*Методи:* `groupby('city')['on_time'].transform('mean')`.

---

## 4) Найважча посилка кожного кур’єра (`apply`)

**Завдання:** для кожної групи `['city','courier']` знайдіть рядок з **найбільшою** вагою (`weight_kg`). У підсумковій таблиці залиште колонки `weight_kg`, `distance_km`, `package_id`.

*Методи:* `groupby(['city','courier']).apply(lambda g: g.loc[g['weight_kg'].idxmax(), ['weight_kg','distance_km','package_id']])` (повернення `Series`).

---