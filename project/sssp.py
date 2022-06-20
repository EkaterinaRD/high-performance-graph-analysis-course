from pygraphblas import Matrix, Vector
from pygraphblas.types import INT64
from typing import List


def sssp(matrix: Matrix, start_v: int):
    
    if not matrix.square:
        raise ValueError("This matrix is not square")
    n = matrix.nrows
    if start_v >= n or start_v < 0:
        raise ValueError("Vertex is incorrect")
        
        
    front = Vector.sparse(INT64, n)
    front[start_v] = 0;
   
 
    step = 0
    while step < n:
        front.vxm(matrix, semiring=INT64.min_plus, out=front, accum=INT64.min)
        step += 1
        
    result = list()
    for i in range(n):
        result.append(front.get(i, -1))

    return result
   
    
def multi_sssp(matrix: Matrix, start_vs: List[int]):
    
    if not matrix.square:
        raise ValueError("This matrix is not square")
    n = matrix.nrows
    m = len(start_vs)
    for i in range(m)
        if start_vs[i] >= n or start_v[i] < 0:
            raise ValueError("Vertex is incorrect")
    
    front_mtx = Matrix.sparse(INT64, nrows = m, ncols = n)
    for i, v in enumerate(start_vs):
        front_mtx.assign_scalar(0, i, v)
    
    step = 0
    while step < n:
        front_mtx.mxm(matrix, semiring=INT64.min_plus, out=front_mtx, accum=INT64.min)
        step += 1
    
    result = list()
    
    
    for i, v in enumerate(start_vs):
        res_row = list()
        for j in range(n):
            res_row.append(front_mtx.get(i, j, -1))
        result.append((v, res_row))
    
    return result
