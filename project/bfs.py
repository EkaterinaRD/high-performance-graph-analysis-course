from pygraphblas import Matrix, Vector
from pygraphblas.types import BOOL, INT64
from pygraphblas.descriptor import RC
from typing import List, Tuple

def _bfs(matrix: Matrix, start_vs: List[int]):
    
    if not matrix.square:
        raise ValueError("This matrix is not square")
    n = matrix.nrows
    m = len(start_vs)
    for i in range(m):
        if start_vs[i] >= n or start_vs[i] < 0:
            raise ValueError("Vertex is incorrect")
         
    
    
    front_mtx = Matrix.sparse(BOOL, nrows = m, ncols = n)
    visited_mtx = Matrix.sparse(BOOL, nrows = m, ncols = n)
    dist_mtx = Matrix.sparse(INT64, nrows = m, ncols = n)
    
    for r, v in enumerate(start_vs):
        front_mtx.assign_scalar(True, r, v)
        visited_mtx.assign_scalar(True, r, v)
        dist_mtx.assign_scalar(0, r, v)
    
    level = 1
    prev = -1
    while visited_mtx.nvals != prev:
        prev = visited_mtx.nvals
        front_mtx = front_mtx.mxm(matrix, mask=visited_mtx, desc=RC)
        visited_mtx = visited_mtx | front_mtx
        dist_mtx.assign_scalar(level, mask=front_mtx)
        level += 1
    
    result = list()
    
    
    for i, v in enumerate(start_vs):
        res_row = list()
        for j in range(n):
            res_row.append(dist_mtx.get(i, j, -1))
        result.append((v, res_row))
    
    return result


def bfs (matrix: Matrix, start_v: int):
    
    result = list()
    result = _bfs(matrix, [start_v])[0][1]
    
    return result
    
    
    
def multi_bfs(matrix: Matrix, start_vs: List[int]):
    
    return _bfs(matrix, start_vs)
   
