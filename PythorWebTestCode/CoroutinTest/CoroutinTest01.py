import json
import time
import asyncio

async def write_file(path):
    data = json.load(open(path, encoding = 'utf-8'))
    with open('/home/ta/data/upload/result.txt', 'w') as f:
        for d in data:
            for _ in range(10):
                for k in d:
                    for kk in k:
                        f.write(kk)



async def json_load(path):
    data = json.load(open(path, encoding = 'utf-8'))    
    for d in data:
        for _ in range(10):
            for k in d:
                for kk in k:
                    with open('/home/ta/data/upload/result.txt', 'w') as f:
                        await write_txt(f,kk)
                                            

async def write_txt(f, kk):    
    f.write(kk)
            


print(f"started at {time.strftime('%X')}")
loop = asyncio.get_event_loop()
tasks = [
    #loop.create_task(write_file('/home/ta/data/upload/tools.json'))
    loop.create_task(json_load('/home/ta/data/upload/tools.json'))
]
loop.run_until_complete(asyncio.gather(*tasks))
print(f"finished at {time.strftime('%X')}")
loop.close()