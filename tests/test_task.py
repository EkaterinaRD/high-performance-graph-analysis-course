import pytest
from pygraphblas import Matrix
from pygraphblas.types import BOOL
from project.bfs import bfs, multi_bfs

@pytest.mark.parametrize("I, J, V, start_v, extected", 
[
    (   
        [0, 0, 0, 0, 0, 1, 1, 2, 3, 4, 5, 5, 5, 6, 6, 7, 7],
        [1, 2, 3, 4, 5, 2, 4, 3, 4, 5, 2, 6, 7, 5, 7, 5, 6],
        [True] * 17,
        0,
        [[0, 1, 2, 3, 4, 5, 6, 7], [0, 1, 1, 1, 1, 1, 2, 2]] 
    ),
    (
        [0, 0, 0, 0, 0, 1, 1, 2, 3, 4, 5, 5, 5, 6, 6, 7, 7],
        [1, 2, 3, 4, 5, 2, 4, 3, 4, 5, 2, 6, 7, 5, 7, 5, 6],
        [True] * 17,
        1,
        [[1, 2, 3, 4, 5, 6, 7], [0, 1, 2, 1, 2, 3, 3]]
    ),
    (
        [0, 0, 0, 0, 0, 1, 1, 2, 3, 4, 5, 5, 5, 6, 6, 7, 7],
        [1, 2, 3, 4, 5, 2, 4, 3, 4, 5, 2, 6, 7, 5, 7, 5, 6],
        [True] * 17,
        2,
        [[2, 3, 4, 5, 6, 7], [0, 1, 2, 3, 4, 4]]
    ),
    (
        [0],
        [0],
        [True],
        0,
        [[0],[0]]
    )
])
def test_bfs (I, J, V, start_v, extected):
    M = Matrix.from_lists(I, J, V)
    assert bfs(M, start_v) == extected

def test_not_square_bfs():
    M = Matrix.sparse(BOOL, nrows = 3, ncols = 11)
    with pytest.raises(ValueError):
        bfs(M, 1)

def test_incorrect_v_bfs():
    M = Matrix.sparse(BOOL, nrows = 3, ncols = 3)
    with pytest.raises(ValueError):
        bfs(M, 5)
    
@pytest.mark.parametrize("I, J, V, start_vs, extected",
[
    (
        [0, 0, 0, 0, 0, 1, 1, 2, 3, 4, 5, 5, 5, 6, 6, 7, 7],
        [1, 2, 3, 4, 5, 2, 4, 3, 4, 5, 2, 6, 7, 5, 7, 5, 6],
        [True] * 17,
        [0, 1, 2],
        [
            (0, [[0, 1, 2, 3, 4, 5, 6, 7], [0, 1, 1, 1, 1, 1, 2, 2]]),
            (1, [[1, 2, 3, 4, 5, 6, 7], [0, 1, 2, 1, 2, 3, 3]]),
            (2, [[2, 3, 4, 5, 6, 7], [0, 1, 2, 3, 4, 4]])
        ]
    ),
    (
        [0],
        [0],
        [True],
        [0],
        [(0,[[0],[0]])]
    ),
    (
        [0, 0, 1, 2],
        [1, 1, 2, 0],
        [True] * 4,
        [2, 1],
        [
            (2, [[0, 1, 2], [1, 2, 0]]),
            (1, [[0, 1, 2], [2, 0, 1]])
        ]
    )
])
def test_multi_bfs(I, J, V, start_vs, extected):
    M = Matrix.from_lists(I, J, V)
    assert multi_bfs(M, start_vs) == extected
    
def test_not_square_multi_bfs():
    M = Matrix.sparse(BOOL, nrows = 3, ncols = 11)
    with pytest.raises(ValueError):
        bfs(M, 1)

def test_incorrect_v_multi_bfs():
    M = Matrix.sparse(BOOL, nrows = 3, ncols = 3)
    with pytest.raises(ValueError):
        bfs(M, 5)
    
    
    
    
    
    
    
    
    
    
