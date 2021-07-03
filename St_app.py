import streamlit as ST
import pickle
import numpy as np
from PIL import Image
import time
import pandas as pd

image=Image.open("Sidebar_Image.png")
ST.sidebar.image(image,use_column_width=True)


menu=ST.sidebar.radio("",['Home','Diabetes Predictor','Heart Disease Predictor','Kidney Disease Predictor','Liver Disease Predictor','About'])
if menu=='Home':
    ST.title('MediCheckup')
    ST.subheader('A Medical Checkup Health App')
    image=Image.open("Home_Image1.jpg")
    ST.image(image,use_column_width=True)

    #ST.beta_expander('Expander')
    with ST.beta_expander('How this app works?'):
        ST.write("This app identifies diseases like diabetes, heart disease, Kidney disease and Liver disease.")
        ST.write("◼️ Enter Required fields related with particular disease. ")
        ST.write("◼️ Click on Predict button, a machine learning or deep learning model will predict or detect the disease and generate the disease status.")
        ST.write("◼️ See your disease status and take precautionary measures. ")
    ST.header("Creator:")
    ST.write("** Syed Saad Ali **")
if menu=='Diabetes Predictor':
    # Diabetes Predictor
    image=Image.open("Diabetes-Predictor-main/Application_Logo.png")
    ST.image(image,use_column_width=True)


    filename1 = 'Diabetes-Predictor-main/diabetes-prediction-rfc-model.pkl'
    classifier = pickle.load(open(filename1, 'rb'))



    preg=ST.number_input("Number of Pregnancies: eg. 0",min_value=0,value=0,step=1,format="%d")
    glucose=ST.number_input("Glucose (mg/dL): eg. 80",min_value=0,value=0,step=1,format="%d")
    bp=ST.number_input("Blood Pressure (mm Hg): eg. 80",min_value=0,value=0,step=1,format="%d")
    st=ST.number_input("Skin Thickness (mm): eg. 20",min_value=0,value=0,step=1,format="%d")
    insulin=ST.number_input("Insulin Level (mu U/ml): eg. 80",min_value=0,value=0,step=1,format="%d")
    bmi=ST.number_input("Body Mass Index (kg/m²): eg. 24.1")
    dpf=ST.number_input("Diabetes Pedigree Function: eg. 1.4")
    age=ST.number_input("Age (years): eg. 40",min_value=0,value=0,step=1,format="%d")




    data = np.array([[preg, glucose, bp, st, insulin, bmi, dpf, age]])
    my_prediction = classifier.predict(data)
    if ST.button("Predict"):
        my_bar = ST.progress(0)
        for percent_complete in range(100):
            time.sleep(0.01)
            my_bar.progress(percent_complete + 1)

        if my_prediction==1:
            ST.info("OOPS! you have diabetes")
            image=Image.open("Diabetes-Predictor-main/Diabetes_Sad.png")
            ST.image(image,use_column_width=True)
        
        else:
            ST.info("Great! you don't have diabetes")
            image=Image.open("Diabetes-Predictor-main/No_Diabetes_Happy.png")
            ST.image(image,use_column_width=True)


# Heart Disease
if menu=='Heart Disease Predictor':
    image=Image.open("Heart-Disease-Prediction/Application_Logo.png")
    ST.image(image,use_column_width=True)

    filename2 = 'Heart-Disease-Prediction/Heart-Disease-Prediction-rfc-model.pkl'
    lr= pickle.load(open(filename2, 'rb'))
    
    age=ST.number_input("Age (Years) eg. 35",min_value=0,value=0,step=1,format="%d")
    sex=ST.number_input("Sex: 1=Male, 0=Female",min_value=0,value=0,step=1,format="%d")
    cp=ST.number_input("Chest Pain Type: eg. 0",min_value=0,value=0,step=1,format="%d")
    trestbps=ST.number_input("Resting Blood Pressure (mm Hg): eg. 99")
    chol=ST.number_input("Cholestrol (mg/dL): eg. 130")
    restecg=ST.number_input("resting electrocardiographic results: eg. 0",min_value=0,value=0,step=1,format="%d")
    thalac=ST.number_input("thalac: eg. 80",min_value=0,value=0,step=1,format="%d")
    exang=ST.number_input("exang: eg. 0",min_value=0,value=0,step=1,format="%d")
    oldpeak=ST.number_input("oldpeak")
    slope=ST.number_input("slope: eg. 0",min_value=0,value=0,step=1,format="%d")
    thal=ST.number_input("thal: eg. 3",min_value=0,value=0,step=1,format="%d")


    



    data2= np.array([[age,sex,cp,trestbps,chol,restecg,thalac,exang,oldpeak,slope,thal]])
    
    #ST.write(data2)
    my_prediction2 =lr.predict(data2)
    if ST.button("Predict"):
        my_bar = ST.progress(0)
        for percent_complete in range(100):
            time.sleep(0.01)
            my_bar.progress(percent_complete + 1)

        if my_prediction2==1:
            ST.info("OOPS! you have Heart Disease")
            image=Image.open("Heart-Disease-Prediction/Sad_Image.png")
            ST.image(image,use_column_width=True)
        else:
            ST.info("Great! you don't have Heart Disease")
            image=Image.open("Heart-Disease-Prediction/Happy_Image.png")
            ST.image(image,use_column_width=True)

