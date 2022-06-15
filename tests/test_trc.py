import pytest
from pygraphblas import Matrix
from pygraphblas.types import BOOL, INT64
from project.trc import trc

@pytest.mark.parametrize("I, J, V, start_v, extected", 
[
    (   
        [0, 0, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6],
        [1, 3, 0, 3, 4, 6, 3, 5, 6, 0, 1, 2, 5, 6, 1, 5, 6, 2, 3, 4, 1, 2, 3, 4],
        [True] * 24,
        0,
        [2, 6, 4, 8, 2, 2, 6] 
    ),
    (
        [0, 0, 0, 0, 1, 2, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5],
        [1, 2, 3, 5, 0, 0, 3, 4, 0, 2, 5, 2, 5, 0, 3, 4],
        [True] * 16,
        0,
        [4, 0, 2, 4, 0, 2]
    ),
    (
        [0, 0, 1, 1, 2, 2],
        [1, 2, 0, 2, 0, 1],
        [True] * 6,
        0,
        [2, 2, 2]
    ),
    (
        [0, 0, 0, 1, 2, 2, 3, 4, 4, 4, 5, 5],
        [2, 4, 5, 4, 0, 3, 2, 0, 1, 5, 0, 4],
        [True] * 12,
        0,
        [2, 0, 0, 0, 2, 2]
    )
])
def test_trc(I, J, V, start_v, extected):
    M = Matrix.from_lists(I, J, V)
    assert trc(M, start_v) == extected

def test_not_square_trc():
    M = Matrix.sparse(BOOL, nrows = 3, ncols = 11)
    with pytest.raises(ValueError):
        trc(M, 1)

def test_not_bool_type_trc():
    M = Matrix.dense(INT64, nrows = 3, ncols = 3, fill = 3)
    with pytest.raises(ValueError):
        trc(M, 1)


@pytest.mark.parametrize("I, J, V, start_v", 
[
    (
        [0, 1, 2],
        [1, 2, 0],
        [True] * 3,
        0
    )
])
def test_not_undirect_trc(I, J, V, start_v):
    M = Matrix.from_lists(I, J, V)
    with pytest.raises(ValueError):
        trc(M, 1)
    
    
    
    
    
