from flask import Flask,render_template,request,redirect,send_from_directory
import mysql.connector
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split 
import joblib
import graphviz
from sklearn import tree
import folium

# # ===========================================================================================================
# df = pd.read_csv('heartdisease.csv')
# df = df.replace({'sex':{0:'Female',1:'Male'}})
# df = df.replace({'cp':{1:'typical angina',2:'atypical angine',3:'non-anginal pain',4:'asymptomatic'}})
# df = df.replace({'fbs':{0:'< 120 mg/dl',1:'> 120 mg/dl'}})
# df = df.replace({'restecg':{0:'normal',1:'having ST-T wave abnormality',2:'showing probable'}})
# df = df.replace({'exang':{1:'yes',0:'no'}})
# df = df.replace({'slope':{1:'upsloping',2:'flat',3:'downsloping'}})
# df = df.replace({'thal':{3:'normal',6:'fixed defect',7:'reversable defect',-100000:'normal'}})
# df = df.replace({'ca':{-100000:0}})
# # ============================================================================================================

# sex = LabelEncoder()
# df['Gender'] = sex.fit_transform(df['sex'])
# df.drop('sex',axis=1,inplace=True)
# chestPain = LabelEncoder()
# df['chestPain'] = chestPain.fit_transform(df['cp'])
# df.drop('cp',axis=1,inplace=True)
# bldsgr = LabelEncoder()
# df['bloodSugar'] = bldsgr.fit_transform(df['fbs'])
# df.drop('fbs',axis=1,inplace=True)
# graph = LabelEncoder()
# df['graph'] = graph.fit_transform(df['restecg'])
# df.drop('restecg',axis=1,inplace=True)
# exang = LabelEncoder()
# df['exe'] = exang.fit_transform(df['exang'])
# df.drop('exang',axis=1,inplace=True)
# slope = LabelEncoder()
# df['slopes'] = slope.fit_transform(df['slope'])
# df.drop('slope',axis=1,inplace=True)
# thall = LabelEncoder()
# df['thl'] = thall.fit_transform(df['thal'])
# df.drop('thal',axis=1,inplace=True)
# vessel = LabelEncoder()
# df['vessel'] = vessel.fit_transform(df['ca'])
# df.drop('ca',axis=1,inplace=True)

# x = df.drop('num',axis=1)
# y = df['num']
# xtr, xts, ytr, yts = train_test_split(
#     x,
#     y,
#     test_size=.05
# )
# model = LogisticRegression(solver='lbfgs',max_iter=1000)
# model.fit(xtr,ytr)
# # joblib.dump(model,'heartmodel')

# scoreLGR = model.score(xtr,ytr)
# print(scoreLGR*100)

# # ===========================================================================================

# from sklearn.tree import DecisionTreeClassifier
# modelTree = DecisionTreeClassifier()
# modelTree.fit(xtr,ytr)
# scoreTree = modelTree.score(xtr,ytr)
# print(scoreTree*100)

# # ===========================================================================================

# from sklearn.svm import SVC
# modelSVCP = SVC(kernel='poly',degree=8,gamma='scale')
# modelSVCP.fit(xtr,ytr)
# scoreSVCP = modelSVCP.score(xtr,ytr)
# print(scoreSVCP * 100)

# # ===========================================================================================

# modelSVCL = SVC(kernel='linear')
# modelSVCL.fit(xtr,ytr)
# scoreSVCL = modelSVCL.score(xtr,ytr)
# print(scoreSVCL * 100)

# # ============================================================================================

# modelSVCG = SVC(kernel='rbf',gamma='auto')
# modelSVCG.fit(xtr,ytr)
# scoreSVCG = modelSVCG.score(xtr,ytr)
# print(scoreSVCG * 100)


df = pd.read_excel('rumahsakit.xlsx')
# print(df.dtypes)
# print(type(df.lng[0]))

rs = []
almt = []
lat = []
lng = []

map = folium.Map(
    location= [-6.2295712,106.759478],
    zoom_start=12
)
for i in df['nama_rumah_sakit']:
    rs.append(i)
for i in df['alamat_rumah_sakit']:
    almt.append(i)
for i in df['lat']:
    lat.append(i)
for i in df['lng']:
    lng.append(i)

for i in range(len(df)):
    folium.Marker(
        [lat[i],lng[i]],
        popup=almt[i],
        tooltip=rs[i]
    ).add_to(map)

map.save('rs.html')

    
    

# map.save('rs.html')
    
