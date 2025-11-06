from django.shortcuts import render

from joblib import load
model=load("./SavedModel/model.joblib")

def predict(request):
    if request.method == 'POST':
        Pregnancy = float(request.POST['Pregnancy'])
        Glucose = float(request.POST['Glucose'])
        BloodPressure = float(request.POST['BloodPressure'])
        SkinThickness = float(request.POST['SkinThickness'])
        Insulin = float(request.POST['Insulin'])
        BMI = float(request.POST['BMI'])
        DiabetesPedigreeFunction = float(request.POST['DiabetesPedigreeFunction'])
        Age = float(request.POST['Age'])
        prediction = model.predict([[Pregnancy, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        if prediction[0] == 0:
            prediction = "No Diabetes"
        else:
            prediction = "You are diabetic"
        return render(request, 'index.html', {'result': prediction})
    return render(request, 'index.html')


