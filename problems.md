## Problems

## Code implementation (5 points)
Pass test cases by implementing the functions in the `code` directory.

Your grade for this section is defined by the autograder. If it says you got an 80/100,
you get 4 points here.

## Free response questions (5 points)

1. (0.5 points) Assume you have a K-nearest neighbor (KNN) classifier for doing a 2-way classification. Assume it uses an <img src="/tex/09af92d48ab87fa468ebde78082d1091.svg?invert_in_darkmode&sanitize=true&sanitize=true" align=middle width=17.96371994999999pt height=22.465723500000017pt/> norm distance metric (e.g. Euclidean, Manhattan, etc.). Assume a naive implementation, like the one taught to you in class. What is the time complexity to select a class label for a new point using this model? Give your answer as a function of the number of points, <img src="/tex/55a049b8f161ae7cfeb0197d75aff967.svg?invert_in_darkmode&sanitize=true&sanitize=true" align=middle width=9.86687624999999pt height=14.15524440000002pt/>, in the data set. What is the space complexity of the model, in terms of <img src="/tex/55a049b8f161ae7cfeb0197d75aff967.svg?invert_in_darkmode&sanitize=true&sanitize=true" align=middle width=9.86687624999999pt height=14.15524440000002pt/> and the number of dimensions <img src="/tex/2103f85b8b1477f430fc407cad462224.svg?invert_in_darkmode&sanitize=true&sanitize=true" align=middle width=8.55596444999999pt height=22.831056599999986pt/> in the vector representing each data point? Explain your reasoning. 

2. (0.5 points) What is the time-complexity of training a KNN classifier, in terms of the number of points in the training data, <img src="/tex/55a049b8f161ae7cfeb0197d75aff967.svg?invert_in_darkmode&sanitize=true&sanitize=true" align=middle width=9.86687624999999pt height=14.15524440000002pt/>, and the number of dimensions <img src="/tex/2103f85b8b1477f430fc407cad462224.svg?invert_in_darkmode&sanitize=true&sanitize=true" align=middle width=8.55596444999999pt height=22.831056599999986pt/> in the vector representing each data point? Explain your reasoning.

3. (0.25 points) Is a KNN classifier able to learn a non-linear decision surface without using a data transformation prior to inputting the data to the classifier? Why or why not? 

4. (0.5 points) We will build up a *collaborative filter* over the next few questions. The questions presume that you have implemented the `collaborative_filtering` function and passed the corresponding test case `test_collaborative_filtering`. Collaborative filters are essentially how recommendation algorithms work on sites like Amazon ("people who bought blank also bought blank") and Netflix ("you watched blank so you might also like blank"). They work by comparing distances between users. If two users are similar, then items that one user has seen and liked but the other hasn't seen are recommended to the other user. First, frame this problem as a KNN regression problem. How are users compared to each other? Given the K nearest neighbors of a user, how can these K neighbors be used to estimate the rating for a movie that the user has not seen?

5. (0.25 points) The MovieLens dataset contains 100k ratings on 1682 movies given by 942 users. First, explore the MovieLens data. For each pair of users, what is the mean number of movies that two users have reviewed in common? What is the median number of movies that two reviewers have reviewed in common? How would the number of movies that two users have both reviewed affect the quality of your collaborative filter? What occurs for those movies that no user has rated? 

6. (0.5 points) Your boss gives you a very large dataset. What problems do you see coming up with implementing kNN? Name a few of them.
 
7. (0.5 points) Discuss possible solutions to the problems you have identified in question (12).
 
8. (0.5 points) Given six training examples as ((a_i, b_i), y_i) values, where a_i and b_i are the two feature values (positive integers) and y_i is the class label: {((1,1),-1),((2, 2), −1), ((2, 8), +1), ((4, 4), +1), ((6, 5), −1), ((3, 6), −1)}. Classify the following test example at coordinates (4, 7) using a k-NNclassifier with k = 3 and Manhattan-distance defined by d((u, v), (p, q)) = |u −p| + |v −q|. Explain shortly how you came up with the answer.
 
9. (0.5 poins) Assume we increase k in a k-NN classifier from 1 to n, where n is the number of training examples. Discuss if the classification accuracy on the training set increases. Consider weighted and unweighted K-NN classifiers.
