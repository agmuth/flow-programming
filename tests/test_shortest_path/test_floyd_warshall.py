import pytest

from flowprog.shortest_path import FloydWarshallAlgorithm
from tests.test_shortest_path.all_pairs_shortest_path_problems import \
    PROBLEMS as ALL_PAIRS_SHORTEST_PATH_PROBLEMS
from tests.test_shortest_path.all_pairs_shortest_path_problems import \
    AllPairsShortestPathProblem
from tests.test_shortest_path.negative_cycle_problems import \
    PROBLEMS as NEGATIVE_CYCLE_PROBLEMS
from tests.test_shortest_path.negative_cycle_problems import \
    NegativeCycleProblem
from tests.test_shortest_path.shortest_path_problems import \
    PROBLEMS as SHORTEST_PATH_PROBLEMS
from tests.test_shortest_path.shortest_path_problems import ShortestPathProblem


@pytest.mark.parametrize("problem", ALL_PAIRS_SHORTEST_PATH_PROBLEMS)
def test_all_pairs_shortest_path(problem: AllPairsShortestPathProblem):
    floyd_warshall = FloydWarshallAlgorithm()
    floyd_warshall(problem.graph)

    for node_from in problem.graph.nodes:
        for node_to in problem.graph.nodes:
            assert (
                floyd_warshall.node_dist_mapping[node_from][node_to]
                == problem.shortest_paths[node_from][node_to]
            )


@pytest.mark.parametrize("problem", SHORTEST_PATH_PROBLEMS)
def test_shortest_path(problem: ShortestPathProblem):
    floyd_warshall = FloydWarshallAlgorithm()
    floyd_warshall(problem.graph)
    floyd_warshall_path_found = floyd_warshall.path(problem.start, problem.end)
    assert floyd_warshall_path_found == problem.shortest_path


@pytest.mark.parametrize("problem", NEGATIVE_CYCLE_PROBLEMS)
def test_find_negative_cycles(problem: NegativeCycleProblem):
    floyd_warshall = FloydWarshallAlgorithm()
    floyd_warshall(problem.graph)
    floyd_warshall_negative_cycles_found = floyd_warshall.get_negative_cycles()

    for cycle1 in floyd_warshall_negative_cycles_found:
        for cycle2 in problem.negative_cycles:
            if set(cycle1) != set(cycle2):
                continue
            if len(cycle1) != len(cycle2):
                assert False

            n = len(cycle1)
            idx2 = cycle2.index(cycle1[0])
            for idx1 in range(n):
                assert cycle1[idx1] == cycle2[(idx1 + idx2) % n]
            break

        else:
            assert False
