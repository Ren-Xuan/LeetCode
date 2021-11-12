class Solution:
    def spiralOrder(self, matrix) :
        self.result = []
        def transpose(matrix):
            return list(zip(*(matrix[1:])))[::-1]
        def f(matrix):
            if len(matrix) == 0:
                return
            for e in matrix[0]:
                self.result.append(e)
            matrix = transpose(matrix)
            f(matrix)
        f(matrix)
        return self.result