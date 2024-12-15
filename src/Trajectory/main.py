import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 9.81  # Gravité (m/s²)
RHO = 1.225  # Masse volumique de l'air au niveau de la mer (kg/m³)

# Paramètres physiques de l'objet
CD = 0.5  # Coefficient de traînée (hypothèse fusée/missile)
CL = 0.2  # Coefficient de portance
AREA = 0.1  # Section transversale de la fusée (m²)
MASS = 50.0  # Masse de la fusée (kg)

# Conditions initiales
initial_velocity = 300.0  # Vitesse initiale (m/s)
launch_angle = 45.0  # Angle de lancement (en degrés)
time_step = 0.01  # Pas de temps (s)
max_time = 60  # Durée maximale de la simulation (s)