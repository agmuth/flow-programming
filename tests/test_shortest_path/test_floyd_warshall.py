import pytest

from flowprog.shortest_path import FloydWarshallAlgorithm
from tests.test_shortest_path.dijkstra_problems import \
    PROBLEMS as DIJKSTRA_PROBLEMS
from tests.test_shortest_path.dijkstra_problems import ShortestPathProblem
from tests.test_shortest_path.floyd_warshall_problems import \
    PROBLEMS as FLOYD_WARSHAL_PPROBLEMS
from tests.test_shortest_path.floyd_warshall_problems import \
    AllPairsShortestPathProblem


@pytest.mark.parametrize("problem", FLOYD_WARSHAL_PPROBLEMS)
def test_all_pairs_shortest_path(problem: AllPairsShortestPathProblem):
    floyd_warshall = FloydWarshallAlgorithm()
    floyd_warshall(problem.graph)

    for node_from in problem.graph.nodes:
        for node_to in problem.graph.nodes:
            assert (
                floyd_warshall.node_dist_mapping[node_from][node_to]
                == problem.shortest_paths[node_from][node_to]
            )


@pytest.mark.parametrize("problem", DIJKSTRA_PROBLEMS)
def test_shortest_path(problem: ShortestPathProblem):
    floyd_warshall = FloydWarshallAlgorithm()
    floyd_warshall(problem.graph)
    floyd_warshall_path_found = floyd_warshall.path(problem.start, problem.end)
    assert floyd_warshall_path_found == problem.shortest_path


if __name__ == "__main__":
    test_shortest_path(DIJKSTRA_PROBLEMS[0])
