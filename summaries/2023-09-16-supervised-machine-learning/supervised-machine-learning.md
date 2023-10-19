---
date: 2023-09-13
type: course
summary: "Supervised Machine Learning: Regression and Classification"
author: Andrew Ng
url: https://www.coursera.org/learn/advanced-learning-algorithms
---

It has been months since my last summary of AI-related content. I have certainly
read more articles and listened to more interviews since then, but I noticed I
was starting to experience diminishing returns with respect to how much I felt
like I was learning. This tends to be a signal for me that I need to dig a bit
deeper to start understanding the layer underneath all of the content I've been
taking in.

I found myself getting excited at the idea of taking an actual course. I really
haven't done that since grad school! I didn't spend much time trying to optimize
for the best possible course for me given my educational background, interests,
professional experience, etc. I figured no matter what, a starter course would
include a lot of redundant information I already knew but would set me on a path
towards a deeper understanding as long as I had the patience to stick with it.

After a very short search, I settled on a [Machine Learning Specialization][1]
series of courses on Coursera. The courses are taught by [Andrew Ng][2], a name
I already recognized from some of the self-guided learning I had been doing for
the previous several months. As of right now, I have completed the first course
in the series, called "Supervised Machine Learning: Regression and
Classification"; and I am in the middle of the second course, called "Advanced
Learning Algorithms".

I was a math minor in college, so much of the content of the first course felt
like a review of concepts I learned 20+ years ago. It actually made me a bit
nostalgic! I remember doing linear regression in high school: given a set of
points, find the best-fit line by minimizing the sum of squared distances from
the points to the line defined by a linear formula. This course covered the same
ground but from a programming lens, which was just fine by me.

My explanation of the topics covered, to check my understanding the Feynman way:

### Regression and classification

**Regression** is the process of producing a model for making _numerical_
predictions given a known data set. In the case of linear regression, the idea
is to find the terms in the linear formula `y = mx + b` (specifically m and b,
called _parameters_) that will produce the most accurate predictions for `y`
given `x`.

**Classification**, in contrast, produces _categorical_ predictions, e.g. "yes"
or "no" for whether a tumor is malignant; or "dog", "cat" etc. for identifying
the subject of a photo.

### Loss function

The best-fit line through a set of points is the one that minimizes the sum of
squared distances between the line and the points, using the [least squares]
[3] method. This is a special case of regression as a general concept, where a
model is defined by some parameters and those parameters are optimized to
minimize the "loss" of each of its predictions, i.e. how far off they are from
known correct values.

In linear regression, the **model** would be the formula defining the line. The
**parameters** would be `m` (slope of the line) and `b` (y-intercept), which are
all you need to define a straight line in a 2-dimensional space. And finally
the **loss function** is the sum of the squared distances between the points in
the data set and the corresponding points on the line (i.e. the ones with the
same `x` input values).

So in plain English, the loss function is a way of asking for any given model,
input, and known correct output, "How good was the model at producing this
output from this input?"

### Gradient descent

In regression, you produce a model to make predictions by minimizing the loss
function. Gradient descent is an algorithm for _how_ to actually do that. It is
basically making small changes to the parameters of a model until you've found
a set of values that minimize the cost (sum of losses) for an input data set.

In order to achieve the "descent" part, you need to take the derivative of the
loss function with respect to each parameter. This gives you a slope. You make
a small adjustment to each parameter in the direction of its respective slope.
Then you calculate the cost with this new set of parameter values and make sure
it has decreased.

The algorithm involves repeating this process until the cost isn't changing
significantly anymore. This indicates that you've reached a local minimum of
the cost function, which means you've identified optimal values for all of the
parameters of your model.

### Sigmoid function

The sigmoid function provides an alternative loss function for classification
problems and is used in **logistic regression**. This is a type of
classification where the possible values for a data point are binary, i.e. true
or false. Logistic regression can produce probabilistic predictions or
confidence levels, e.g. the probability of passing an exam based on hours spent
studying.

![Example Sigmoid function](/images/supervised-machine-learning-sigmoid-function.png)

Visually, the sigmoid function makes a smooth S-shaped curve between 0 and 1 on
the y-axis. This provides a model which can produce probabilities or confidence
levels in something being true or false based on the value of `x`.

Rather than the least squares method used in linear regression, the loss for a
given prediction is essentially the distance between the confidence level
provided by the model and the true value. For example, if the model predicts
with 95% confidence that a value will be true and it is true, the loss is 0.05.
If the model predicts with 95% confidence that a value will be true and it is
false, the loss is 0.95.

### Normalization

I understand the premise behind normalization but I'm honestly a little fuzzy on
the math.

For a model that takes multiple types of input ("features"), if the values of
those inputs have very different magnitudes, it is helpful to transform them to
have similar magnitudes. As an example, if one set of features falls within the
range 1-100, and another set of features falls within the range
10,000-1,000,000, you could take the second set and multiply by 0.001 so that
the ranges are closer together, and then reverse that transformation after
optimizing the model.

What I don't totally understand is why this is helpful. _Visually_, it makes
sense as a way to plot data in a more comprehensible way. I think normalization
allows for gradient descent to work more effectively on a model with multiple
parameters. I am not sure if this is truly the only way to achieve that or if
an alternate technique might be to use different values for alpha (rate of
descent) for different parameters.

### Regularization

As with normalization, the ideas behind regularization are also a bit blurry to
me.

If you have a model with a large number of parameters, it is possible that
through gradient descent you will arrive at a model that _overfits_ the
training data, i.e. it fits the data a bit too perfectly and then ends up
performing worse than expected on newer data. A really unscientific way of
thinking about this in my mind is that the model becomes "a little too close"
to its training data, which hurts its ability to generalize.

Regularization essentially forces the weights of parameters down so that they
have less influence on the model's predictions.

What is strange to me about regularization is that it feels like making a model
more complex in order to make it simpler. The simpler thing to do in my mind
would be to reduce the number of parameters in the model. But I think the idea
behind regularization is that you still want your parameters to _sort of_
affect the model's predictions, just _not too much_. It feels a bit to me like
just fiddling around with data.

I probably need to go back and learn more about this!

[1]: https://www.coursera.org/specializations/machine-learning-introduction
[2]: https://www.andrewng.org/
[3]: https://en.wikipedia.org/wiki/Least_squares
