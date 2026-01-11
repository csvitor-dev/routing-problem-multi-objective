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
from lib.cmd import pluck_flags_from_cmd_args
from utils.plot import plot_vrp_instance, plot_pareto_frontier, plot_solution_routes
from src.parser.domain_mapper import get_instance
from src.domain.domain_problem import DomainProblem
from src.domain.vrp_notation import VrpNotation
from src.support.solution import knee_point


def show_input(vrp: VrpNotation) -> None:
    print("=" * 35)
    print("Input Data")
    print("=" * 35, end="\n\n")

    print("Nodes:", vrp.nodes)
    print("Demand:", vrp.demands, end="\n\n")
    print("-" * 35, end="\n\n")


def app() -> None:
    flags = pluck_flags_from_cmd_args(
        search_for=['instance', 'plot', 'generate-result'])

    instance = get_instance(flags['instance'])
    show_input(instance)

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
    routes = problem.decode(knee_point(res))

    if flags['generate-result']:
        plot_pareto_frontier(res, flags['instance'])
        plot_solution_routes(instance, routes, flags['instance'])
    print("Best choice via Knee Point:", [
          list(map(int, route)) for route in routes])


if __name__ == "__main__":
    app()
