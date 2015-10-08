import redis

redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)
redis_trainer = redis.StrictRedis(host='localhost', port=6379, db=1)


def get_spam_trainers():
    trainers = []
    lis = redis_trainer.lrange('trainer:spam:keys', 0, -1)
    print('lis', lis)
    for key in lis:
        print('key', key)
        trainers.append(redis_trainer.hgetall(key))
    return trainers
