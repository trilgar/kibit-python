# Практична робота: «Стрітфуд-фест — трансформація даних»

## 0) Стартові дані (скопіюйте й запустіть як є)

```python
import numpy as np
import pandas as pd

np.random.seed(7)

menu = pd.DataFrame({
    "dish": ["taco", "ramen", "falafel", "taco", "pierogi", "gelato", "falafel"],
    "cuisine": ["mex", "jpn", "me", "mex", "pl", "it", "me"],
    "label": ["veggie", "picante", "vegano", "piccante", "mięsne", "dolce", "vegetarian"],
    "base_price": [5.0, 9.5, 7.0, 5.0, 6.0, 4.5, 7.0]
})

popularity = pd.Series([4.2, np.nan, 3.8, 4.2, 4.0, np.nan, 3.8], name="popularity")
```

---

## 1) Дублікати

1. Порахуйте кількість дубльованих рядків у `menu` (використати: `DataFrame.duplicated().sum()`).
2. Виведіть тільки дублікати як окрему таблицю (використати фільтрацію `menu[menu.duplicated()]`).
3. Створіть версію без дублікатів (використати: `DataFrame.drop_duplicates()`).

Коротко поясніть, чому обрали саме такі правила дублювання.

---

## 2) Заміна значень (нормалізація міток)

1. Нормалізуйте колонку `label` за власним словником:
   - vegano, vegetarian, veggie → vegetarian
   - picante, piccante → spicy
   - mięsne → meat, dolce → dessert

   Використати: `Series.replace(mapping)` на `menu["label"]`.

2. Перевірте результат (використати: `Series.unique()` або `value_counts()`).

---

## 3) Заміна пропусків у Series

1. Замініть NaN у `popularity` на 0 (використати: `Series.replace(np.nan, 0)`).
2. Додайте серію як колонку до `menu` (використати: звичайне присвоєння `menu["popularity"] = ...`).

---

## 4) Додавання значень за словником

1. Створіть словник сервісної націнки за кухнею (власні значення).
```python
service_fee_dict = {"mex": 1.5, "jpn": 2.0, "me": 1.0, "pl": 0.8, "it": 1.2}
```
2. Додайте колонку `service_fee` із цього словника (використати: `Series.map()` на `menu["cuisine"]`).
3. Створіть колонку `final_price = base_price + service_fee` (звичайна арифметика над колонками).

---

## 5) Перейменування міток

1. Перейменуйте колонку `dish` → `item` (використати: `DataFrame.rename(columns={...})`).
2. Перейменуйте індекси 0...N у формат `r001, r002, …` (використати: `DataFrame.rename(index=mapping_dict)` або створення словника через `enumerate`).
3. Зробіть точкове перейменування в один рядок: лише `base_price` → `price_base` (використати: `rename(columns={...})`).

---

