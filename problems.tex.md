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

6. (O.5 points) The effectiveness of a KNN regressor is affected by the value of K that you choose and the number of data points it has available. Use the <"regress on me"> data set. Split it into <how many?> training and <how many?> testing points. Use a Euclidean distance measure for your regressor.  Now, fit the data using K = 1, K = 2, K = 4, K = 8. Which one performed best, as measured with sum-of-squared-errors on the testing set? Repeat the experiment with the testing and training set flipped. How did this change things?

7. (0.5 points) The effectiveness of a KNN  regressor is affected by the distance measure chosen. Let's explore how changing the value of $p$ in a $L^p$ norm affects the effectiveness in a K-nearest regressor.  <assign some problem to do so>
   
8. 
