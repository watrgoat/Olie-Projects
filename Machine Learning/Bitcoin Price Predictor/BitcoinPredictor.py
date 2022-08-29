import pandas as pd
import matplotlib.pyplot as plt
import sklearn
from sklearn.ensemble import RandomForestRegressor


training = pd.read_csv("bitcoin_price_Training - Training.csv")
test = pd.read_csv("bitcoin_price_1week_Test - Test.csv")
training = training.iloc[::-1]
test = test.iloc[::-1]

training['Date'] = pd.to_datetime(training['Date'], infer_datetime_format=True)
training['year'] = pd.DatetimeIndex(training['Date']).year
training['month'] = pd.DatetimeIndex(training['Date']).month
training['day'] = pd.DatetimeIndex(training['Date']).day
test['Date'] = pd.to_datetime(test['Date'], infer_datetime_format=True)
test['year'] = pd.DatetimeIndex(test['Date']).year
test['month'] = pd.DatetimeIndex(test['Date']).month
test['day'] = pd.DatetimeIndex(test['Date']).day

training = training.replace(',','', regex=True)
training_mean = training.loc[training['Volume'] != '-', 'Volume']
training_mean = pd.to_numeric(training_mean)
training_mean = training_mean.mean()
training['Volume'] = training['Volume'].replace('-',training_mean, regex=True)
training['Volume'] = training['Volume'].astype('int64')
training['Market Cap'] = training['Market Cap'].astype('int64')

test = test.replace(',','', regex=True)
test['Volume'] = test['Volume'].astype('int64')
test['Market Cap'] = test['Market Cap'].astype('int64')

training = training.drop(columns='Date')
test = test.drop(columns='Date')

training = training.drop()

y_train = training['Open']
X_train = training.drop(columns='Open')
y_test = test['Open']
X_test = test.drop(columns='Open')

#print(training.describe())
#print(training.info())


#plt.plot_date(training["Date"], training['Open'])
#plt.show()

regressor = RandomForestRegressor(random_state=1)
regressor.fit(X_train, y_train)
predictions = regressor.predict((X_test))

from sklearn.metrics import r2_score, mean_squared_error

print(mean_squared_error(y_test, predictions, squared=False))

plt.scatter(predictions, y_test)
plt.show()

# stuff todo
# try cutting out old data
# try different value for extra volume
# try different mode (xgboost, gradientforest, neural network)
# test data for more than 1 week
# standard deviation of last 30 days