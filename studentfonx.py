import psycopg2
class studentdata:
        def __init__(self,student_number,password):
            self.student_number=student_number
            self.password=password
            self.conn = psycopg2.connect(
                    host="localhost",
                    database="school",
                    user="postgres",
                    password="me5842")

            self.cur = self.conn.cursor()
       
        
        def studentlogin(self):
            
            self.cur.execute("""
            select * from students
            where studentid={} and password_=MD5('{}')
            """.format(self.student_number,self.password),
            )
            self.student = self.cur.fetchall()
            # self.cur.close()
            # self.conn.commit()
            return self.student
        
        def lessonshow(self):
                
            self.cur.execute("""
               SELECT l.lessonname from lessons l
               INNER JOIN lessons_students as ls
               ON ls.lessonid = l.lessonid 
               where ls.studentid={}
            """.format(self.student_number),
            )
            self.lessons = self.cur.fetchall()
            # self.cur.close()
            # self.conn.commit()
            return self.lessons
        
        def gradeshow(self):
            self.cur.execute("""
               SELECT midterm , final_ from lessons_students 
               where studentid={}
            """.format(self.student_number),
            )
            self.grades = self.cur.fetchall()
            # self.cur.close()
            # self.conn.commit()
            return self.grades
        
        def close(self):
            if self.conn is not None:
                self.conn.close()
                print('Database connection closed.')

