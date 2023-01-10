import pika
import os

class Publisher:
    def __init__(self) -> None: 
        self.__url='172.17.0.3'
        self.__port=5672
        #self.__vhost='ta_default'
        self.__vhost='ta_22003'
        self.__cred = pika.PlainCredentials('guest','guest')
        #self.__queue = 'pre_default'
        self.__queue = 'pre_22003'
    
    def main(self):
        conn = pika.BlockingConnection(pika.ConnectionParameters(self.__url, self.__port, self.__vhost, self.__cred))
        chan = conn.channel()
        #path = '/home/ta/data/22002_posco'
        path = '/home/ta/data/22003_starfield'
        for (root, directories, files) in os.walk(path):
            #for file in files[0:2000]:
            for file in files:
                print(file)
                bodyDict = dict()
                bodyDict['processType'] = 'insert' #['insert','delete'] defalut:insert
                bodyDict['filePath'] = path
                bodyDict['fileName'] = file
                bodyDict['CompanyCode'] = '22003'
                bodyDict['CompanyName'] = 'starfield'
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
