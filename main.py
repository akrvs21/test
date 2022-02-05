from fastapi import FastAPI,HTTPException, status, HTTPException, Depends, Response
import psycopg2
import time

app = FastAPI()

while True:
    try:
        # Connect to your postgres DB
        conn = psycopg2.connect()

        # Open a cursor to perform database operations
        cursor = conn.cursor()
        print('DB connection was successfull!')
        break
    except Exception as error:
        print('Connection to DB failed')
        print("Error: ", error)
        time.sleep(2)

@app.get("/")
async def root():
    cursor.execute("""SELECT * FROM characters""")
    flags = cursor.fetchall()
    return {'data': flags}

# @app.get('/flags/{someid}')
# async def getFlag():
#     cursor.execute("""SELECT * FROM characters WHERE flag_id = %s""", (str(someid)))
#     flag = cursor.fetchone()
#     if not flag:
#         # more cleaner version
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"flag with id: {someid} was not found")
#     return {'flag': flag}
    
