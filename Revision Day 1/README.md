# **```Machine learning```**
Where computers being learned without explicitly programmed.

- **Explicit programming**: Learning using specific algorithms, providing with not a wide range of patterns. Underperformed by humans. 
- **Machine learning**: Depends on previous actions, experiences, and dataset.

&nbsp;

# **```Types of machine learning```**

1. Supervised learning
2. Unsupervised learning
3. Recommender system
4. Reinforcement Learning

&nbsp;

# **```Supervised learning```**

Supervised learning learn from data labeled with the "right answer".

**Usecases**:

1. Spam filtering
2. Speech recognition
3. Machine translation
4. Online advertising

## **```Supervised learning algorithms```**

### Types of values

1. Quantitative or Numerical values or data: Regression problem.
2. Qualitative or Categorical values: Classification problem.

### Numerical data  
In regression the predicted number doesn't bound to whole numbers. This could be any fractional number. 
1. **Discrete data**: Set of finite values in a specific range. 
2. **Continuous data**: Fractional values that can change over time. 

Depends on the aforementioned values or data supervised learning algorithms can be distributed into two major subclasses:

### **```1. Regression```**

**Predict a number (both discrete and continuous values), where could be infinitely many possible outputs.** Regression is a statistical method that helps us by understanding and predicting the relationship between feature (independent) and target (dependent) variables.

Regression analysis aims to establish a relationship between the independent variables (input features) and the dependent variable (output or target variable) to make accurate predictions.


### Regression types

- **Positive regression**: Independent variables increase affect positively or increase the value of dependent variables.
- **Negative regression**: Independent variables increase affect negatively or decrease the value of dependent variables. 

### Outlier
Outlier are those values that are different from rest of the values or data points. Too small or too large values that drastically increase or decrease the overall result.

Two types of variables are:

- **Independent variable (X)**: A variable whose value does not change by the effect of other variable and used to manipulate the dependent variables.
- **Dependent variable (Y)**: Changes happened when independent variables values are changed.

### Benefits of regression algorithm

1. Regression analysis help us determine whether a machine learning model is over-fitting or under-fitting. 


**```Types of regression algorithms```**

1. Linear regression
   1. Single variable or **univariate** linear regression
   2. Multiple linear regression
2. Logistic regression
3. Polynomial regression


**```Regression algorithms limitations or drawbacks```**

1. **Underperformed result for out-of-bound test data**: Regression models are not fit for predicting values outside the range of the training data, this is because the model has not been trained on such extreme or outlying value

### **```2. Classification```**

As classification problems works on categorical values. Categorical data can be represented as discrete numerical values by encoding the categories with integers or other numerical labels. Since categories are strictly represent a single value, and categorical values can't be broken into smaller fractions. 

1. Linear classifiers
2. Support Vector Machines (SVM)
3. Decision Trees
4. K-Nearest Neighbor (KNN)
5. Random Forest

&nbsp;

# **```Unsupervised learning or Clustering```**

Unlike supervised learning algorithms, the unsupervised learning dataset doesn't provided with any corresponding "output or right answers". This is because in unsupervised learning we're not intend to predict any result rather we'll make groups also known as clusters. 

- Algorithm has to determine pattern structure from the given dataset. 

## Types of unsupervised learning algorithms
- Clustering

&nbsp;

# Linear Regression

![](20240417171954.png)

Linear regression is a method that let us understand the relationship between dependent and independent variables. 
- **Usecase**: Prediction, Estimation, Forecasting, Hypothesis testing, and Modeling causal relationships.
- It predicts continuous value. example: y = mx + c
- y is target, x is independent feature, m is slope, c is intercept
- By training on many datapoints, the model understands value of c and m. Then taking any value x, the model can estimate the value y.
- Simple linear regression = Use 1 independent variable for predicting 1 dependent variable
- Multiple linear regression = Use multiple independent variables for predicting 1 dependent variable
- Noise : 
    - Error in prediction. 
    - The error is gaussian noise and the residuals show normal distribution properties. 
    - The more the error, the more spread out the normal distribution (sigma or standard deviation in normal distribution)
    - The best fit line has the least noise.
- We define an error function for m and c and choose the line that reduces the error and gain the optimized value for m and c
- Error function = loss function = cost function
- Residual = distance between datapoints and the fitted line
- Our loss function can be RSS (Residual Sum of Squares) the sum of the residuals and our goal is to minimize this value.
- metrics 
    - r-squared : percentage of the variance in target values explained by the features. range is 0 to 1
    - RMSE : Root Mean squared error (Average error in prediction)
- cross validation : do train-test process in multiple folds and take average to consolidate r-squared.
- Regularization : penalizes large co-efficients to reduce overfitting. Some regressions that uses regularization:
    - Lasso Regression
    - Ridge Regression
- Hyperparameter : Variables used to optimize model parameters

