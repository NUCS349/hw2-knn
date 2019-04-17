## Problems

## Code implementation (5 points)
Pass test cases by implementing the functions in the `code` directory.

Your grade for this section is defined by the autograder. If it says you got an 80/100,
you get 4 points here.

## Free response questions (5 points)

1. (0.5 points) Assume you've used a perceptron to learn a good decision boundary model <img src="/tex/9fa880c0493a6190c9cd7031ba53083a.svg?invert_in_darkmode&sanitize=true" align=middle width=35.03868554999999pt height=27.72066330000001pt/> for a two-way classification problem. What is the time complexity to select a class label for a new point using this model? Give your answer as a function of the number of points, <img src="/tex/55a049b8f161ae7cfeb0197d75aff967.svg?invert_in_darkmode&sanitize=true" align=middle width=9.86687624999999pt height=14.15524440000002pt/>, in the data set the decision boundary was learned from. What is the space complexity of the model, in terms of <img src="/tex/55a049b8f161ae7cfeb0197d75aff967.svg?invert_in_darkmode&sanitize=true" align=middle width=9.86687624999999pt height=14.15524440000002pt/> and the number of dimensions <img src="/tex/2103f85b8b1477f430fc407cad462224.svg?invert_in_darkmode&sanitize=true" align=middle width=8.55596444999999pt height=22.831056599999986pt/> in the vector representing each data point? Explain your reasoning.

2. (0.5 points) Assume you have a K-nearest neighbor (KNN) classifier for doing a 2-way classification. Assume it uses an <img src="/tex/09af92d48ab87fa468ebde78082d1091.svg?invert_in_darkmode&sanitize=true" align=middle width=17.96371994999999pt height=22.465723500000017pt/> norm distance metric (e.g. Euclidean, Manhattan, etc.). Assume a naive implementation, like the one taught to you in class. What is the time complexity to select a class label for a new point using this model? Give your answer as a function of the number of points, <img src="/tex/55a049b8f161ae7cfeb0197d75aff967.svg?invert_in_darkmode&sanitize=true" align=middle width=9.86687624999999pt height=14.15524440000002pt/>, in the data set. What is the space complexity of the model, in terms of <img src="/tex/55a049b8f161ae7cfeb0197d75aff967.svg?invert_in_darkmode&sanitize=true" align=middle width=9.86687624999999pt height=14.15524440000002pt/> and the number of dimensions <img src="/tex/2103f85b8b1477f430fc407cad462224.svg?invert_in_darkmode&sanitize=true" align=middle width=8.55596444999999pt height=22.831056599999986pt/> in the vector representing each data point? Explain your reasoning. 

3. (0.5 points) What is the time-complexity of training a KNN classifier, in terms of the number of points in the training data, <img src="/tex/55a049b8f161ae7cfeb0197d75aff967.svg?invert_in_darkmode&sanitize=true" align=middle width=9.86687624999999pt height=14.15524440000002pt/>, and the number of dimensions <img src="/tex/2103f85b8b1477f430fc407cad462224.svg?invert_in_darkmode&sanitize=true" align=middle width=8.55596444999999pt height=22.831056599999986pt/> in the vector representing each data point? Is this greater or less than the time-complexity of training a perceptron on the same data? Explain your reasoning.

4. (0.5 points) Is a KNN classifier able to learn a non-linear decision surface without using a data transformation prior to inputting the data to the classifier? Why or why not? 

5. (O.5 points) Assume a Euclidean distance metric. Give an illustration of where the function produced by KNN regression would be very similar to that of a learned linear regressor, but very different when considered on a larger range of input values than exists in the training data. Provide a graph and an explanation. 

#### The following questions presume a lot of things. 
 - 1) they implemented regression (not classification) as KNN. 
 - 2) They have an understanding of how to deal with missing data
 - 3) We've discussed collaborative filtering with them
 - 4) They know what imputation is.
#### I think this would require an additional lecture to cover that kind of material.
 

6. (0.5 points) We will now perform KNN regression (or imputation) on the MovieLens dataset. The MovieLens dataset contains 100k ratings on 1682 movies given by 942 users. First, explore the MovieLens data. For each pair of users, what is the mean number of movies that two users have reviewed in common? What is the median number of movies that two reviewers have reviewed in common?

7. (0.5 points) We will build up a *collaborative filter* over the next few questions. Collaborative filters are essentially how recommendation algorithms work on sites like Amazon ("people who bought blank also bought blank") and Netflix ("you watched blank so you might also like blank"). They work by comparing distances between users. If two users are similar, then items that one user has seen and liked but the other hasn't seen are recommended to the other user. First, frame this problem as a KNN regression problem. What are the features? What is the output of the system? How can the neighbors of a user be used to impute that users rating for a movie they have not rated?

8.  (O.5 points) The effectiveness of a KNN regressor is affected by the value of K that you choose and the number of data points it has available. Use the MovieLens data set, which contains 100k points. Split it into 99000 training and 1000 testing points. Use a Euclidean distance measure for your regressor.  Now, fit the data using K = 1, K = 2, K = 4, K = 8. Which one performed best, as measured with sum-of-squared-errors on the testing set? Repeat the experiment with the testing and training set flipped. How did this change things?

9.  (0.5 points) The effectiveness of a KNN  regressor is affected by the distance measure chosen. Let's explore how changing the distance measure changees the effectiveness of a KNN regressor. Use the MovieLens dataset, using the best K found in the previous question. Split the data into 99000 training and 1000 testing points. Compare the performance of imputation, using a sum-of-squared-errors on the testing set, for the following distance measures: 'euclidean' (p=2), 'manhattan' (p=1), and 'cosine'. Which distance measure worked best? Why do you think so?

10. (0.5 points) The effectiveness of a KNN  regressor is affected by the aggregator chosen. Let's explore how changing the distance measure changees the effectiveness of a KNN regressor. Use the MovieLens dataset, using the best K found in the previous question. Split the data into 99000 training and 1000 testing points. Compare the performance of imputation, using a sum-of-squared-errors on the testing set, for the following aggregators: 'mean', 'median', and 'mode'. Which worked best? Why do you think so?
