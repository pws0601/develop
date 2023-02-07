import requests

#url = 'http://localhost:8000/tools/stopword/xlsUpload_stopword/D002'
url = 'http://10.10.224.3:10180/tools/stopword/xlsUpload_stopword/D002'

files = open('/home/ta/project/stopword_test.xlsx', 'rb')
upload = {'file':files}
res = requests.post(url, files = upload)
print(res)