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
        #studentlogin
        if table=='students':
            student_number=int(input("studentnumber:"))
            password=input("password:")
            cur.execute("""
            select * from students
            where studentid={} and password_=MD5('{}')
            """.format(student_number,password),
            )
            student = cur.fetchall()
            if student==[]:
                print("password or username is wrong")
            else:
                print(student)
        #teacherlogin
        elif table=='teachers':
            username=input("username:")
            password=input("password:")
            cur.execute("""
            select teacherid,username,teachername,teachersurname,dateofbirth from teachers
            where username='{}' and password_=MD5('{}')
            """.format(username,password),
            )
            teacher = cur.fetchall()
            if teacher==[]:
                print("password or username is wrong")
            else:
                print("""username={}
name={}
surname={}
date of birth={}""".format(teacher[0][1],teacher[0][2].upper(),teacher[0][3].upper(),teacher[0][4]))  
                
                
        cur.execute("""
            select * from lessons where teacherid='{}'""".format(teacher[0][0])
            )
          
        lesson = cur.fetchall()
        print(lesson)
        
        choose=input("ne istiyon:")
        
        if choose=="add":
            lesson_name=input("hangi ders:")
            cur.execute("""
            insert into lessons(lessonname,teacherid,classid)
            values('{}',{},2)
            """.format(lesson_name,teacher[0][0])
            )
            
        elif choose=="delete":
            lesson_name=input("hangi ders:")
            cur.execute("""
            select lessonid from lessons where lessonname='{}'""".format(lesson_name)
            )
            lesson_id=cur.fetchall()
            
            cur.execute("""
            DELETE FROM lessons WHERE lessonid='{}' ;
            """.format(lesson_id[0][0])
            )
        
        elif choose=="renew":
            lesson_name=input("hangi ders:")
            cur.execute("""
            select lessonid from lessons where lessonname='{}'""".format(lesson_name)
            )
            lesson_id=cur.fetchall()
            new_name=input("name:")
            new_class=input("class:")
            
            cur.execute(""" update lessons set lessonname='{}', classid={} WHERE lessonid={}
                        """.format(new_name,new_class,lesson_id[0][0]))
        
        cur.execute("""
            select * from lessons where teacherid='{}'""".format(teacher[0][0])
            )
        lesson = cur.fetchall()
        print(lesson)
            

        # cur.execute("""
        #     select * from {}
        #     """.format(table),   
        # )
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