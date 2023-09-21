#consider:user as row,movie as column,movie_rating as a value
class SparseMatrix:
    def __init__(self,user,movie):
        self.matrix = dict()
        self.user=user
        self.movie= movie

    def set(self, user, movie, movie_rating):
        # Converting (user, movie) to movie_rating value
        try:
            if not isinstance(user, int):
                raise ValueError("user must be an integer")
            if not isinstance(movie, int):
                raise ValueError("movie must be an integer")
            if user < 0 or movie < 0:
                raise ValueError("Negative values prevent the construction of the matrix")
            if movie_rating < 0:
                raise ValueError("The value of the movie_rating cannot be negative.")
            if self.user<user or self.movie<movie:
                raise ValueError("The row and column are out of bound index")
            if movie_rating != 0:
                self.matrix[(user, movie)] = movie_rating

            elif (user, movie) in self.matrix:
                del self.matrix[(user, movie)]
        except ValueError as e:
            return str(e)
    def get(self, user, movie):
        # This function returns the movie_rating at (user, movie).
        try:
            if user < 0 or movie < 0 or self.user<user or self.movie<movie:
                raise ValueError("Invalid user or movie index")
            return self.matrix.get((user, movie), 0)  ## If not specified, the default movie_rating is 0.
        except ValueError as e:
            return str(e)

    def recommend(self, vector):
        try:
            if self.movie!=len(vector):
                raise ValueError("The Sparse Matrix cannot be possible to do with the given vector")
            # Calculating the total number of users using the matrix's maximum user index.
            max_user = max(user for (user, _) in self.matrix.keys()) if self.matrix else 0
            recommendations = [0] * max_user  #Initialize suggestions based upon on the user count.
            for user in range(1, max_user + 1):
                for movie in range(1, len(vector) + 1):
                    recommendations[user - 1] += self.get(user, movie) * vector[movie - 1]
            return recommendations
        except ValueError as v:
            return str(v)

    def add_movie(self,matrix):
        try:
            if self.user!=matrix.user or self.movie!=self.movie:
                raise ValueError("The two matrix users and movies should be correct")
            result_matrix = SparseMatrix(3,3)  # Create a new matrix to store the result
            max_user = 0
            max_movie = 0
            #Determine the highest user and movie indices possible for both matrices.
            for user, movie in self.matrix.keys():
                max_user = max(max_user, user)
                max_movie = max(max_movie, movie)
            for user in range(max_user + 1):
                for movie in range(max_movie + 1):
                    if user < 0 or movie < 0:
                        raise ValueError("User and movie values must be non-negative.")
                    value = self.get(user, movie) + matrix.get(user, movie)  # Addition of values from both matrices
                    result_matrix.set(user, movie, value)  # Set the result in the new matrix
            return result_matrix
        except ValueError as e:
            return str(e)


    def to_dense(self):
        max_user = -1
        max_movie = -1
        # Find the maximum user and movies in the sparse matrix
        for user, movie in self.matrix.keys():
            if user > max_user:
                max_user = user
            if movie > max_movie:
                max_movie = movie
        #Create a 2D list for the dense matrix and set all of its members to 0.
        dense_matrix = [[0] * (max_movie + 1) for _ in range(max_user + 1)]

        # Add values from the sparse matrix to the dense matrix.
        for (user, movie), rating in self.matrix.items():
            dense_matrix[user][movie] = rating
        return dense_matrix

movie_rating_matrix = SparseMatrix(3,3)
movie_rating_matrix.set(0, 0, 0.3)
movie_rating_matrix.set(1, 1, 0.2)
movie_rating_matrix.set(2, 2, 0.3)
print(movie_rating_matrix.get(1,1))
new_matrix = SparseMatrix(3,3)
new_matrix.set(0, 0, 0.3)
new_matrix.set(1, 0, 0.3)
new_matrix.set(2, 2, 0.4)
result_matrix=SparseMatrix(3,3)
result_matrix = movie_rating_matrix.add_movie(new_matrix)
additionmatrix=result_matrix.to_dense()
print(additionmatrix)
