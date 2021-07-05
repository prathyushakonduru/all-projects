############# Script Details #################################################################

# Script Name            :  quicksort.py
# Script version         :  3.8.5
# Prepared By            :  Prathyusha.Konduru@infinite.com
# Created_date           :  09-06-21
# last_modification_date :  14-06-21

##############################################################################################
# Purpose of the Script
#############################################################################################

# This script is designed such that work on for the all the operations 
# like GET, CREATE, DELETE, LIST of the information available for students present in class_room_api

#############################################################################################
# Below points has been considered in the Script
#############################################################################################

# 1.Created a class_room api .

# 2.Given respective credentials and permissions to it.

# 3.Created various method of delete ,list , create , get  

# 4.A log file created with the current date time along with message specified.

##############################################################################################
import quicksort
import logging
service=quicksort.main()
import logging
logging.basicConfig(filename="classroom_api_testing.log",
                    format='%(asctime)s %(message)s',
                    filemode='w',level=logging.INFO)

#it create the course 
def create_course():
    course = {
    'name': '10th Grade Biology',
    'section': 'Period 2',
    'descriptionHeading': 'Welcome to 10th Grade Biology',
    'description': """We'll be learning about about the
                structure of living creatures from a
                combination of textbooks, guest lectures,
                and lab work. Expect to be excited!""",
    'room': '301',
    'ownerId': 'me',
    'courseState': 'PROVISIONED'
    }
    course = service.courses().create(body=course).execute()
    logging.info("course created sucessfully")
    print('Course created: %s %s' % (course.get('name'), course.get('id')))
# it create the invitation by invite the student to join the class
def invitations(user_name):
    print('starts')
    info={"userId":'prathyusharaju223@gmail.com','courseId':'360069631764','role':'student'}
    course=service.invitations().create(body=info).execute()
    logging.info("invitation sended successfully")
    print(course)
    return course
#it will list all the students who are joined the class
def list_student():
    ls=[]
    course=service.courses().students().list(courseId='360069631764',pageSize=10).execute()
    print(course)
    logging.info("list the students successfully")
    return course
# it will delete the student
def delete_student(userid):
    course=service.courses().students().delete(courseId='360069631764',userId=userid).execute()
    print("student deleted")
    logging.info("delete the student successfully")
    return course
# it will get the information of particular student
def get_student():
    course=service.courses().students().get(courseId='360069631764',userId='100809771192456205834').execute()
    logging.info("get the information of particular id")
    print(course)
    print("sended")
    return course
if __name__ == '__main__':
    #create_course()
    #courses_get(360067902943)
    #student_create(360054470546)
    #add_student(3600707575744)
    #list_courses()
    #course_update(360054970755)
    #course_patch(360069631764)
    #add_student(360069631764)
    #invitations('username')
    #delete_student('112434639493315429907')
    list_student()
    #get_student()
    