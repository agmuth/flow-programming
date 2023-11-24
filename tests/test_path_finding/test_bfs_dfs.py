import pytest

from flowprog.path_finding import BreadthFirstSearch, DepthFirstSearch
from tests.test_path_finding.problems import PROBLEMS, PathFindingProblem


@pytest.mark.parametrize("problem", PROBLEMS)
def test_bfs(problem: PathFindingProblem):
    if problem.bfs_path:
        bfs = BreadthFirstSearch()
        bfs_path_found = bfs(
            problem.graph,
            problem.start,
            problem.end,
        )
        assert bfs_path_found == problem.bfs_path


@pytest.mark.parametrize("problem", PROBLEMS)
def test_dfs(problem: PathFindingProblem):
    if problem.dfs_path:
        dfs = DepthFirstSearch()
        dfs_path_found = dfs(
            problem.graph,
            problem.start,
            problem.end,
        )
        assert dfs_path_found == problem.dfs_path
