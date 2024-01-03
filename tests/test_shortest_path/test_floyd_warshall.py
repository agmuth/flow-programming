import pytest

from flowprog.shortest_path import FloydWarshallAlgorithm
from tests.test_shortest_path.floyd_warshall_problems import (
    PROBLEMS, AllPairsShortestPathProblem)


@pytest.mark.parametrize("problem", PROBLEMS)
def test_floyd_warshall(problem: AllPairsShortestPathProblem):
    floy_warshall = FloydWarshallAlgorithm()
    floy_warshall(problem.graph)

    for node_from in problem.graph.nodes:
        for node_to in problem.graph.nodes:
            assert (
                floy_warshall.node_dist_mapping[node_from][node_to]
                == problem.shortest_paths[node_from][node_to]
            )


if __name__ == "__main__":
    test_floyd_warshall(PROBLEMS[0])
