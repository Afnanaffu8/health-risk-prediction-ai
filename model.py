import pandas as pd
from sklearn.ensemble import RandomForestClassifier

data = pd.read_csv("dataset.csv")

X = data[['age', 'bmi', 'glucose', 'bp']]
y = data['risk']

model = RandomForestClassifier()
model.fit(X, y)

def predict_risk(age, bmi, glucose, bp):
    prob = model.predict_proba([[age, bmi, glucose, bp]])[0][1]
    percentage = round(prob * 100, 2)

    if percentage > 60:
        level = "High Risk"
    else:
        level = "Low Risk"

    return percentage, level