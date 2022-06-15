from pygraphblas import Matrix, Vector
from pygraphblas.types import BOOL, INT64

def trc(matrix: Matrix, start_v: int):
    
    #check matrix
    if not matrix.square:
        raise ValueError("This matrix is not square")
    if matrix.type != BOOL:
        raise ValueError("Mtx's type is not BOOL")
    if not matrix.iseq(matrix.transpose()):
        raise ValueError("Graph is not undirected") 
   
    
    #matrix2 = matrix @ matrix
    matrix2 = matrix.mxm(matrix, cast=INT64)
    matrix2 = matrix2.emult(matrix, cast=INT64)
    
    n = matrix.nrows
    result = list()
    for j in range(n):
        j_row = matrix2.extract_row(j)
        elm_result = 0
        for i in range(n):
            elm_result += j_row.get(i, 0)
        result.append(elm_result)
    
    return result
    
