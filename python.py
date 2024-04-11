import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('odessa.csv')

# Вибираємо тип графіка
plt.bar(data['tempMin'], data['infoMonth'])

# Налаштовуємо вісь X
plt.xlabel('Дата')

# Налаштовуємо вісь Y
plt.ylabel('Температура (°C)')

# Додаємо заголовок
plt.title('Графік даних про температуру')

# Відображаємо графік
plt.show()