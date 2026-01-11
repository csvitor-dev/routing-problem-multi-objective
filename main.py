""" 
TRABALHO DE PROJETO E ANÁLISE DE ALGORITMOS

Equipe:
    - Jona Ferreira de Sousa (539700) [ES]
    - Vitor Costa de Sousa (536678) [ES]
"""

from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.operators.crossover.sbx import SBX
from pymoo.operators.mutation.pm import PM
from pymoo.optimize import minimize
import matplotlib.pyplot as plt
from lib.cmd import pluck_flags_from_cmd_args
from utils.plot_graph import plot_vrp_instance
from src.parser.domain_mapper import get_instance
from src.domain.domain_problem import DomainProblem


def app() -> None:
    flags = pluck_flags_from_cmd_args(
        search_for=['instance', 'plot', 'generate-result'])

    instance = get_instance(flags['instance'])

    if flags['plot']:
        plot_vrp_instance(instance, flags['instance'])

    problem = DomainProblem(instance)
    algorithm = NSGA2(
        pop_size=100,
        crossover=SBX(prob=0.9, eta=15),
        mutation=PM(prob=0.2, eta=20),
        eliminate_duplicates=True
    )

    res = minimize(
        problem,
        algorithm,
        ('n_gen', 200),
        seed=1,
    )

    if flags['generate-result']:
        plt.scatter(res.F[:, 0], res.F[:, 1])
        plt.xlabel("Distância total")
        plt.ylabel("Makespan")
        plt.savefig(f"./resources/output/result-{flags['instance']}.png")


if __name__ == "__main__":
    app()
