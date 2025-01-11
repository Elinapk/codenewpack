""" Projekt Fizyka

--

Prosta symulacja zjawiska fizycznego.

Wybrano rzut ukośny. Ponieważ jest to jedno z zagadnień mechaniki klasycznej.
Zasymuluję tutaj ruch obiektu rzucanego pod kontem Theta z prędkością
początkową v0 przy jednoczenym uwzględnieniu przyspieszenia ziemskiego g.
Wyrysowana zostanie trajektoria ruchu na wykresie, a także obliczony maksymalny
zasięg, wysokość oraz czas lotu.



Funkcja:
-oblicza: trajektorię, czas lotu, zasięg oraz maksymalna wysokośc na podstawie
równań ruchu w rzucie ukośnym.
-zwraca także wartości niezbedne do jego anlizy oraz wykresu.

Wzory z załaczeniu.

Użytkownik podaje parametry takie jak: predkość początkową v0
oraz kat rzutu theta.
matplotlib- czyli biblioteka do tworzenia wykresów rysuje trajektorię
na podstawie x i y, z czytelnym tytułem, siatką oraz osią.

Instrukcja:
Proszę o skopiowanie kodu rzut_ukosny.py i uruchomienie go w Python 3,
ważne fragmenty wytłumaczone w komentarzach oraz opisie.

Na podstawie wprowadzonych danych wykres pokaże trajektorię rzutu ukośnego
w układzie współrzędnych.

--

wykonawca Ewelina Pępek

"""
import numpy as np
import matplotlib.pyplot as plt

def rzut_ukosny(v0, theta, g=9.81):
    """
    Oblicza trajektorię ruchu w rzucie ukośnym.
    :param v0: Prędkość początkowa [m/s]
    :param theta: Kąt rzutu [stopnie]
    :param g: Przyspieszenie ziemskie [m/s^2]
    :return: Czas lotu, zasięg, maksymalna wysokość, punkty trajektorii
    """
    # Przeliczamy kąt na radiany
    theta_rad = np.radians(theta)
    
    # Czas lotu
    t_lotu = 2 * v0 * np.sin(theta_rad) / g
    
    # Zasięg
    zasięg = v0 * np.cos(theta_rad) * t_lotu
    
    # Maksymalna wysokość
    max_h = (v0 ** 2) * (np.sin(theta_rad) ** 2) / (2 * g)
    
    # Trajektoria
    t = np.linspace(0, t_lotu, num=500)
    x = v0 * np.cos(theta_rad) * t
    y = v0 * np.sin(theta_rad) * t - 0.5 * g * t ** 2
    
    return t_lotu, zasięg, max_h, x, y

def main():
    print("Symulacja rzutu ukośnego")
    
    # Pobieranie danych wejściowych od użytkownika
    try:
        v0 = float(input("Podaj prędkość początkową (m/s): "))
        theta = float(input("Podaj kąt rzutu (°): "))
        if v0 <= 0 or not (0 <= theta <= 90):
            raise ValueError("Nieprawidłowe dane wejściowe.")
    except ValueError as e:
        print(f"Błąd: {e}")
        return
    
    # Obliczenia
    t_lotu, zasięg, max_h, x, y = rzut_ukosny(v0, theta)
    
    # Wyświetlenie wyników
    print("\nWyniki symulacji:")
    print(f"- Czas lotu: {t_lotu:.2f} s")
    print(f"- Zasięg: {zasięg:.2f} m")
    print(f"- Maksymalna wysokość: {max_h:.2f} m")
    
    # Wizualizacja
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label=f"Trajektoria (v0={v0} m/s, θ={theta}°)")
    plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
    plt.title("Symulacja rzutu ukośnego")
    plt.xlabel("Odległość [m]")
    plt.ylabel("Wysokość [m]")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
