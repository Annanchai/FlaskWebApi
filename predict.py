from flask import Flask, request
import pickle
import sklearn


app = Flask(__name__)
print(__name__)

model_pickle = open('./artefacts/classifier.pkl', 'rb')
clf = pickle.load(model_pickle)


@app.route('/predict', method=['POST'])
def prediction():
    loan_req = request.get_json ()
    if loan_req['Gender']=='Male':
        Gender = 0
    else:
        Gender = 1
        
    if loan_req['Married'] == 'Unmarried':
        Married = 0
    else:
        Married = 1
        
    if loan_req['Credit_History'] == 'Unclear Debts':
        Credit_History = 0
    else:
        Credit_History = 1
        
    ApplicantIncome = loan_req['ApplicantIncome']
    LoanAmount = loan_req['LoanAmount']
    
    result = clf.predict([[Gender, Married, ApplicantIncome, LoanAmount, Credit_History]])