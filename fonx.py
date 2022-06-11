import psycopg2
def connect():
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="school",
            user="postgres",
            password="me5842")

        cur = conn.cursor()
        table=input("tablo:")
        if table=='students':
            id=int(input("id:"))
            password=input("password:")
            cur.execute("""
            select * from students
            where studentid={} and password_=MD5('{}')
            """.format(id,password),
            )
            student = cur.fetchone()
            if student==[]:
                print("sifre yanlıs yada kullanıcı bulunamadı")
            else:
                print(student)
        elif table=='teachers':
            username=input("username:")
            password=input("password:")
            cur.execute("""
            select * from teachers
            where username='{}' and password_=MD5('{}')
            """.format(username,password),
            )
            teacher = cur.fetchone()
            if teacher==[]:
                print("sifre yanlıs yada kullanıcı bulunamadı")
            else:
                print(teacher)        
        

        cur.execute("""
<<<<<<< HEAD
        
            select * from students
            """,
=======
            select * from {}
            """.format(table),
>>>>>>> 42d302e121ab6026412fea558339fff476bda625
            
        )
        # students = cur.fetchall()
        # for all in students:
        #     print(all)   


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