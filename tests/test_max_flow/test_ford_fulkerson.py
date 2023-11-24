import pytest

from flowprog.max_flow import EdmonsKarpAlgorithm, FordFulkersonAlgorithm
from tests.test_max_flow.problems import PROBLEMS, MaxFlowProblem


@pytest.mark.parametrize("problem", PROBLEMS)
def test_ford_fulkerson(problem: MaxFlowProblem):
    ford_fulkerson = FordFulkersonAlgorithm()
    max_flow, residual_graph = ford_fulkerson(
        problem.graph, problem.source, problem.sink
    )
    assert max_flow == problem.max_flow


@pytest.mark.parametrize("problem", PROBLEMS)
def test_edmons_karp(problem: MaxFlowProblem):
    edmons_karp = EdmonsKarpAlgorithm()
    max_flow, residual_graph = edmons_karp(problem.graph, problem.source, problem.sink)
    assert max_flow == problem.max_flow
