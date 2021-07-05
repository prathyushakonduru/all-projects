#Purpose of the script
########################################################################################################################
# Google Classroom API Validation.
# Create and execute test cases in pytest for the all the operations GET, CREATE, DELETE and LIST 
########################################################################################################################

import methods
import pytest,os
import logging
import sample

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()
course_ids=methods.list_student()
logger.info("all ids are listed and colleted in a variable called course_ids ")
ls=[]
for course in course_ids.items():
    for i in range(len(course[1])):
        ls.append(course[1][i]['userId'])
logger.info("userId  is collected and appended in list")
#print(ls)
#print(course_ids['students'][0]['userId'])
#it will check whether the id is present or not
def test_list():
    with pytest.raises(ValueError) as exc_info:
        sample.validate_testcases('1023539848576041525')
    assert str(exc_info.value)=='id is not correct'
    print(str(exc_info.value))
    #assert '102353984857604152559' in ls
    #negative testcase
    #assert '4562353984857604152559'  not in ls
    #logger.info("test_list is passed successfully")
#it will check whether the information is present in particular id or not
'''def test_get():
    course=methods.get_student()
    assert course['courseId']=='360069631764'
    #negative testcase 
    assert course['courseId']!='360069631704'
    logger.info("test_get is passed successfully")
#it will ckeck whether the particular id is deeted or not
def test_delete():
    course_id='112434639493315429907'
    methods.delete_student(course_id)
    lst_ids=methods.list_student()
    print(lst_ids)
    ls1=[]
    for course in lst_ids.items():
        #print(id1)
        for i in range(len(course[1])):
            print(i)
            ls1.append(course[1][i]['userId'])
            print(ls1)
    assert '112434639493315429907' not in ls1
    #negative testcase
    assert '112434639493315429' not in ls1
    logger.info("test_delete is passed successfully")
#it will check whether the invitation has been sended or not
def test_invitations():
    user_name='Sandeep Raju'
    #methods.invitations(user_name)
    list_student=methods.list_student()
    names=[]
    for course in list_student.items():
        for user in range(len(course[1])):
            names.append(course[1][user]['profile']['name']['fullName'])
    assert 'Sandeep Raju' in names
    #negative test_case
    assert 'sandeep' not in names
    logger.info("test_invitation is passed successfully")'''
    
if __name__ == '__main__':
    pytest.main(args=['-s', os.path.abspath(__file__)])
    logger.info("programm ends here")