# Lesson 13 Reading

Navigation | [Past Reading](../Read-12/README.md) | [Home Page](../README.md) | [Next Reading](../Read-14/README.md) |

## How to Run Linear Regression in Python

[Source](http://bigdata-madesimple.com/how-to-run-linear-regression-in-python-scikit-learn/)

Linear regression is probably one of the most important and widely used regression techniques. Itβs among the simplest regression methods. One of its main advantages is the ease of interpreting results.

### Problem Formulation

When implementing linear regression of some dependent variable π¦ on the set of independent variables π± = (π₯β, β¦, π₯α΅£), where π is the number of predictors, you assume a linear relationship between π¦ and π±: π¦ = π½β + π½βπ₯β + β― + π½α΅£π₯α΅£ + π. This equation is the regression equation. π½β, π½β, β¦, π½α΅£ are the regression coefficients, and π is the random error.

Linear regression calculates the estimators of the regression coefficients or simply the predicted weights, denoted with πβ, πβ, β¦, πα΅£. They define the estimated regression function π(π±) = πβ + πβπ₯β + β― + πα΅£π₯α΅£. This function should capture the dependencies between the inputs and output sufficiently well.

The estimated or predicted response, π(π±α΅’), for each observation π = 1, β¦, π, should be as close as possible to the corresponding actual response π¦α΅’. The differences π¦α΅’ - π(π±α΅’) for all observations π = 1, β¦, π, are called the residuals. Regression is about determining the best predicted weights, that is the weights corresponding to the smallest residuals.

To get the best weights, you usually minimize the sum of squared residuals (SSR) for all observations π = 1, β¦, π: SSR = Ξ£α΅’(π¦α΅’ - π(π±α΅’))Β². This approach is called the method of ordinary least squares.

Regression Performance
The variation of actual responses π¦α΅’, π = 1, β¦, π, occurs partly due to the dependence on the predictors π±α΅’. However, there is also an additional inherent variance of the output.

The coefficient of determination, denoted as πΒ², tells you which amount of variation in π¦ can be explained by the dependence on π± using the particular regression model. Larger πΒ² indicates a better fit and means that the model can better explain the variation of the output with different inputs.

The value πΒ² = 1 corresponds to SSR = 0, that is to the perfect fit since the values of predicted and actual responses fit completely to each other.

Simple Linear Regression
Simple or single-variate linear regression is the simplest case of linear regression with a single independent variable, π± = π₯.

When implementing simple linear regression, you typically start with a given set of input-output (π₯-π¦) pairs (green circles). These pairs are your observations. For example, the leftmost observation (green circle) has the input π₯ = 5 and the actual output (response) π¦ = 5. The next one has π₯ = 15 and π¦ = 20, and so on.

The estimated regression function (black line) has the equation π(π₯) = πβ + πβπ₯. Your goal is to calculate the optimal values of the predicted weights πβ and πβ that minimize SSR and determine the estimated regression function. The value of πβ, also called the intercept, shows the point where the estimated regression line crosses the π¦ axis. It is the value of the estimated response π(π₯) for π₯ = 0. The value of πβ determines the slope of the estimated regression line.

The predicted responses (red squares) are the points on the regression line that correspond to the input values. For example, for the input π₯ = 5, the predicted response is π(5) = 8.33 (represented with the leftmost red square).

The residuals (vertical dashed gray lines) can be calculated as π¦α΅’ - π(π±α΅’) = π¦α΅’ - πβ - πβπ₯α΅’ for π = 1, β¦, π. They are the distances between the green circles and red squares. When you implement linear regression, you are actually trying to minimize these distances and make the red squares as close to the predefined green circles as possible.

Simple Linear Regression With scikit-learn
Letβs start with the simplest case, which is simple linear regression.

There are five basic steps when youβre implementing linear regression:

Import the packages and classes you need.
Provide data to work with and eventually do appropriate transformations.
Create a regression model and fit it with existing data.
Check the results of model fitting to know whether the model is satisfactory.
Apply the model for predictions.
These steps are more or less general for most of the regression approaches and implementations.

### Step 1: Import packages and classes

The first step is to import the package numpy and the class LinearRegression from sklearn.linear_model:

    import numpy as np
    from sklearn.model_selection import LinearRegression

Now, you have all the functionalities you need to implement linear regression.

The fundamental data type of NumPy is the array type called numpy.ndarray. The rest of this article uses the term array to refer to instances of the type numpy.ndarray.

The class sklearn.model_selection.LinearRegression will be used to perform linear and polynomial regression and make predictions accordingly.

### Step 2: Provide data

The second step is defining data to work with. The inputs (regressors, π₯) and output (predictor, π¦) should be arrays (the instances of the class numpy.ndarray) or similar objects. This is the simplest way of providing data for regression:

    x = np.array([5, 15, 25, 35, 45, 55]).reshape((-1, 1))
    y = np.array([5, 20, 14, 32, 22, 38])

Now, you have two arrays: the input x and output y. You should call .reshape() on x because this array is required to be two-dimensional, or to be more precise, to have one column and as many rows as necessary. Thatβs exactly what the argument (-1, 1) of .reshape() specifies.

This is how x and y look now:

    >>> print(x)
    [[ 5]
    [15]
    [25]
    [35]
    [45]
    [55]]
    >>> print(y)
    [ 5 20 14 32 22 38]

As you can see, x has two dimensions, and x.shape is (6, 1), while y has a single dimension, and y.shape is (6,).

### Step 3: Create a model and fit it

The next step is to create a linear regression model and fit it using the existing data.

Letβs create an instance of the class LinearRegression, which will represent the regression model:

    model = LinearRegression()

This statement creates the variable model as the instance of LinearRegression. You can provide several optional parameters to LinearRegression:

fit_intercept is a Boolean (True by default) that decides whether to calculate the intercept πβ (True) or consider it equal to zero (False).
normalize is a Boolean (False by default) that decides whether to normalize the input variables (True) or not (False).
copy_X is a Boolean (True by default) that decides whether to copy (True) or overwrite the input variables (False).
n_jobs is an integer or None (default) and represents the number of jobs used in parallel computation. None usually means one job and -1 to use all processors.
This example uses the default values of all parameters.

Itβs time to start using the model. First, you need to call .fit() on model:

    model.fit(x, y)

With .fit(), you calculate the optimal values of the weights πβ and πβ, using the existing input and output (x and y) as the arguments. In other words, .fit() fits the model. It returns self, which is the variable model itself. Thatβs why you can replace the last two statements with this one:

    model = LinearRegression().fit(x, y)

This statement does the same thing as the previous two. Itβs just shorter.

### Step 4: Get results

Once you have your model fitted, you can get the results to check whether the model works satisfactorily and interpret it.

You can obtain the coefficient of determination (πΒ²) with .score() called on model:

    >>> r_sq = model.score(x, y)
    >>> print('coefficient of determination:', r_sq)
    coefficient of determination: 0.715875613747954

When youβre applying .score(), the arguments are also the predictor x and regressor y, and the return value is πΒ².

The attributes of model are .intercept_, which represents the coefficient, πβ and .coef_, which represents πβ:

    >>> print('intercept:', model.intercept_)
    intercept: 5.633333333333329
    >>> print('slope:', model.coef_)
    slope: [0.54]

The code above illustrates how to get πβ and πβ. You can notice that .intercept_is a scalar, while .coef_ is an array.

The value πβ = 5.63 (approximately) illustrates that your model predicts the response 5.63 when π₯ is zero. The value πβ = 0.54 means that the predicted response rises by 0.54 when π₯ is increased by one.

You should notice that you can provide y as a two-dimensional array as well. In this case, youβll get a similar result. This is how it might look:

    >>> new_model = LinearRegression().fit(x, y.reshape((-1, 1)))
    >>> print('intercept:', new_model.intercept_)
    intercept: [5.63333333]
    >>> print('slope:', new_model.coef_)
    slope: [[0.54]]

As you can see, this example is very similar to the previous one, but in this case, .intercept_is a one-dimensional array with the single element πβ, and .coef_ is a two-dimensional array with the single element πβ.

### Step 5: Predict response

Once there is a satisfactory model, you can use it for predictions with either existing or new data.

To obtain the predicted response, use .predict():

    >>> y_pred = model.predict(x)
    >>> print('predicted response:', y_pred, sep='\n')
    predicted response:
    [ 8.33333333 13.73333333 19.13333333 24.53333333 29.93333333 35.33333333]
    When applying .predict(), you pass the regressor as the argument and get the corresponding predicted response.

    This is a nearly identical way to predict the response:

    >>> y_pred = model.intercept_+ model.coef_ * x
    >>> print('predicted response:', y_pred, sep='\n')
    predicted response:
    [[ 8.33333333]
    [13.73333333]
    [19.13333333]
    [24.53333333]
    [29.93333333]
    [35.33333333]]

In this case, you multiply each element of x with model.coef_and add model.intercept_ to the product.

The output here differs from the previous example only in dimensions. The predicted response is now a two-dimensional array, while in the previous case, it had one dimension.

If you reduce the number of dimensions of x to one, these two approaches will yield the same result. You can do this by replacing x with x.reshape(-1), x.flatten(), or x.ravel() when multiplying it with model.coef_.

In practice, regression models are often applied for forecasts. This means that you can use fitted models to calculate the outputs based on some other, new inputs:

    >>> x_new = np.arange(5).reshape((-1, 1))
    >>> print(x_new)
    [[0]
    [1]
    [2]
    [3]
    [4]]
    >>> y_new = model.predict(x_new)
    >>> print(y_new)
    [5.63333333 6.17333333 6.71333333 7.25333333 7.79333333]

Here .predict() is applied to the new regressor x_new and yields the response y_new. This example conveniently uses arange() from numpy to generate an array with the elements from 0 (inclusive) to 5 (exclusive), that is 0, 1, 2, 3, and 4.
