import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle
pd.options.display.max_columns = None

df = pd.read_csv("FuelConsumption.csv.txt")
df = df[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB','CO2EMISSIONS']].copy(deep=True)

x = df.iloc[:,:3]
y = df.iloc[:,-1]
regressor = LinearRegression()

regressor.fit(x,y)
pickle.dump(regressor, open('model.pkl','wb'))

model = pickle.load(open('model.pkl','rb'))
print(model.predict([[2.6, 8, 10.1]]))


