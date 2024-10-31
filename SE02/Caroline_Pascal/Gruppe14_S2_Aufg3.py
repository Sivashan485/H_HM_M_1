import matplotlib.pyplot as plt
import numpy as np

def s2n(n):
  """
  Berechnet die Seitenlänge eines Vielecks mit 2n Ecken, das in einen Einheitskreis eingeschrieben ist.

  Args:
    n: Die Anzahl der Ecken des Vielecks (n >= 3).

  Returns:
    Die Seitenlänge des Vielecks.
  """
  return np.sqrt(2 - 2 * np.sqrt(1 - (1/4) * (np.sin(np.pi/n)**2)))

def sum_seitenlaenge(n):
  """
  Berechnet die Summe der Seitenlängen eines Vielecks mit 2n Ecken, das in einen Einheitskreis eingeschrieben ist.

  Args:
    n: Die Anzahl der Ecken des Vielecks (n >= 3).

  Returns:
    Die Summe der Seitenlängen.
  """
  return 2 * n * s2n(n)

# Berechne die Summe der Seitenlängen für verschiedene Werte von n
n_values = np.arange(3, 20, 1)
sum_seitenlaenge_values = [sum_seitenlaenge(n) for n in n_values]

# Plotte die Ergebnisse
plt.plot(2 * n_values, sum_seitenlaenge_values, 'o-')
plt.xlabel('Anzahl der Ecken (2n)')
plt.ylabel('Summe der Seitenlängen')
plt.title('Approximation von 2π durch die Summe der Seitenlängen von Vielecken')
plt.grid(True)
plt.show()

# Berechne 2π mit der neuen Formel
a = 1 + np.sqrt(1 - (1/4) * (np.sin(np.pi/6)**2))
b = 1 - np.sqrt(1 - (1/4) * (np.sin(np.pi/6)**2))
two_pi_approx = 2 * 6 * (a - b) / (a + b)
print('Approximation von 2π mit der neuen Formel:', two_pi_approx)