
[![Coverage Status](https://coveralls.io/repos/github/Clementbgn/Projet_Python/badge.svg?branch=main)](https://coveralls.io/github/Clementbgn/Projet_Python?branch=main)

# Coverage obtenu sur Coverage.io
![alt text](doc/Coverage.png)

# Simulation de Trajectoire Balistique

Ce projet implémente une simulation de trajectoire balistique pour un objet (comme une fusée ou un missile), en tenant compte des forces aérodynamiques (trainée et portance). La simulation est effectuée sans correction de la direction (comme le TVC, ou "Thrust Vector Control").

## Fonctionnalités

Le programme permet de simuler la trajectoire d'un objet lancé avec une vitesse et un angle initials, en prenant en compte les forces suivantes :
- **Gravité** : Affecte l'objet en permanence pendant sa trajectoire.
- **Trainée** : Résistance de l'air qui ralentit l'objet en fonction de sa vitesse et de sa forme.
- **Portance** : Générée par l'objet en mouvement dans l'air, modifiant sa trajectoire selon les lois aérodynamiques.

Le résultat de la simulation est affiché graphiquement en utilisant `matplotlib`.

## Fichiers

- **`main.py`** : Le fichier principal contenant la logique de simulation et l'affichage des résultats.
- **`tests/test_main.py`** : Fichier contenant des tests unitaires pour vérifier le bon fonctionnement des fonctions principales.

## Fonctions Principales

### `compute_forces(vx, vy)`
Calcule les forces aérodynamiques (trainée et portance) agissant sur l'objet en fonction de ses vitesses dans les directions `x` et `y`.

#### Paramètres :
- `vx` (float) : Vitesse de l'objet dans la direction `x` (en m/s).
- `vy` (float) : Vitesse de l'objet dans la direction `y` (en m/s).

#### Retour :
- `fx` (float) : Force de trainée agissant sur l'objet dans la direction `x` (en N).
- `fy` (float) : Force de portance agissant sur l'objet dans la direction `y` (en N).

### `simulate_trajectory(initial_velocity, initial_angle, time_step, total_time)`
Simule la trajectoire balistique de l'objet en tenant compte des forces calculées par `compute_forces` et de la gravité.

#### Paramètres :
- `initial_velocity` (float) : Vitesse initiale de l'objet (en m/s).
- `initial_angle` (float) : Angle de lancement par rapport à l'horizontale (en degrés).
- `time_step` (float) : Pas de temps pour la simulation (en secondes).
- `total_time` (float) : Durée totale de la simulation (en secondes).

#### Retour :
- `time` (list) : Liste des moments (en secondes) lors de la simulation.
- `x` (list) : Liste des positions de l'objet sur l'axe `x` (en mètres).
- `y` (list) : Liste des positions de l'objet sur l'axe `y` (en mètres).

### `plot_trajectory(time, x, y)`
Affiche graphiquement la trajectoire de l'objet en fonction du temps en utilisant `matplotlib`.

#### Paramètres :
- `time` (list) : Liste des moments (en secondes) lors de la simulation.
- `x` (list) : Liste des positions de l'objet sur l'axe `x` (en mètres).
- `y` (list) : Liste des positions de l'objet sur l'axe `y` (en mètres).
