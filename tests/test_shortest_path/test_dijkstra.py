import pytest

from flowprog.shortest_path import DijkstrasAlgorithm
from tests.test_shortest_path.dijkstra_problems import (PROBLEMS,
                                                        ShortestPathProblem)


@pytest.mark.parametrize("problem", PROBLEMS)
def test_dijkstra(problem: ShortestPathProblem):
    dijkstra = DijkstrasAlgorithm()
    dijkstra_path_found = dijkstra(problem.graph, problem.start, problem.end)
    assert dijkstra_path_found == problem.shortest_path
