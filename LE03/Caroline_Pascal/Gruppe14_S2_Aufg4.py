import matplotlib.pyplot as plt

def find_machine_epsilon():
    eps = 1.0
    while (1.0 + eps) != 1.0:
        eps /= 2.0
    return eps * 2.0

def find_max_positive_machine_number():
    q = 1.0
    while (q * 2.0) > q:
        q *= 2.0
    return q / 2.0

eps = find_machine_epsilon()
qmin = find_max_positive_machine_number()

print(f"Maschinengenauigkeit (eps): {eps}")
print(f"grösstmögliche positive Maschinenzahl (qmin): {qmin}")

# Plotting
values = [eps, qmin]
labels = ['eps', 'qmin']

plt.figure(figsize=(10, 6))
plt.bar(labels, values, color=['blue', 'green'])
plt.yscale('log')
plt.ylabel('Value (log scale)')
plt.title('Maschinengenauigkeit (eps) und grösstmögliche positive Maschinenzahl (qmin)')
plt.grid(True, which="both", ls="--")
plt.show()