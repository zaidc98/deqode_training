import pandas as pd
import requests
from pandas.io import gbq
print("==================")
def hello_world(request):
    print("================== a1")
    api_req = requests.get("https://raw.githubusercontent.com/amylio/Movies-ETL/main/MOD8_Challenge_Submission/Resources/wikipedia-movies.json").json()
    print("================== a2")
    df=pd.DataFrame.from_dict(api_req)
    df = df[["year","title","Directed by"]]
    df['year'] = df['year'].astype(float)
    df['title'] = df['title'].astype('string')
    df['Directed by'] = df['Directed by'].astype("string")
    print(df.dtypes)
    
    print("================== a3")
    
    try:
        print("========== inside try block ===========")
        df.rename(columns = {'Directed by':'directed_by'}, inplace = True)
        df.to_gbq(destination_table="movie_test.movie", project_id="playground-s-11-7ee45197", if_exists='replace')
        print("============ done loading")
    except Exception as e:
        print("=========== exception ========")
        print(e)
    return "Done"

