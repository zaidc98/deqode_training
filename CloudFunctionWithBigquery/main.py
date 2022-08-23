import pandas as pd
import requests
from pandas.io import gbq
print("==================")
def hello_world(request):
   print("================== a1")
   api_req = requests.get("https://raw.githubusercontent.com/amylio/Movies-ETL/main/MOD8_Challenge_Submission/Resources/wikipedia-movies.json").json()
   print("================== a2")
   df=pd.DataFrame.from_dict(api_req)
   # df = df[["year","title","Directed by"]]
   df.columns = df.columns.str.replace(' ','_')
   # df.columns = df.columns.str.replace('\(|\)','_')
   df.columns = df.columns.str.replace('\(|\)','_')
   df.columns = df.columns.str.replace('\.','')
   df.columns = df.columns.str.replace('\–','_')
 
   #was getting error as - Expected bytes, got a 'list' object. so casting it to string
   for col in df.columns:
       if df[col].dtype == list:
           df[col] = df[col].astype(str)
 
   # df=df.applymap(str)
  
   print(df.columns)
 
   print(df.dtypes)
  
   print("================== a3")
  
   try:
       print("========== inside try block ===========")
      
       df.to_gbq(destination_table="movie_test.movie", project_id="playground-s-11-cc61af1f", if_exists='replace')
       print("============ done loading")
   except Exception as e:
       print("=========== exception ========")
       print(e)
   return "Done"
