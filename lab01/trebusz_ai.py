import math
import random
import matplotlib.pyplot as plt

def calculate_distance(angle, v0=50, h=100, g=9.81):
    alpha = math.radians(angle)
    distance = (v0 * math.sin(alpha) + math.sqrt(v0**2 * math.sin(alpha)**2 + 2 * g * h)) * (v0 * math.cos(alpha) / g)
    return distance

def trajectory_points(angle, v0=50, h=100, g=9.81, num_points=100):
    alpha = math.radians(angle)
    vx = v0 * math.cos(alpha)
    vy = v0 * math.sin(alpha)
    
    t_flight = (vy + math.sqrt(vy**2 + 2 * g * h)) / g
    t_values = [t_flight * i / num_points for i in range(num_points + 1)]
    
    x_values = [vx * t for t in t_values]
    y_values = [h + vy * t - 0.5 * g * t**2 for t in t_values]
    
    return x_values, y_values

def plot_trajectory(angle):
    x_values, y_values = trajectory_points(angle)
    
    plt.figure(figsize=(10, 5))
    plt.plot(x_values, y_values, 'b', label='Trajektoria pocisku')
    plt.xlabel('Odległość (m)')
    plt.ylabel('Wysokość (m)')
    plt.title('Trajektoria pocisku Warwolf')
    plt.grid()
    plt.savefig('trajektoria.png')
    plt.show()

def main():
    target_distance = random.randint(50, 340)
    print(f"Cel znajduje się w odległości {target_distance} metrów.")
    attempts = 0
    
    while True:
        try:
            angle = float(input("Podaj kąt strzału (w stopniach): "))
        except ValueError:
            print("Proszę podać poprawną wartość liczbową!")
            continue
        
        attempts += 1
        shot_distance = calculate_distance(angle)
        print(f"Pocisk upadł w odległości {shot_distance:.2f} metrów.")
        
        if abs(shot_distance - target_distance) <= 5:
            print(f"Cel trafiony! Liczba prób: {attempts}")
            plot_trajectory(angle)
            break
        else:
            print("Chybiony! Spróbuj ponownie.")

if __name__ == "__main__":
    main()
