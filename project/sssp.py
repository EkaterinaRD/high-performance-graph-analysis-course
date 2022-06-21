from pygraphblas import Matrix, Vector
from pygraphblas.types import INT64
from typing import List


def _sssp(matrix: Matrix, start_vs: List[int]):
    
    if not matrix.square:
        raise ValueError("This matrix is not square")
    n = matrix.nrows
    m = len(start_vs)
    for i in range(m):
        if start_vs[i] >= n or start_vs[i] < 0:
            raise ValueError("Vertex is incorrect")
    
    front_mtx = Matrix.sparse(INT64, nrows = m, ncols = n)
    for i, v in enumerate(start_vs):
        front_mtx.assign_scalar(0, i, v)
    
    step = 0
    is_change = True
    while step < n and is_change:
        prev = front_mtx
        front_mtx.mxm(matrix, semiring=INT64.min_plus, out=front_mtx, accum=INT64.min)
        is_change = not prev.iseq(front_mtx)
        step += 1
    
    result = list()
    
    
    for i, v in enumerate(start_vs):
        res_row = list()
        for j in range(n):
            res_row.append(front_mtx.get(i, j, -1))
        result.append((v, res_row))
    
    return result

def sssp(matrix: Matrix, start_v: int):
    
    result = list()
    result = _sssp(matrix, [start_v])[0][1]
    
    return result
   
    
def multi_sssp(matrix: Matrix, start_vs: List[int]):
    
    return _sssp(matrix, start_vs)
