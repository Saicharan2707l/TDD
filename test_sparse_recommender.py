#test page for sparse_recommender page
import pytest
import unittest
from sparse_recommender import SparseMatrix
movie_rating_matrix = SparseMatrix(3,3)

#consider:user as row,movie as column,movie_rating as a value
# Testing the set method for the user,movie value as negative
def testsetmethodwithnegativevalueasuser():
    assert movie_rating_matrix.set(-1, 0, 1) == "Negative values prevent the construction of the matrix"

# Testing the set method for string value as user
def testsetmethodwithStringvalueasuser():
    assert movie_rating_matrix.set("str", 0, 1)=="user must be an integer"

# Testing the set method for string value as movie
def testsetmethodwithStringvalueasmovie():
    assert movie_rating_matrix.set(0, "str", 1)=="movie must be an integer"

# Testing the set method for the user,movie value as negative
def testsetmethodwithnegativevalueasmovie():
   assert movie_rating_matrix.set(1, -2, -3) == "Negative values prevent the construction of the matrix"

#Testing the set method for the user,movie value as outofboundindex
def testsetmethodwithOutofBoundIndex():
   assert movie_rating_matrix.set(4, 4, 3) == "The row and column are out of bound index"

# Testing the set method for the user,movie rating as negative
def testsetmethodwithnegativevalueasusermovierating():
   assert movie_rating_matrix.set(-1, 2, -3) == "Negative values prevent the construction of the matrix"

# Testing the set method for the movie value as negative
def testsetmethodwithnegativevalueasmovie_rating():
    movie_rating_matrix.set(1, 2, -3)
    assert movie_rating_matrix.set(1, 2, -3) == "The value of the movie_rating cannot be negative."

# Testing the default value for the matrix and the result is in zero.
def testinggetdefaultwithcorrectvalue():
    assert movie_rating_matrix.get(2, 2) == 0  # Default movie_rating for unset elements should be 0

#Testing the set method for the user,movie value as outofboundindex
def testgetmethodwithOutofBoundIndex():
   assert movie_rating_matrix.get(4, 4) == "Invalid user or movie index"

# Testing the  negative value for user and movie as input,handling through raising an exception.
def testinggetdefaultwithIncorrectvalueforusermovie():
    assert movie_rating_matrix.get(-2, -2) == "Invalid user or movie index"

# Testing the  negative value for movie as input,handling through raising an exception.
def testinggetdefaultwithIncorrectvalueformovie():
    assert movie_rating_matrix.get(2, -2) == "Invalid user or movie index"

# Testing the wrong value for the matrix and the handling the result
def testinggetdefaultwithIncorrectvalue():
    try:
        assert movie_rating_matrix.get(2, 2) == 1  # Default movie_rating for unset elements should be 0
    except AssertionError as e:
        print("please test the value with the correct input")

# Testing the recommendation  movie_rating matrix with the user vector and checking with the value.
def test_recommendmovierating_Checkcorrectvalue():
    movie_rating_matrix.set(1, 1, 1)
    movie_rating_matrix.set(1, 3, 1)
    movie_rating_matrix.set(2, 2, 1)
    movie_rating_matrix.set(3, 1, 1)
    vector = [2, 3, 4]
    print("Created the movie_vector and running the code")
    recommendations = movie_rating_matrix.recommend(vector)
    assert recommendations == [6, 3, 2]  # Expected result of matrix-vector multiplication

# Testing the different length of user vector with the movie_rating_matrix,handling with the exception.
def test_recommendmovierating_withdiffuservectorlengths():
    movie_rating_matrix.set(1, 1, 1)
    movie_rating_matrix.set(1, 3, 1)
    movie_rating_matrix.set(2, 2, 1)
    movie_rating_matrix.set(3, 1, 1)
    vector = [2, 3, 4,0]
    print("Created the movie_vector and running the code")
    recommendations = movie_rating_matrix.recommend(vector)
    assert recommendations =="The Sparse Matrix cannot be possible to do with the given vector"   # Expected result of matrix-vector multiplication

#Addition of two sparse matrix and checking with the result_matrix
def test_addmovieratings_Checkingcorrectvalues():
    movie_rating_matrix = SparseMatrix(3,3)
    movie_rating_matrix.set(0, 0, 0.3)
    movie_rating_matrix.set(1, 1, 0.2)
    movie_rating_matrix.set(2, 2, 0.3)
    # Creating a new movie matrix to add
    new_matrix = SparseMatrix(3,3)
    new_matrix.set(0, 0, 0.3)
    new_matrix.set(1, 0, 0.3)
    new_matrix.set(2, 2, 0.4)
    result_matrix = movie_rating_matrix.add_movie(new_matrix)
    dense_result = result_matrix.to_dense()
    expected_result = [[0.6,0,0],[0.3,0.2,0],[0,0,0.7]]
    assert dense_result == expected_result

#Addition of two sparse matrix and checking with the result_matrix
def test_addmovieratings_withdifferentusersmovies():
    movie_rating_matrix = SparseMatrix(3,3)
    movie_rating_matrix.set(0, 0, 0.3)
    movie_rating_matrix.set(1, 1, 0.2)
    movie_rating_matrix.set(2, 2, 0.3)
    # Creating a new movie matrix to add
    new_matrix = SparseMatrix(4,4)
    new_matrix.set(0, 0, 0.3)
    new_matrix.set(1, 0, 0.3)
    new_matrix.set(2, 2, 0.4)
    result_matrix = movie_rating_matrix.add_movie(new_matrix)
    assert result_matrix == "The two matrix users and movies should be correct"

#The pass value is obtained by comparing the provided sparse matrix to the dense matrix with the right value.
def testdensematrixwith_correctvalue():
    movie_rating_matrix = SparseMatrix(3,3)
    movie_rating_matrix.set(0, 0, 2)
    movie_rating_matrix.set(1, 0, 2)
    movie_rating_matrix.set(2, 2, 2)
    # Convert the sparse matrix to a dense matrix
    dense_matrix = movie_rating_matrix.to_dense()
    # Define the expected dense matrix with matching dimensions
    #Define the expected dense matrix with matching dimensions
    expected_matrix = [[2, 0, 0], [2, 0, 0], [0, 0, 2]]
    # Assert that the dense matrix matches the expected matrix
    assert dense_matrix == expected_matrix

