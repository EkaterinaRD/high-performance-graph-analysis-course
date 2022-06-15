from pygraphblas import Matrix, Vector
from pygraphblas.types import INT64
from typing import List


def ssp(matrix: Matrix, start_v: int):
    
    if not matrix.square:
        raise ValueError("This matrix is not square")
    n = matrix.nrows
    if start_v >= n or start_v < 0:
        raise ValueError("Vertex is incorrect")
        
        
    front = Vector.sparse(INT64, n)
    front[start_v] = 0;
    
    step = 0
    while step < n:
        front.min_plus(matrix, out=front, accum=INT64.min)
        step += 1
    
    result = list()
    for i in range(n):
        result.append(front.get(i, -1))
    return result
    
    
def multi_ssp(matrix: Matrix, start_vs: List[int]):
    result = list()
    for start_v in start_vs:
        result.append((start_v, ssp(matrix,start_v)))
        
    return result
