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
        
        def addlesson(self,lesson):
            self.lesson=lesson
            self.cur.execute("""             
              select lessonid from lessons where lessonname='{}'
            """.format(self.lesson)
            )
            
            self.lessonid=self.cur.fetchall()
            self.cur.execute("""             
             insert into lessons_teachers(lessonid,teacherid)
             values ({},{})
            """.format(self.lessonid[0][0],self.teacher[0][0])
            )
        def delete_(self,lesson):
            self.lesson=lesson
            self.cur.execute("""             
              select lessonid from lessons where lessonname='{}'
            """.format(self.lesson)
            )
            
            self.lessonid=self.cur.fetchall()
            self.cur.execute("""             
              delete from lessons_teachers where lessonid='{}' and teacherid={}
            """.format(self.lessonid[0][0],self.teacher[0][0])
            )
            
        def studentlist(self,lesson):
            self.lesson=lesson
            self.cur.execute("""             
              select * from students where studentid in
(select studentid from lessons_students where lessonid in
(select lessonid from lessons where lessonname='{}'))
            """.format(self.lesson)
            )
            self.student =self.cur.fetchall()
            return self.student
        
        def nostudentlist(self,lesson):
            self.lesson=lesson
            self.cur.execute("""             
              select * from students where studentid not in
(select studentid from lessons_students where lessonid in
(select lessonid from lessons where lessonname='{}'))
            """.format(self.lesson)
            )
            self.nostudent =self.cur.fetchall()
            return self.nostudent
            
        def shwgrades(self,lessonname,studentname):
            self.lessonname=lessonname
            self.studentname=studentname
            self.cur.execute("""             
              select lessonid from lessons where lessonname='{}'
            """.format(self.lessonname)
            )
            self.lessonid =self. cur.fetchall()
            self.cur.execute("""             
              select studentid from students where studentname='{}'
            """.format(self.studentname)
            )
            self.studentid =self. cur.fetchall()
            self.cur.execute("""             
             SELECT midterm,final_,attandance
FROM lessons_students where studentid={} and lessonid={};
            """.format(self.studentid[0][0],self.lessonid[0][0])
            )
            self.grades =self. cur.fetchall()
            return self.grades
        
        def removestd(self,lessonname,studentname):
            self.lessonname=lessonname
            self.studentname=studentname
            self.cur.execute("""             
              select lessonid from lessons where lessonname='{}'
            """.format(self.lessonname)
            )
            self.lessonid =self. cur.fetchall()
            self.cur.execute("""             
              select studentid from students where studentname='{}'
            """.format(self.studentname)
            )
            self.studentid=self.cur.fetchall()
            self.cur.execute("""             
              delete from lessons_students where lessonid={} and studentid={}
            """.format(self.lessonid[0][0],self.studentid[0][0])
            )
            
        def close_(self):
            self.cur.close()
            self.conn.commit()
            if self.conn is not None:
                self.conn.close()