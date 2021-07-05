from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from googleapiclient import errors
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/classroom.rosters']

def main():
    """Shows basic usage of the Classroom API.
    Prints the names of the first 10 courses the user has access to.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    service = build('classroom', 'v1', credentials=creds)
    return service
    # Call the Classroom API
    #results = service.courses().list(pageSize=10).execute()
    #courses = results.get('courses', [])
def create_course():
    service=main()
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
    print('Course created: %s %s' % (course.get('name'), course.get('id')))
def courses_get(course_id):
    service=main()
    try:
        course = service.courses().get(id=course_id).execute()
        print(course)
        print('Course "{%s}" found.' % course.get('name'))
    except errors.HttpError as error:
        print('Course with ID "{%s}" not found.' % course_id)

def invitations():
    service=main()
    print('starts')
    info={"userId":'naveenknkn7@gmail.com','courseId':'3600707575744','role':'student'}
    i=service.invitations().create(body=info).execute()
    print('sended')

def add_student( course_id):
    service=main()
    """ Adds a student to a course. """
    
    # [START classroom_add_student]
    enrollment_code = 'abcdef'
    info= {
        'userId': 'prathyusharaju223@gmail.com',
        'profile':'student',
        'name':'prathyusha',
        'fullname':'prathyushakonduru'
    }
    student=service.invitations().create(body=info).execute()
    print(student)
    try:
        student = service.courses().students().create(
            courseId=course_id,
            enrollmentCode=enrollment_code,
            body=student).execute()
        print(
            '''User {%s} was enrolled as a student in
                the course with ID "{%s}"'''
            % (student.get('profile').get('name').get('fullName'),
                course_id))
    except errors.HttpError as error:
        print('You are already a member of this course.')
    # [END classroom_add_student]
        return error
    return student
def list_courses():
    service=main()
    courses = []
    page_token = None

    while True:
        response = service.courses().list(pageToken=page_token,
                                            pageSize=100).execute()
        courses.extend(response.get('courses', []))
        page_token = response.get('nextPageToken', None)
        if not page_token:
            break

    if not courses:
        print('No courses found.')
    else:
        print('Courses:')
    for course in courses:
        print(course.get('name'), course.get('id'))
def course_update(course_id):
    service=main()
    course = service.courses().get(id=course_id).execute()
    course['section'] = 'Period 3'
    course['room'] = '302'
    course = service.courses().update(id=course_id, body=course).execute()
    print(course)
    print('Course %s updated.' % course.get('name'))
def course_patch(course_id):
    service=main()
    course = {
    'section': 'Period 3',
    'room': '302'
    }
    course = service.courses().patch(id=course_id,
                                    updateMask='section,room',
                                    body=course).execute()
    print(course)
    print('Course "%s" updated.' % course.get('name'))
    
if __name__ == '__main__':
    main()
    #create_course()
    #courses_get(360067902943)
    #student_create(360054470546)
    #add_student(3600707575744)
    #list_courses()
    #course_update(360054970755)
    #course_patch(360069631764)
    #add_student(360069631764)
    invitations()







