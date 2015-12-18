import memcache

# (1) クライアントオブジェクトの生成
client = memcache.Client(["localhost:11211"])

# (2) キーをセット
client.set("key1", "some value 1")
client.set("key2", "some value 2")

# (3) 値の取得
value1 = client.get("key1")
print(value1)
value2 = client.get("key10")
print(value2)

# (4) キーの削除
client.delete("key1")
value1 = client.get("key1")
print(value1)

