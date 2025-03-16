import math
import random
import matplotlib.pyplot as plt
import numpy as np

h = 100
v0 = 50
g = 9.81

target_distance = random.randint(50, 340)
print(f"Cel został wylosowany w odległości: {target_distance} metrów")

attempts = 0

while True:
    angle = float(input("Podaj kąt strzału w stopniach: "))
    angle_rad = math.radians(angle)

    distance = (v0 * math.sin(angle_rad) + 
                math.sqrt(v0**2 * math.sin(angle_rad)**2 + 2 * g * h)) * \
               (v0 * math.cos(angle_rad) / g)

    attempts += 1

    if target_distance - 5 <= distance <= target_distance + 5:
        print(f"Cel trafiony! Liczba prób: {attempts}")
        break
    else:
        print(f"Chybiony! Pocisk trafił w odległość: {distance:.2f} metrów.")


angle_rad = np.radians(angle) 

t_flight = (v0 * np.sin(angle_rad) + 
             np.sqrt(v0**2 * np.sin(angle_rad)**2 + 2 * g * h)) / g

t = np.linspace(0, t_flight, num=500)

x = v0 * np.cos(angle_rad) * t
y = h + v0 * np.sin(angle_rad) * t - 0.5 * g * t**2

plt.figure(figsize=(10, 5))
plt.plot(x, y, color='blue')
plt.title('Trajektoria pocisku Warwolf')
plt.xlabel('Odległość (m)')
plt.ylabel('Wysokość (m)')
plt.grid()
plt.xlim(0, max(x) + 10)
plt.ylim(0, max(y) + 10)

plt.savefig('trajektoria1.png')
plt.show()