if menu=='Kidney Disease Predictor':

    image=Image.open("Kidney-Disease-Prediction/Kidney_Logo.png")
    ST.image(image,use_column_width=True)


    filename3 = 'Kidney-Disease-Prediction/kidney_model.pkl'
    m1= pickle.load(open(filename3, 'rb'))


    Blood_Pressure=ST.number_input("Blood Pressure (mm Hg) eg:80 ")
    Specific_Gravity=ST.number_input("Specific Gravity() eg: 1.01")
    Albumin=ST.number_input("Albumin(g/dL) eg: 3.00")
    Blood_Sugar_Level=ST.number_input("Blood Sugar Level() eg: 1.0")
    Red_Blood_Cells_Count=ST.number_input("Red Blood Cells Count()  eg: 0(abnormal) or 1(normal)")
    Pus_Cell_Count=ST.number_input("Pus_Cell_Count eg: 0(abnormal) or 1(normal)")
    Pus_Cell_Clump=ST.number_input("Pus Cell Clump eg: 0(present) or 1(not present)")

    data3= np.array([[Blood_Pressure,Specific_Gravity,Albumin,Blood_Sugar_Level,Red_Blood_Cells_Count,Pus_Cell_Count,Pus_Cell_Clump]])
    my_prediction3 =m1.predict(data3)
    if ST.button("Predict"):
        my_bar = ST.progress(0)
        for percent_complete in range(100):
            time.sleep(0.01)
            my_bar.progress(percent_complete + 1)
        ST.write("Your entered data:")
        df= pd.DataFrame(data3)
        ST.table(df)
        if my_prediction3==1:
            ST.info("OOPS! you have Kidney Disease")
            #image=Image.open("Heart-Disease-Prediction\\Sad_Image.png")
            #ST.image(image,use_column_width=True)
        else:
            ST.info("Great! you don't have Kidney Disease")
            #image=Image.open("Heart-Disease-Prediction\\Happy_Image.png")
            #ST.image(image,use_column_width=True)



if menu=='Liver Disease Predictor':
    image=Image.open("Liver-Disease-Prediction/Liver_Logo.png")
    ST.image(image,use_column_width=True)

    filename4 = 'Liver-Disease-Prediction/Liver-Disease-Model.pkl'
    m2= pickle.load(open(filename4, 'rb'))
    
    Total_Bilirubin=ST.number_input("Total_Bilirubin (mg/dL) eg: 0.9")
    Direct_Bilirubin=ST.number_input("Direct_Bilirubin (mg/dL) eg: 0.2")
    Alkaline_Phosphotase=ST.number_input("Alkaline_Phosphotase (IU/L) eg: 290")
    Alamine_Aminotransferase=ST.number_input("Alamine_Aminotransferase (IU/L) eg: 22")
    Total_Protiens=ST.number_input("Total_Protiens (g/dL) eg: 4.8")
    Albumin=ST.number_input("Albumin (g/dL) eg: 3.2")
    Albumin_and_Globulin_Ratio=ST.number_input("Albumin_and_Globulin_Ratio (A/G ratio) eg: 1.2")



    data4=np.array([[Total_Bilirubin,Direct_Bilirubin,Alkaline_Phosphotase,Alamine_Aminotransferase,Total_Protiens,Albumin,Albumin_and_Globulin_Ratio]])

    my_prediction4 =m2.predict(data4)
    if ST.button("Predict"):
        my_bar = ST.progress(0)
        for percent_complete in range(100):
            time.sleep(0.01)
            my_bar.progress(percent_complete + 1)

        if my_prediction4==1:
            ST.info("OOPS! you have Kidney Disease")
            #image=Image.open("Heart-Disease-Prediction\\Sad_Image.png")
            #ST.image(image,use_column_width=True)
        else:
            ST.info("Great! you don't have Kidney Disease")
            #image=Image.open("Heart-Disease-Prediction\\Happy_Image.png")
            #ST.image(image,use_column_width=True)


