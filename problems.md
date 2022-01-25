# Coding (6 points)
Pass test cases by implementing the functions in the `src` directory.

Your score for this section is defined by the autograder. If it says you got an 80/100, you get 4.8 points here.

# Free-response Questions (4 points)

1. Assume you have a k-Nearest Neighbors (kNN) classifier for doing a 2-way classification. Assume it uses an <img src="/tex/09af92d48ab87fa468ebde78082d1091.svg?invert_in_darkmode&sanitize=true&sanitize=true" align=middle width=17.96371994999999pt height=22.465723500000017pt/> norm distance metric (e.g., Euclidean, Manhattan, etc.). Assume a straightforward implementation, like the one discussed in class. 
    1. (0.25 points) What is the time complexity to select a class label for (i.e., to classify) a new point using this model? Give your answer in terms of the number of points, <img src="/tex/55a049b8f161ae7cfeb0197d75aff967.svg?invert_in_darkmode&sanitize=true&sanitize=true" align=middle width=9.86687624999999pt height=14.15524440000002pt/>, in the data set. You can answer this using Big O notation and explain why you think that is the answer, or you can answer this by simply explaining your reasoning in terms of the number of points.
    1. (0.25 points) What is the space complexity of the model, in terms of <img src="/tex/55a049b8f161ae7cfeb0197d75aff967.svg?invert_in_darkmode&sanitize=true&sanitize=true" align=middle width=9.86687624999999pt height=14.15524440000002pt/> and the number of dimensions, <img src="/tex/2103f85b8b1477f430fc407cad462224.svg?invert_in_darkmode&sanitize=true&sanitize=true" align=middle width=8.55596444999999pt height=22.831056599999986pt/>, in the vector representing each data point? Once again, you can use Big O notation with an explanation or give an explanation of your reasoning. 

1. (0.25 points) What is the time complexity of training a kNN classifier in terms of the number of points in the training data, <img src="/tex/55a049b8f161ae7cfeb0197d75aff967.svg?invert_in_darkmode&sanitize=true&sanitize=true" align=middle width=9.86687624999999pt height=14.15524440000002pt/>, and the number of dimensions, <img src="/tex/2103f85b8b1477f430fc407cad462224.svg?invert_in_darkmode&sanitize=true&sanitize=true" align=middle width=8.55596444999999pt height=22.831056599999986pt/>, in the vector representing each data point? The same note about Big O notation applies here as did for Question 1.

1. (0.25 points) Is a kNN classifier able to learn a non-linear decision surface? Why or why not? 

1. Imagine we're building a *collaborative filter*, which we'll learn a lot about later in the quarter. Collaborative filters are essentially how recommendation algorithms work on sites like Amazon ("people who bought blank also bought blank") and Netflix ("you watched blank, so you might also like blank"). They work by comparing distances between users.
    1. (0.25 points) If two users are similar, then items that one user has seen and liked but the other hasn't seen are recommended to the other user. First, frame this problem as a kNN regression problem. How are users compared to each other?
    1. (0.25 points) Given the k nearest neighbors of a user, how can these k neighbors be used to estimate the rating for a movie that the user has not seen?

1. (0.5 points) Your boss gives you a very large dataset. What problems do you see coming up with implementing kNN? Name a few of them.
 
1. (0.5 points) Discuss possible solutions to the problems you have identified in Question 5.
 
1. You are given these six training examples as ((a_i, b_i), y_i) values, where a_i and b_i are the two feature values (positive integers) and y_i is the class label: {((1,1),-1),((2, 2), −1), ((2, 8), +1), ((4, 4), +1), ((6, 5), −1), ((3, 6), −1)}.
    1. (0.5 points) Classify the following test example at coordinates (4, 7) using a kNN classifier with k = 3 and Manhattan distance defined by d((u, v), (p, q)) = |u − p| + |v − q|.
    1. (0.5 points) Explain in short how you came up with the answer.
 
1. (0.5 points) Assume we increase k in a kNN classifier from 1 to n, where n is the number of training examples. Discuss if the classification accuracy on the training set increases. Consider weighted and unweighted kNN classifiers.
