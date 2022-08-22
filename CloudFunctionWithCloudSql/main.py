import sqlalchemy
 
connection_name = "playground-s-11-47a4feb8:us-central1:sqlinstance"
db_name = "emp"
db_user = "root"
db_password = "root"
 
driver_name = 'mysql+pymysql'
query_string = dict({"unix_socket": "/cloudsql/{}".format(connection_name)})
 
 
 
def fetchall(request):
    #request_json = request.get_json()
    stmt = sqlalchemy.text('select * from employee')
    print("====== inside fetch =======")
    db = sqlalchemy.create_engine(
      sqlalchemy.engine.url.URL(
        drivername=driver_name,
        username=db_user,
        password=db_password,
        database=db_name,
        query=query_string,
      ),
      pool_size=5,
      max_overflow=2,
      pool_timeout=30,
      pool_recycle=1800
    )
    print("====== db connection =======")
    try:
        with db.connect() as conn:
            print("===== insert==")
            conn.execute('insert into employee values(3,"Arsh")')
            print("====== inside connection =======")
            result = conn.execute(stmt).fetchall()
            print("======")
            for r in result:
              print(r)
    except Exception as e:
        return 'Error 1 : {}'.format(str(e))
    return str(result)
