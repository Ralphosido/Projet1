# Initialisation des variables

F = 10000  # en N
E = 210  # en GPa = 10^3 N/mm^2
L = 100  # en mm
b = 10  # en mm
h = 20  # en mm

# Calcul de l'inertie

I = (h*b^3)/12

# Calcul de la déformation maximale

delta_max = (F*L^3)/(3*E)
delta_max = round(delta_max, 2)
print("la déformation de la poutre est de",(delta_max),"mm")

