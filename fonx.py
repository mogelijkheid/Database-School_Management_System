import psycopg2
def connect():
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="school",
            user="postgres",
            password="1")

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
            teacher = cur.fetchall()
            if teacher==[]:
                print("sifre yanlıs yada kullanıcı bulunamadı")
            else:
                print(teacher)        
        


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