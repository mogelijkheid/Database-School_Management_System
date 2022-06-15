import psycopg2
class teacherdata:
        def __init__(self,username,password):
            self.username=username
            self.password=password
            self.conn = psycopg2.connect(
                    host="localhost",
                    database="school",
                    user="postgres",
                    password="me5842")

            self.cur = self.conn.cursor()
            self.cur.execute("""
            select * from teachers
            where username='{}' and password_=MD5('{}')
            """.format(self.username,self.password),
            )
            self.teacher = self.cur.fetchall()
        
        def teacherlogin(self):
            return self.teacher
        
        def teacherlesson(self):
            self.cur.execute("""             
               SELECT l.lessonid,l.lessonname ,cl.classname, cl.capacity from lessons l
               INNER JOIN class_ as cl
               ON l.classid=cl.classid
			   where l.lessonid in (select lt.lessonid from lessons_teachers as lt
			   where teacherid={} );
            """.format(self.teacher[0][0])
            )
            self.lesson =self. cur.fetchall()
            self.cur.execute("""             
              SELECT l.lessonid,l.lessonname ,cl.classname, cl.capacity from lessons l
               INNER JOIN class_ as cl
               ON l.classid=cl.classid
			   where l.lessonid not in  (select lt.lessonid from lessons_teachers as lt
			   where teacherid={} );
            """.format(self.teacher[0][0])
            )
            self.nolesson=self.cur.fetchall()
            return self.lesson,self.nolesson
        def close():
            if self.conn is not None:
                self.conn.close()
                print('Database connection closed.')