if menu=='About':
    ST.header("** Details: **")
    ST.subheader("This is a basic machine learning and deep learning based medical app.")
    ST.write("The prediction about the disease is made with the help of the machine learning model which itself is trained on the thousands of the datasets.")
    ST.write("So with the following paragraph I gonna be describing about the types of the diseases which gonna be getting employed in this app. \n ")
    ST.header("1. Diabetes:")
    image=Image.open("diabetes.jpg")
    ST.image(image,use_column_width=True)
    ST.write("Diabetes is a disease that occurs when your blood glucose, also called blood sugar, is too high. Blood glucose is your main source of energy and comes from the food you eat. Insulin, a hormone made by the pancreas, helps glucose from food get into your cells to be used for energy.")
    ST.markdown("**What health problems can people with diabetes develop? **")
    ST.write("Over time, high blood glucose leads to problems such as")
    ST.write("◼️ heart disease")
    ST.write("◼️ stroke")
    ST.write("◼️ kidney disease")
    ST.write("◼️ eye problems")
    ST.write("◼️ dental disease")
    ST.write("◼️ nerve damage")
    ST.write("◼️ foot problems")

    ST.header("2. Heart Disease:")
    image=Image.open("heart.jpg")
    ST.image(image,use_column_width=True)
    ST.markdown("** Overview: **")
    ST.write("""Heart disease describes a range of conditions that affect your heart. Diseases under the heart disease umbrella include blood vessel diseases, such as coronary artery disease; heart rhythm problems (arrhythmias); and heart defects you're born with (congenital heart defects), among others. The term "heart disease" is often used interchangeably with the term "cardiovascular disease." Cardiovascular disease generally refers to conditions that involve narrowed or blocked blood vessels that can lead to a heart attack, chest pain (angina) or stroke. Other heart conditions, such as those that affect your heart's muscle, valves or rhythm, also are considered forms of heart disease. Many forms of heart disease can be prevented or treated with healthy lifestyle choices.""")
    ST.markdown("** Symptoms: **")
    ST.write("◼️ Chest pain, chest tightness, chest pressure and chest discomfort (angina) ")
    ST.write("◼️ Shortness of breath")
    ST.write("◼️ Pain, numbness, weakness or coldness in your legs or arms if the blood vessels in those parts of your body are narrowed")
    ST.write("◼️ Pain in the neck, jaw, throat, upper abdomen or back")
    ST.header("3. Kidney Disease:")
    
    image=Image.open("kidney.jpeg")
    ST.image(image,use_column_width=True)
    ST.markdown("** Overview: **")
    ST.write("""The kidneys play key roles in body function, not only by filtering the blood and getting rid of waste products, but also by balancing the electrolyte levels in the body, controlling blood pressure, and stimulating the production of red blood cells.
    The kidneys are located in the abdomen toward the back, normally one on each side of the spine. They get their blood supply through the renal arteries directly from the aorta and send blood back to the heart via the renal veins to the vena cava. (The term "renal" is derived from the Latin name for kidney.)""")
    ST.write("◼️ Lethargy")
    ST.write("◼️ Weakness")
    ST.write("◼️ Shortness of breath")
    ST.write("◼️ Generalized swelling (edema)")
    ST.write("◼️ Generalized weakness due to anemia")
    ST.write("◼️ Loss of appetite")
    ST.write("◼️ Lethargy")
    ST.write("◼️ Fatigue")
    ST.write("◼️ Congestive heart failure")
    ST.write("◼️ Metabolic acidosis")
    ST.write("◼️ High blood potassium (hyperkalemia)")
    ST.write("◼️ Fatal heart rhythm disturbances (arrhythmias) including ventricular tachycardia and ventricular fibrillation")
    ST.write("""◼️ Rising urea levels in the blood (uremia) may lead to brain encephalopathy, pericarditis (inflammation of the heart lining), or low calcium blood levels (hypocalcemia)""")

    ST.header("4. Liver Disease:")
    image=Image.open("liver.jpg")
    ST.image(image,use_column_width=True)
    ST.markdown("** Overview: **")
    ST.write("""Liver disease is any disturbance of liver function that causes illness. The liver is responsible for many critical functions within the body and should it become diseased or injured, the loss of those functions can cause significant damage to the body. Liver disease is also referred to as hepatic disease.
    Liver disease is a broad term that covers all the potential problems that cause the liver to fail to perform its designated functions. Usually, more than 75% or three quarters of liver tissue needs to be affected before a decrease in function occurs.""")
    ST.markdown("** Symptoms: **")
    ST.write("Classic symptoms of liver disease include:")
    ST.write("◼️ nausea")
    ST.write("◼️ vomiting")
    ST.write("◼️ right upper quadrant abdominal pain, and ")
    ST.write("◼️ jaundice (a yellow discoloration of the skin due to elevated bilirubin concentrations in the bloodstream).")

   

    





