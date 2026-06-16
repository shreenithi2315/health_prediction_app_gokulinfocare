from datetime import date

import streamlit as st

from db import add_patient, get_all_patients, update_patient, delete_patient
from predictor import get_prediction
st.title("Health Prediction App")
st.subheader("Enter Patient Details")

full_name = st.text_input("Full Name")
dob = st.date_input("Date of Birth")
email = st.text_input("Email")
glucose = st.number_input("Glucose (mg/dL)", min_value=0.0)
haemoglobin = st.number_input("Haemoglobin (g/dL)", min_value=0.0)
cholesterol = st.number_input("Cholesterol (mg/dL)", min_value=0.0)

if st.button("Add Patient"):
    if full_name == "":
        st.error("Please enter the patient's full name")
    elif "@" not in email or email == "":
        st.error("Please enter a valid email address")
    elif dob > date.today():
        st.error("Date of birth cannot be a future date")
    elif glucose == 0.0 or haemoglobin == 0.0 or cholesterol == 0.0:
        st.error("Please enter valid blood test values")
    else:
        remarks = get_prediction(full_name, glucose, haemoglobin, cholesterol)
        add_patient(full_name,str(dob), email, glucose, haemoglobin, cholesterol, remarks)
        st.success("Patient added successfully")
        st.write("Remarks:", remarks)
st.subheader("Patient Records")
patients = get_all_patients()
search = st.text_input("search the name")

if len(patients) == 0:
    st.write("No patients record")
else:
    if search != "":
        patients = [p for p in patients if search.lower() in p[1].lower()]
    import pandas as pd
    df = pd.DataFrame(patients, columns=["ID", "Full Name", "Date of Birth", "Email", "Glucose", "Haemoglobin", "Cholesterol", "Remarks"])
    st.dataframe(df)

st.subheader("Update Patient")
patients = get_all_patients()
patient_options = []
for patient in patients:
    patient_options.append(str(patient[0]) + " - " + patient[1])
selected = st.selectbox("Select patient ", patient_options)
for patient in patients:
    if selected.startswith(str(patient[0])):
        selected_data = patient
        break
updated_name = st.text_input("Full Name", value=selected_data[1])
updated_dob = st.date_input("Date of Birth", value=date.fromisoformat(selected_data[2]))
updated_email = st.text_input("Email", value=selected_data[3])
updated_glucose = st.number_input("Glucose (mg/dL)", min_value=0.0, value=selected_data[4])
updated_haemoglobin = st.number_input("Haemoglobin (g/dL)", min_value=0.0, value=selected_data[5])
updated_cholesterol = st.number_input("Cholesterol (mg/dL)", min_value=0.0, value=selected_data[6])

if st.button("Update Patient"):
    if updated_name == "":
        st.error("Please enter the patient full name")
    elif "@" not in updated_email or updated_email == "":
        st.error("Please enter a valid email address")
    elif updated_dob > date.today():
        st.error("Date of birth cannot be a future date")
    elif updated_glucose == 0.0 or updated_haemoglobin == 0.0 or updated_cholesterol == 0.0:
        st.error("Please enter valid blood test values")
    else:
        update_patient(selected_data[0], updated_name, str(updated_dob), updated_email, updated_glucose, updated_haemoglobin, updated_cholesterol, selected_data[7])
        st.success("Patient updated successfully")
    
st.subheader("Delete Patient")
patients = get_all_patients()
deletelist = []
for patient in patients:
    deletelist.append(str(patient[0]) + " - " + patient[1])
selected_del = st.selectbox("Select patient to delete", deletelist)

if st.button("Delete patient"):
    for patient in patients:
        if selected_del.startswith(str(patient[0])):
            delete_patient(patient[0])
            st.success("Patient deleted successfully")
            break
