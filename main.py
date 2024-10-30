import numpy as np
import pandas as pd

# 1. Massiv yaratish
array_1d = np.array([1, 2, 3, 4, 5])
array_2d = np.array([[1, 2, 3], [4, 5, 6]])

# 2. Matematik operatsiyalar
sum_array = np.sum(array_1d)
mean_array = np.mean(array_1d)
product_array = np.prod(array_1d)

print("1D Massiv:", array_1d)
print("2D Massiv:\n", array_2d)
print("Massivlar yig'indisi:", sum_array)
print("O'rtacha:", mean_array)
print("Ko'paytma:", product_array)

# DataFrame yaratish
data = {
    'Ism': ['Ozodbek', 'Joxongir', 'Azizbek', 'Shaxodat'],
    'Yoshi': [31, 18, 37, 43],
    'Shahar': ['Andijon', 'Quva', 'Fargona', 'Toshkent']
}
df = pd.DataFrame(data)

# Ma'lumotlarni ko'rish
print(df)

# Filtrlash
young_people = df[df['Yoshi'] < 30]
print("30 yoshdan kichiklar:\n", young_people)

# O'zgartirish
df['Yoshi'] += 1  # Har bir shaxsning yoshini 1 ga oshirish
print("Yangilangan DataFrame:\n", df)

# Fargona shahridagi shaxslarni filtrlash
fargona_people = df[df['Shahar'] == 'Fargona']
print("Fargona shahridagi shaxslar:\n", fargona_people)

# DataFrame ni CSV formatida saqlash
df.to_csv('data.csv', index=False)
