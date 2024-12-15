import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))


import pytest
from src.Trajectory.main import compute_forces, simulate_trajectory


def test_compute_forces():
    """ Teste le calcul des forces aérodynamiques. """
    # Test avec vitesse nulle (pas de forces)
    fx, fy = compute_forces(0, 0)
    assert fx == 0, "La force de traînée et portance devrait être nulle si la vitesse est nulle."
    assert fy == 0, "La force de traînée et portance devrait être nulle si la vitesse est nulle."

def test_simulate_trajectory():
    """ Teste la simulation de trajectoire. """
    # Récupération des résultats de la simulation
    x_positions, y_positions, times = simulate_trajectory()

    # Vérifie que les positions et les temps ne sont pas vides
    assert len(x_positions) > 0, "La liste des positions x ne doit pas être vide."
    assert len(y_positions) > 0, "La liste des positions y ne doit pas être vide."
    assert len(times) > 0, "La liste des temps ne doit pas être vide."

    # Vérifie que la fusée commence au sol
    assert x_positions[0] == 0, "La position initiale en x doit être 0."
    assert y_positions[0] == 0, "La position initiale en y doit être 0."

    # Vérifie que l'altitude revient à zéro ou en dessous (retombe au sol)
    assert y_positions[-1] <= 0, "La fusée doit retomber au sol (altitude <= 0)."

    # Vérifie que le temps augmente correctement
    assert times[0] == 0, "Le temps initial doit être 0."
    assert times[-1] > times[0], "Le temps final doit être supérieur au temps initial."

if __name__ == "__main__":
    pytest.main()
