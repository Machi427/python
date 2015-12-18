class Spam:
     def __del__(self):
         pass

spam1 = Spam()
spam2 = Spam()

# 循環参照を作る
spam1.other = spam2
spam2.other = spam1

# オブジェクトへの参照を削除する
del spam1, spam2

# ガベージコレクションを起動
import gc
gc.collect()

# spam1, spam2 が解放されず、gc.garbageに格納されるのを確認する
print(gc.garbage)

