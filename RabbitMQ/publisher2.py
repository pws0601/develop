import pika
import os

class Publisher:
    def __init__(self) -> None: 
        self.__url='172.17.0.3'
        self.__port=5672
        self.__vhost='ta_22008'
        self.__cred = pika.PlainCredentials('guest','guest')
        self.__queue = 'pre_22008'
    
    def main(self):
        conn = pika.BlockingConnection(pika.ConnectionParameters(self.__url, self.__port, self.__vhost, self.__cred))
        chan = conn.channel()
        targetDirList = list()
        path = '/home/ta/data/22008_HITE/12/$date$/22008/'
        for i in range(1,32):
            if i<10 : 
                targetDir = path.replace('$date$','0'+str(i))
            else:
                targetDir = path.replace('$date$',str(i))
            for (root, directories, files) in os.walk(targetDir):
                for directory in directories:
                    targetDirList.append(targetDir+directory)
        
        for targetPath in targetDirList:
            for (root, directories, files) in os.walk(targetPath):
                for file in files:
                    print(file)
                    bodyDict = dict()
                    bodyDict['processType'] = 'insert' #['insert','delete'] defalut:insert
                    bodyDict['filePath'] = targetPath
                    bodyDict['fileName'] = file
                    bodyDict['CompanyCode'] = '22008'
                    bodyDict['CompanyName'] = '하이트진로'
                    body = str(bodyDict)
                    
                    chan.basic_publish(
                        exchange='',
                        routing_key=self.__queue,            
                        body = body,
                        properties=pika.BasicProperties(
                            delivery_mode = pika.spec.PERSISTENT_DELIVERY_MODE
                        )
                    )
                    
        conn.close()


publisher = Publisher()
publisher.main()
