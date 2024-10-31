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


print(f"Maschinengenauigkeit (eps): {find_machine_epsilon()}")
print(f"grösstmögliche positive Maschinenzahl (qmin): {find_max_positive_machine_number()}")

