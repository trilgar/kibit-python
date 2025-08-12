# Практичне завдання — GroupBy & Aggregation («Кав'ярні міста»)

**Мета:** закріпити роботу з `GroupBy` (split–apply–combine): прості й ієрархічні групування, кілька агрегатів, власні функції, ітерація по групах, робота з квантилями, додавання префіксів до назв колонок.

---

## 0) Створення даних (запустіть як є)

```python
import numpy as np
import pandas as pd

np.random.seed(7)

cities   = ['Kyiv','Kyiv','Kyiv','Lviv','Lviv','Lviv','Odesa','Odesa','Odesa','Kyiv','Lviv','Odesa']
shops    = ['K1','K1','K2','L1','L2','L2','O1','O1','O2','K2','L1','O2']
products = ['espresso','latte','croissant','espresso','tea','croissant','latte','espresso','tea','tea','latte','croissant']
category_map = {'espresso':'drink','latte':'drink','tea':'drink','croissant':'food'}
price_map    = {'espresso':2.50,'latte':3.80,'tea':1.90,'croissant':2.20}

qty = np.random.randint(10, 50, size=len(products))

sales = pd.DataFrame({
    'city': cities,
    'shop': shops,
    'product': products,
    'category': [category_map[p] for p in products],
    'price': [price_map[p] for p in products],
    'qty': qty
})

sales
```

> У таблиці кожен рядок — агрегований запис продажів для комбінації (місто, заклад, продукт).

---

## 1) Розігрів

**Завдання:** додайте колонку `revenue = price * qty` і виведіть перші 5 рядків.
*Підказка методів:* звичайна векторна операція над стовпцями.

---

## 2) Базова агрегація за одним ключем

**Завдання:** згрупуйте за `city` та порахуйте:

* загальну кількість одиниць (`qty`) та загальний дохід (`revenue`) — сума;
* середню ціну (`price`) — середнє.

*Підказка методів:* `groupby('city')`, вибір потрібних колонок, `sum()`, `mean()`.

---

## 3) Кілька агрегатів за один прохід

**Завдання:** для кожного міста обчисліть одразу кілька показників для `price` і `revenue`:

* `mean`, `std`;
* **власну функцію** `value_range` (максимум − мінімум).

*Підказка методів:* визначте `def value_range(s): ...`; застосуйте `agg(['mean','std', value_range])` до вибраних колонок.

---

## 4) Ієрархічне групування (кілька ключів)

**Завдання:** згрупуйте за `['city','category']` і порахуйте сумарний `revenue`.

*Підказка методів:* `groupby(['city','category'])['revenue'].sum()`; зверніть увагу на багаторівневий індекс у результаті.

---

## 5) Квантилі всередині груп

**Завдання:** знайдіть **0.6-квантиль** ціни `price` окремо для кожного міста.

*Підказка методів:* `groupby('city')['price'].quantile(0.6)`.

---

## 6) Ітерація по групах

**Завдання:** для кожного міста виведіть:

* кількість унікальних продуктів;
* назву продукту з **найбільшою** кількістю проданих одиниць (`qty`).

*Підказка методів:* цикл `for name, grp in sales.groupby('city'):`; у середині `grp['product'].nunique()`, `grp.loc[grp['qty'].idxmax(), 'product']` або сортування.

---

## 7) Охайні назви колонок після агрегації

**Завдання:** побудуйте таблицю середніх значень усіх числових колонок по `city` і додайте префікс `mean_` до назв колонок результату.

*Підказка методів:* `sales.groupby('city').mean(numeric_only=True).add_prefix('mean_')`.

---