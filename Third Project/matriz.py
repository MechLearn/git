

class Matrix:
    def __init__(self, rows,columns, elements):
        if rows <=0 or columns <=0:
            raise ValueError("The rows and columns must be upper that zero!")
        if len(elements) != rows * columns:
            raise ValueError("La cantidad de elementos no coincide")
        
        
        self.rows = rows
        self.columns = columns
        self.values = elements
        self.dimension = (rows,columns)
        
        
    def __str__(self):
        matrix_str = ""
        
        for i in range(self.rows):
            row = self.values[i * self.columns : (i+1)*self.columns]
            matrix_str += " ".join(map(str,row)) + "\n"
        
        return matrix_str
    
    def sum(self, other_matrix):
        if self.dimension != other_matrix.dimension:
            raise ValueError(" The dimension of both matrix are different, cant do the summ ! ")
        
        new_matrix = Matrix(self.rows,self.columns, [a+b for a,b in zip(self.values, other_matrix.values)])
        return new_matrix
    
    def difference(self, other_matrix):
      if self.dimension != other_matrix.dimension:
        raise ValueError(" The dimension of both matrix are different, cant do the difference ! ")
        
        new_matrix = Matrix(self.rows,self.columns, [a-b for a,b in zip(self.values, other_matrix.values)])
        return new_matrix
    
    
    def multiplication(self, scalar):
        new_matrix = Matrix(self.rows,self.columns,[value * scalar for value in self.values])
        return new_matrix
    
    def transpuesta(self):
     new_matrix = Matrix(self.columns, self.rows, [self.values[i + j * self.columns] for j in range(self.rows) for i in range(self.columns)])
     return new_matrix
    
    
    
    
 
    
    

        