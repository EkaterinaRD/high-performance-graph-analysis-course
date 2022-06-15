from pygraphblas import Matrix, Vector
from pygraphblas.types import BOOL, INT64
from pygraphblas.descriptor import RC
from typing import List, Tuple

def bfs (matrix: Matrix, start_v: int):
    
    
    if not matrix.square:
        raise ValueError("This matrix is not square")
    n = matrix.nrows
    if start_v >= n or start_v < 0:
        raise ValueError("Vertex is incorrect")
    
    front = Vector.sparse(BOOL, n)
    front[start_v] = True
    
    visited = Vector.sparse(BOOL, n)
    visited[start_v] = True
    
    dist = Vector.sparse(INT64, n, fill=-1)
    dist[start_v] = 0
    level = 1
   
   
    while level < n:
        front = front.vxm(matrix, desc=RC, mask=visited)
        visited = visited | front
        dist.assign_scalar(level, mask=front)
        level += 1
    
    result = list()
    result = dist.to_lists()
    return result
    
def multi_bfs(matrix: Matrix, start_vs: List[int]):
    
    result = list()
    for start_v in start_vs:
        result.append((start_v, bfs(matrix,start_v)))
        
    return result
