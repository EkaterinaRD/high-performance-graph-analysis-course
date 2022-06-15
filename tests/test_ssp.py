import pytest
from pygraphblas import Matrix
from pygraphblas.types import BOOL
from ssp import ssp, multi_ssp

@pytest.mark.parametrize("I, J, V, start_v, extected", 
[
    (   
        [0, 0, 1, 1, 2, 3, 3, 4, 5, 6, 6, 6],
        [1, 3, 4, 6, 5, 0, 2, 5, 2, 2, 3, 4],
        [3, 8, 1, 7, 5, 2, 4, 1, 5, 1, 5, 9],
        0,
        [0, 3, 10, 8, 4, 5, 10]
    ),
    (
        [0, 0, 1, 1, 2, 3, 3, 4, 5, 6, 6, 6],
        [1, 3, 4, 6, 5, 0, 2, 5, 2, 2, 3, 4],
        [3, 8, 1, 7, 5, 2, 4, 1, 5, 1, 5, 9],
        1,
        [14, 0, 7, 12, 1, 2, 7]
    ),
    (
        [0, 0, 1, 1, 3, 3, 6, 6, 6],
        [1, 3, 4, 6, 0, 2, 2, 3, 4],
        [3, 8, 1, 7, 2, 4, 1, 5, 9],
        2,
        [-1, -1, 0, -1, -1, -1, -1]
    ),
    (
        [0],
        [0],
        [0],
        0,
        [0]
    )
])
def test_ssp (I, J, V, start_v, extected):
    M = Matrix.from_lists(I, J, V)
    assert ssp(M, start_v) == extected

def test_not_square_ssp():
    M = Matrix.sparse(BOOL, nrows = 3, ncols = 11)
    with pytest.raises(ValueError):
        ssp(M, 1)

def test_incorrect_v_ssp():
    M = Matrix.sparse(BOOL, nrows = 3, ncols = 3)
    with pytest.raises(ValueError):
        ssp(M, 5)
    
@pytest.mark.parametrize("I, J, V, start_vs, extected",
[
    (   
        [0, 0, 1, 1, 2, 3, 3, 4, 5, 6, 6, 6],
        [1, 3, 4, 6, 5, 0, 2, 5, 2, 2, 3, 4],
        [3, 8, 1, 7, 5, 2, 4, 1, 5, 1, 5, 9],
        [0, 1, 2],
        [
            (0, [0, 3, 10, 8, 4, 5, 10]),
            (1, [14, 0, 7, 12, 1, 2, 7]),
            (2, [-1, -1, 0, -1, -1, 5, -1])
        ]
    ), 
    (
        [0, 0, 0, 2, 2, 2, 3, 4, 5],
        [1, 3, 5, 0, 3, 4, 5, 5, 4],
        [3, 2, 7, 8, 1, 4, 1, 5, 1],
        [0, 1, 2, 3, 4, 5],
        [
            (0, [0, 3, -1, 2, 4, 3]),
            (1, [-1, 0, -1, -1, -1, -1]),
            (2, [8, 11, 0, 1, 3, 2]),
            (3, [-1, -1, -1, 0, 2, 1]),
            (4, [-1, -1, -1, -1, 0, 5]),
            (5, [-1, -1, -1, -1, 1, 0])
        ]
    ),
    (
        [0, 1, 2],
        [1, 2, 0],
        [1, 2, 3],
        [2],
        [(2, [3, 4, 0])]
    )
])
def test_multi_ssp(I, J, V, start_vs, extected):
    M = Matrix.from_lists(I, J, V)
    assert multi_ssp(M, start_vs) == extected
    
def test_not_square_multi_ssp():
    M = Matrix.sparse(BOOL, nrows = 3, ncols = 11)
    with pytest.raises(ValueError):
        ssp(M, 1)

def test_incorrect_v_multi_ssp():
    M = Matrix.sparse(BOOL, nrows = 3, ncols = 3)
    with pytest.raises(ValueError):
        ssp(M, 5)
    
    
    
    
    
    
    
    
    
    
