import json, os
os.makedirs("week06/data/raw", exist_ok=True)
os.makedirs("week06/data/processed", exist_ok=True)
os.makedirs("week06/reports", exist_ok=True)

open("week06/data/raw/students_messy.csv","w",encoding="utf-8").write("""student_id,name,program,city,attendance,assignment,midterm,final,admission_date
1001,Ali Khan,BSAI,Islamabad,85,78,72,81,2025-09-01
1002,Sara Ahmed,BS AI,islamabad,,88,68,75,01/09/2025
1003,Ahmed Raza,BSAI,Rawalpindi,92,80,missing,88,2025/09/01
1003,Ahmed Raza,BSAI,Rawalpindi,92,80,missing,88,2025/09/01
1004,Ayesha Noor,BSCS,Rwp,110,86,75,90,09-01-2025
1005,Hamza Ali, BS-AI,Islamabad,74,70,52,,2025-09-01
1006,Zainab Malik,BSDS,RAWALPINDI,81,91,84,93,2025-09-02
1007,Usman Tariq,AI,Islamabad,69,60,48,55,September 3 2025
1008,Maryam Iqbal,BSAI,,88,89,87,94,2025-09-03
1009,Bilal Ahmed,BSCS,Islamabad,-5,55,42,49,2025-09-04
1010,Hira Khan,BS DS,Rawalpindi,79,N/A,72,80,2025-09-04
""")

open("week06/data/raw/attendance.csv","w",encoding="utf-8").write("""student_id,classes_held,classes_attended
1001,30,26
1002,30,24
1003,30,28
1004,30,27
1005,30,22
1006,30,25
1007,30,20
1008,30,29
1009,30,18
1010,30,24
""")

# notebook
nb = {"cells":[
{"cell_type":"markdown","metadata":{},"source":["# Week 6 - Pandas Lab\\nAll steps from manual"]},
{"cell_type":"code","metadata":{},"source":["import pandas as pd, numpy as np\\nprint(pd.__version__)"]},
{"cell_type":"code","metadata":{},"source":["students=pd.read_csv('week06/data/raw/students_messy.csv', na_values=['','missing','N/A','-'])\\nprint(students.head())\\nprint(students.shape)\\nprint(students.isna().sum())\\nprint('dup',students.duplicated().sum())"]},
{"cell_type":"code","metadata":{},"source":["students=students.drop_duplicates().reset_index(drop=True)\\n# text clean\\nstudents['program']=students['program'].astype('string').str.strip().str.upper()\\nstudents['program']=students['program'].replace({'BS AI':'BSAI','BS-AI':'BSAI','AI':'BSAI','BS DS':'BSDS'})\\nstudents['city']=students['city'].astype('string').str.strip().str.title()\\nstudents['city']=students['city'].replace({'Rwp':'Rawalpindi'})\\nstudents['city']=students['city'].fillna('Unknown')\\nprint(students[['program','city']].head())"]},
{"cell_type":"code","metadata":{},"source":["# types\\nfor c in ['attendance','assignment','midterm','final']:\\n students[c]=pd.to_numeric(students[c], errors='coerce')\\nstudents['admission_date']=pd.to_datetime(students['admission_date'], dayfirst=True, errors='coerce')\\nstudents['student_id']=students['student_id'].astype('string')\\n# range\\ncleaning_log=[]; invalid=[]\\nfor c in ['attendance','assignment','midterm','final']:\\n m=(students[c]<0)|(students[c]>100)\\n if m.any():\\n cleaning_log.append({'col':c,'action':'set NA'})\\n students.loc[m,c]=pd.NA\\n# impute\\nfor c in ['attendance']:\\n students[c]=students.groupby('program')[c].transform(lambda x: x.fillna(x.median()))\\n students[c]=students[c].fillna(students[c].median())\\nfor c in ['assignment','midterm','final']:\\n students[c]=students[c].fillna(students[c].median())\\nprint(students.isna().sum())"]},
{"cell_type":"code","metadata":{},"source":["# features\\nstudents['weighted_score']=students['assignment']*0.2+students['midterm']*0.3+students['final']*0.5\\nimport numpy as np\\nstudents['attendance_status']=np.select([students['attendance']<75,(students['attendance']>=75)&(students['attendance']<85),students['attendance']>=85],['Low','Satisfactory','Excellent'])\\nstudents['grade']=np.select([students['weighted_score']>=85,students['weighted_score']>=75,students['weighted_score']>=65,students['weighted_score']>=50],['A','B','C','D'],default='F')\\nstudents['at_risk']=(students['attendance']<75)|(students['weighted_score']<50)\\nprogram_summary=students.groupby('program').agg(student_count=('student_id','count'),avg_weighted_score=('weighted_score','mean')).reset_index()\\ngrade_distribution=students.groupby('grade').agg(count=('student_id','count')).reset_index()\\nprint(program_summary)\\nprint(grade_distribution)\\n# save\\nstudents.to_csv('week06/data/processed/students_clean.csv',index=False)\\nprogram_summary.to_csv('week06/data/processed/program_summary.csv',index=False)\\ngrade_distribution.to_csv('week06/data/processed/grade_distribution.csv',index=False)\\nprint('saved')"]},
],"metadata":{},"nbformat":4,"nbformat_minor":5}
open("week06/pandas_lab.ipynb","w",encoding="utf-8").write(json.dumps(nb))
print("DONE - notebook and csv created")