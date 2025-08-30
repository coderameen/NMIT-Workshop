import pandas as pd
df = pd.read_csv("pizza_dataset.csv")
print(df.head())

# To check missing or null value
print(df.isnull().sum())

#Split into X and y axis(input and output)
X = df.drop(columns='eat_pizza', axis=1)
# X = df.iloc[:,:-1]

y = df['eat_pizza']
# y = df.iloc[:,-1]

#Call model
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()

#train model
model.fit(X,y)

#prediction
age = int(input("Enter your age: "))
weight = int(input("Enter your weight"))
pred = model.predict([[age,weight]])
print(pred[0])
if pred[0] == 1:
    print("Enjoy Pizzaaa....")
else:
    print("Go to GYM...")


#Save the Model
import pickle
pickle.dump(model,open('pizza_model.pkl','wb'))