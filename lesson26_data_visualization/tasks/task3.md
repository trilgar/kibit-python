# Mini-task: «Пінгвіни Палмера»

**Мета:** потренуватися будувати `scatter` і `barplot` у Seaborn на реальному датафреймі.

## Дані

Використайте вбудований датасет **`penguins`** (Seaborn автоматично його завантажить з інтернету):

```python
import seaborn as sns
penguins = sns.load_dataset("penguins")
```

## Що зробити

1. **Очистити дані** від пропусків у потрібних колонках.
   Підказка: `dropna(subset=[...])`.

2. **Scatter plot:**

   * по осі **X**: довжина дзьоба, `bill_length_mm`
   * по осі **Y**: довжина плавця, `flipper_length_mm`
   * додайте розфарбування за **видом** (`hue="species"`) і різні маркери за **статтю** (`style="sex"`).
   * підпишіть осі одиницями вимірювання (мм).

3. **Bar plot:**

   * по осі **X**: вид (`species`)
   * по осі **Y**: **середня** маса тіла (`body_mass_g`)
   * додайте `hue="sex"` та приберіть довірчий інтервал (щоб показати саме середні).
   * підпишіть вісь Y у грамах (g).

4. Оформлення: тема `whitegrid`, читабельні підписи, легенда, зрозумілі заголовки.

## Скелет коду (з пропусками — потрібно заповнити)

```python
import seaborn as sns, numpy as np
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid", palette="Set2")

penguins = sns.load_dataset("penguins")

# 0) очистка
penguins = penguins.dropna(subset=["...", "...", "..."])   # <- впишіть колонки

# 1) SCATTER
ax = sns.scatterplot(
    data=penguins,
    x="...",         # bill_length_mm
    y="...",         # flipper_length_mm
    hue="...",       # species
    style="..."      # sex
)
ax.set(xlabel="...", ylabel="...", title="...")  # додайте одиниці вимірювання
plt.show()

# 2) BARPLOT
ax = sns.barplot(
    data=penguins,
    x="...",         # species
    y="...",         # body_mass_g
    hue="...",       # sex
    estimator=np.mean, ci=None
)
ax.set(xlabel="...", ylabel="...", title="...")
plt.show()
```