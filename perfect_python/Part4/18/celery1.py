#(1)mytask から add 関数のインポート
from mytask import add
import time

#(2)タスクの実行を依頼
delayed = add.delay(3,2)

#(3)タスクの処理の終了を待つ
while delayed.ready() == False:
    time.sleep(1)

#(4)実行結果の出力
print(delayed.get())

