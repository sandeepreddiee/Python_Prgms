class SparseMatrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = {}  # Use a dictionary to store non-zero elements

    def set_value(self, row, col, value):
        # Set the value at (row, col) to value
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.data[(row, col)] = value

    def get_value(self, row, col):
        # Return the value at (row, col)
        return self.data.get((row, col), 0)

    def multiply_with_vector(self, user_vector):
        # Multiply the sparse matrix with a user_vector to produce recommendations
        if len(user_vector) != self.cols:
            raise ValueError("Vector length must match the number of columns")
        
        recommendations = [0] * self.rows
        for (row, col), value in self.data.items():
            recommendations[row] += value * user_vector[col]
        
        return recommendations

    def add_matrix(self, other_matrix):
        # Add another sparse matrix to the current one
        if self.rows != other_matrix.rows or self.cols != other_matrix.cols:
            raise ValueError("Matrix dimensions must match")
        
        result = SparseMatrix(self.rows, self.cols)
        for (row, col), value in self.data.items():
            result.set_value(row, col, value)
        
        for (row, col), value in other_matrix.data.items():
            result.set_value(row, col, result.get_value(row, col) + value)
        
        return result

    def to_dense_matrix(self):
        # Convert the sparse matrix to a dense matrix
        dense_matrix = [[0] * self.cols for _ in range(self.rows)]
        for (row, col), value in self.data.items():
            dense_matrix[row][col] = value
        
        return dense_matrix