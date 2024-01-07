import pytest

from flowprog.min_cost import (CycleCancelingAlgorithm)
from tests.test_min_cost.problems import PROBLEMS, MinCostProblem


@pytest.mark.parametrize("problem", PROBLEMS)
def test_successive_shortest_path(problem: MinCostProblem):
    pass


@pytest.mark.parametrize("problem", PROBLEMS)
def test_cycle_canceling(problem: MinCostProblem):
    cycle_canceling_algo = CycleCancelingAlgorithm()
    cost, flow_network = cycle_canceling_algo(
        problem.graph,
        problem.source,
        problem.sink,
        problem.flow,
    )
    assert cost == problem.min_cost


if __name__ == "__main__":
    test_cycle_canceling(PROBLEMS[0])
