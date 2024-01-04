import pytest

from flowprog.min_cost import CycleCancelingAlgorithm, SuccessiveShortestPathAlgorithm
from tests.test_min_cost.problems import PROBLEMS, MinCostProblem


@pytest.mark.parametrize("problem", PROBLEMS)
def test_successive_shortest_path(problem: MinCostProblem):
    pass


@pytest.mark.parametrize("problem", PROBLEMS)
def test_cycle_canceling(problem: MinCostProblem):
    pass
