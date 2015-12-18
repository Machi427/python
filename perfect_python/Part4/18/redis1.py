import redis

# (1) クライアントオブジェクトの生成
client = redis.Redis(host='localhost', port=6379, db=0)

# (2) リストの生成と追加
client.rpush('mylist', 'eggs')
client.rpush('mylist', 'ham')
client.lpush('mylist', 'spam')

# (3) リストの取得
result = client.lrange('mylist', 0, -1)
print(result)

# (4) リストから値の削除
client.lrem('mylist', 0, 'eggs')

# (5) ハッシュの生成と値の設定
client.hset('words', 'jugem', 'goko')
print(client.hget('words', 'jugem'))

# (6) Pythonの辞書を一気に登録
d = {'spam': 'salty', 'eggs': 'mild', 'ham': 'ioly'}
client.hmset('words', d)
print(client.hgetall('words'))

