""" Basic class to create a matrix from a string of numbers
 and then return specific rows and columns """
class Matrix:
    """ Class definition """
    data = []

    def __init__(self, matrix_string):
        """ Initializer """
        if not isinstance(matrix_string, str):
            raise TypeError("Matrix class requires string object.")
        temp = matrix_string.split("\n")
        for row in temp:
            self.data.append(row.split(" "))
        self.convert_array_str_to_int()

    def convert_array_str_to_int(self):
        """ Converts array of strings to array of ints """
        row = col = 0
        while row < len(self.data):
            while col < len(self.data[row]):
                self.data[row][col] = int(self.data[row][col])
                col += 1
            col = 0
            row += 1

    def row(self, index):
        """ Return a row based on the index provided """
        return self.data[index - 1]

    def column(self, index):
        """ Return a column """
        returnee = []
        for row in self.data:
            returnee.append(row[index - 1])
        return returnee
