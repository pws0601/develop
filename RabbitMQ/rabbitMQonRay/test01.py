import ray
import pika
import time



ray.init()

@ray.remote
def printMessage(msg,num):
    print(num ,' :: Received %s' % msg)
    time.sleep(5)
    print('next!!!!')

def printMessage2(msg,num):
    print(num ,' :: Received %s' % msg)
    time.sleep(5)
    print('next!!!!')

def on_message(channel, method_frame, header_frame, body):
    start = time.time()
    printMessage.remote(body,1)
    #printMessage2(body,1)
    #printMessage2(body,2)
    #printMessage2(body,3)
    #14.9903 sec
    print(f"{time.time()-start:.4f} sec") # 종료와 함께 수행시간 출력

        


def main():    
    __url='172.17.0.2'
    __port=5672
    __vhost='mq_test'
    __cred = pika.PlainCredentials('guest','guest')
    conn = pika.BlockingConnection(pika.ConnectionParameters(__url, __port, __vhost, __cred))
    chan = conn.channel()
    chan.basic_consume(
        queue = 't_msg_q',        
        on_message_callback = on_message,
        auto_ack = True
    )
    print('Consumer is starting...')
    chan.start_consuming()

main()