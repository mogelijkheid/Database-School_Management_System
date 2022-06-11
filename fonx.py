import psycopg2
def connect():
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="school",
            user="postgres",
            password="1")

        cur = conn.cursor()

        cur.execute("""
        
            select * from students
            """,
            
        )
        students = cur.fetchall()
        for all in students:
            print(all)   


        cur.close()
        conn.commit()

    except (Exception) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

if __name__ == '__main__':
    connect()