import redis

# redis 연결
rd = redis.StrictRedis(host='localhost', port=6379, db=0)

#rd.set("test_key","test_value")

print(rd.get("test_key"))