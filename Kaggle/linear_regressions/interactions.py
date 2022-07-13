from vg_stats.vg_stats import nump, panda, train_test_split, LinearRegression,plot

# import data
df = panda.read_csv("../input/salary/Salary.csv")
df

# Set x axis data
x = df["YearsExperience"].values
x

# Set y axis data
y = df["Salary"].values
y

# Data extraction & Shaping
x_train, x_test, y_train, y_test = train_test_split(
    x, y, train_size=0.8, test_size=0.2, random_state=12
)
x_train = x_train.reshape(-1, 1)
x_test = x_test.reshape(-1, 1)
x_train

# Linear Regression Model
model = LinearRegression()
model.fit(x_train, y_train)

# Predict the output by the regression model
y_predecit = model.predict(x_test.reshape(-1, 1))
y_predecit

train_occuracy = model.score(x_train, y_train)
train_occuracy

test_occuracy = model.score(x_test, y_test)
test_occuracy

# Prediction of salary based on length of experiences
new_data = nump.array([9]).reshape(-1, 1)
new_data

model.predict(new_data)

# Visualize Prediction
%matplotlib inline
plot.scatter(x,y, color = "blue")
plot.plot(x_test, y_predict, color='red', linewidth=2)
plot.xlabel('Experience Years')
plot.ylabel('Salary')
plot.title('Experience Years VS Salary')

# Visualize Prediction VS Actual
%matplotlib inline
plot.scatter(x_test,y_test, color = "blue")
plot.scatter(x_test,y_predict, color = "red")
plot.xlabel('Experience Years')
plot.ylabel('Salary')
plot.title('Experience Years VS Salary')