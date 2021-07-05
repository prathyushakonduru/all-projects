def validate_testcases(userid):
    if len(userid)<21 or len(userid)>21:
        raise ValueError("id is not correct")