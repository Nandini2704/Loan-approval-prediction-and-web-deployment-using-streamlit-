import streamlit as st
import pandas as pd
import pickle as pk
import numpy as np
import PIL as image
pickle_in=open("loan_approval_rf.pkl","rb")
rf_model=pk.load(pickle_in)
def loan_approval(No_of_dependents, Education, Self_Employed, Loan_Amount,
       Loan_Term,Cibil_Score):
    prediction=rf_model.predict([[No_of_dependents, Education, Self_Employed, Loan_Amount,
       Loan_Term,Cibil_Score]])
    print(prediction)
    return prediction
def main():
    html_temp="""
    <div style="background-color:##B1DDF1;">
    <h1 style="color:white;text-align:center;font-size:50px;font-style:italic">Loan Approval Prediction</h1>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    No_of_dependents=st.number_input("No_of_dependents")
    Education=st.number_input("Education")
    Self_Employed=st.number_input("Self_Employed")
    Loan_Amount=st.number_input("Loan_Amount")
    Loan_Term=st.number_input("Loan_Term")
    Cibil_Score=st.number_input("Cibil_Score")
    result=""
    if st.button("Predict"):
        result=loan_approval(No_of_dependents, Education, Self_Employed, Loan_Amount,
       Loan_Term,Cibil_Score)
        if(result==0):
            result="Rejected"
            st.text(result)
        else:
            result="Approved"
            st.text(result)
if __name__=="__main__":
    main()
