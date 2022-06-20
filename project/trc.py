from pygraphblas import Matrix, Vector
from pygraphblas.types import BOOL, INT64

def trc(matrix: Matrix, start_v: int):
    
    #check matrix
    if not matrix.square:
        raise ValueError("This matrix is not square")
    if matrix.type != BOOL:
        raise ValueError("Mtx's type is not BOOL")
    if not matrix.iseq(matrix.transpose()):
        matrix = matrix | matrix.transpose() 
   
 
    tmp_mtx = matrix.mxm(matrix, cast=INT64, mask=matrix)
    
    
    n = matrix.nrows
    
    result = list()
    for i in range(n):
        tmp = list()
        tmp = tmp_mtx.extract_row(i).to_lists()[1]
        result.append(sum(tmp) // 2)
    
    return result
    
