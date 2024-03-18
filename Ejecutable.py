import math

# Coeficientes de la ecuación
A = 3
B = -1
C = -2

# Calcular el discriminante
discriminante = B**2 - 4*A*C

# Verificar si hay soluciones reales
if discriminante < 0:
    print("La ecuación no tiene soluciones reales (números complejos).")
else:
    # Calcular las raíces
    raiz_discriminante = math.sqrt(discriminante)
    x1 = (-B + raiz_discriminante) / (2*A)
    x2 = (-B - raiz_discriminante) / (2*A)
    print("Las soluciones de la ecuación son:")
    print(f"x1 = {x1}")
    print(f"x2 = {x2}")
