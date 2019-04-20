## Problems

## Code implementation (5 points)
Pass test cases by implementing the functions in the `code` directory.

Your grade for this section is defined by the autograder. If it says you got an 80/100,
you get 4 points here.

## Free response questions (5 points)

1. (0.5 points) Assume you've used a perceptron to learn a good decision boundary model $\mathbf{w^Tx}$ for a two-way classification problem. What is the time complexity to select a class label for a new point using this model? Give your answer as a function of the number of points, $n$, in the data set the decision boundary was learned from. What is the space complexity of the model, in terms of $n$ and the number of dimensions $d$ in the vector representing each data point? Explain your reasoning.

2. (0.5 points) Assume you have a K-nearest neighbor (KNN) classifier for doing a 2-way classification. Assume it uses an $L^p$ norm distance metric (e.g. Euclidean, Manhattan, etc.). Assume a naive implementation, like the one taught to you in class. What is the time complexity to select a class label for a new point using this model? Give your answer as a function of the number of points, $n$, in the data set. What is the space complexity of the model, in terms of $n$ and the number of dimensions $d$ in the vector representing each data point? Explain your reasoning. 

3. (0.5 points) What is the time-complexity of training a KNN classifier, in terms of the number of points in the training data, $n$, and the number of dimensions $d$ in the vector representing each data point? Is this greater or less than the time-complexity of training a perceptron on the same data? Explain your reasoning.

4. (0.5 points) Is a KNN classifier able to learn a non-linear decision surface without using a data transformation prior to inputting the data to the classifier? Why or why not? 

5. (O.5 points) Assume a Euclidean distance metric. Give an illustration of where the function produced by KNN regression would be very similar to that of a learned linear regressor, but very different when considered on a larger range of input values than exists in the training data. Provide a graph and an explanation. 

6. (0.5 points) We will build up a *collaborative filter* over the next few questions. The questions presume that you have implemented the `collaborative_filtering` function and passed the corresponding test case `test_collaborative_filtering`. Collaborative filters are essentially how recommendation algorithms work on sites like Amazon ("people who bought blank also bought blank") and Netflix ("you watched blank so you might also like blank"). They work by comparing distances between users. If two users are similar, then items that one user has seen and liked but the other hasn't seen are recommended to the other user. First, frame this problem as a KNN regression problem. How are users compared to each other? Given the K nearest neighbors of a user, how can these K neighbors be used to impute the rating for a movie that the user has not seen?

7. (0.5 points) We will now perform KNN regression (or imputation) on the MovieLens dataset. The MovieLens dataset contains 100k ratings on 1682 movies given by 942 users. First, explore the MovieLens data. For each pair of users, what is the mean number of movies that two users have reviewed in common? What is the median number of movies that two reviewers have reviewed in common? How would the number of movies that two users have both reviewed affect the quality of your collaborative filter? What occurs for those movies that no user has rated? 

8.  (0.25 points) We will implement our collaborative filter on the MovieLens dataset. The process for this and the following questions is as follows (note the free parameters `N, K, D, A`):
    1.  For each user in MovieLens, take `N` ratings at random that are *known* (e.g. nonzero ratings) and replace them with 0. Save this altered data as a new matrix. Be sure to keep the original data around to evaluate your approach.
    2.  Use the `collaborative_filtering` function to impute values for this new matrix with `n_neighbors = K`, `distance_measure = D`, and `aggregator = A`. 
    3.  We now wish to evaluate the quality of the collaborative filter. For each rating that you imputed, do: (original_rating - imputed_rating) ** 2. Take the mean of all of these, and then take the square root of that. This is the mean squared error evaluation: error = sqrt(mean((r_i - rhat_i)^2)) where r_i is the original rating and rhat_i is the imputed rating, and i iterates over all of the ratings you replaced with 0.

    HINT: Write ONE function that takes in `(N, K, D, A)` as arguments and returns the error of a collaborative filter on the MovieLens dataset. You will be able to use this function for each of the following questions.

    WARNING: Some of these plots can take a very long time to generate as the collobarative filter process is *expensive*. Start early so your computations finish before the deadline! The runtime of the solution (run on a Macbook Pro 2018 laptop) is noted at the end of each question. One tip is to first run the experiments on a small subset of the data to make sure everything works, say just the first 100 users. Once everything works, move up to the entire dataset of 943 users.
   
    For this question, we will perform ablations (a term meaning the analysis of the effect of a free parameter on an algorithm) across `N`, the number of ratings we blank out per user. We wish to understand the effect of increasing N. Report the error of your collaborative filter for the values N = 1, 2, 4, and 8. Keep K, D, and A fixed at 3, `'euclidean'`, and `'mean'`, respectively. Report the error via a plot. On the x-axis should be the value of N and on the y-axis should be the mean squared error of imputating missing values. What happens as N increases?

    (Estimated runtime: 95 seconds)
    
9. (0.25 points) For this question, we will perform ablations across values of D, the distance measure we use to compare users. Report the error of your collaborative filter via a table. For each possible distance measure, report the error of the filter. Keep N, K, and A fixed at 1, 3, and `'mean'`, respectively. Report the error for each possible distance measure `'euclidean'`, `'cosine'`, and `'manhattan'` distance. (Estimated runtime: 52 seconds)
    
10. (0.25 points) Once you find the best performing distance measure, we will now perform ablations across values of K. Report the error of your collaborative filter via a plot. On the x-axis should be the value of K and on the y-axis should be the mean squared error of the filter. Do this for K = 1, 3, 7, 11, 15, 31. Keep N, D, and A fixed at 1, the best performing distance measure found in the previous question, and `'mean'`, respectively. (Estimated runtime: 95 seconds)
    
11. (0.25 points) Finally, we perform ablations across the type of aggregator used. Report the error of your collaborative filter via a table. For each possible aggregator, report the error of the filter. Keep N, D, and K fixed at 1, the best performing distance measure you found, and the best performing value of K that you found, respectively. Set A to be either `'mean'`, `'mode'`, or `'median'`. (Estimated runtime: 110 seconds)
    
12. (0.5 points) Now, discuss your results. What were the best settings you found for D, A, and K? For D, why do you think that distance measure worked best? For A, what about the best setting made it more suitable for your dataset? How did the value of K affect your results? Engage with the results of your experiments.