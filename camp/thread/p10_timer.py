# 定时器： 指定n秒后执行
from threading import Timer

def hello():
    print("hello, world")

t = Timer(1, hello)  # 表示1秒后执行hello函数
t.start()
