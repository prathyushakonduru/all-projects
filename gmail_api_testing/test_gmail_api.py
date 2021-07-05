import quick_sort_data
import pprint
ls=[]
messages=quick_sort_data.get_email_list()
for message in messages:
    ls.append(message["id"])
pprint.pprint(quick_sort_data.get_email_content(ls[0]))
def test_get():
    assert len(quick_sort_data.get_email_content(ls[0]))!=0
def test_trash():
    assert "TRASH" in ((quick_sort_data.email_content_trash(ls[0]))["labelIds"])
def test_trash():
    assert "UNTRASH"  not in ((quick_sort_data.email_content_untrash(ls[0]))["labelIds"])
def test_batchmodify():
    res=quick_sort_data.get_email_content(ls[0])
    print(res("labelIds"))
    addlabel="STARRED"
    oldlabel="UNREAD"
    label_body={"ids":[ls[0]],"addlabelIds":[addlabel],"removeLabelIds":[oldlabel]}
    pprint.pprint(quick_sort_data.email_batch_modify(label_body))
    res_1=(quick_sort_data.get_email_content(ls[0]))
    print(res_1['labelIds'])
    assert addlabel in res_1['labelIds'] and oldmodel not in res_1['labelIds']
def test_delete():
    id=ls[0]
    print(id)
    quick_sort_data.email_content_delete(ls[0])
    messages=quick_sort_data.get_email_list()
    ls1=[]
    for message in messages:
        ls1.append(messages["id"])
    assert id not in ls1

"""def test_batchdelete():
    Body=[ls[0],ls[1]]
    pprint.pprint(quick_sort_data.get_batchdelete(Body))
    messages"""
 