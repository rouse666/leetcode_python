# 基于__new__方法实现的单例模式(推荐使用,方便)
# 知识点:
# 1> 一个对象的实例化过程是先执行类的__new__方法,
# 如果我们没有写,默认会调用object的__new__方法,返回一个实例化对象,
# 然后再调用__init__方法,对这个对象进行初始化,我们可以根据这个实现单例.
# 2> 在一个类的__new__方法中先判断是不是存在实例,如果存在实例,就直接返回,如果不存在实例就创建.
import threading


class Singleton(object):
    _instance_lock = threading.Lock()

    def __init__(self, *args, **kwargs):
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            with Singleton._instance_lock:
                if not hasattr(cls, '_instance'):
                    Singleton._instance = super().__new__(cls)
            return Singleton._instance


obj1 = Singleton()
obj2 = Singleton()
print(obj1, obj2)


def task(arg):
    obj = Singleton()
    print(obj)


for i in range(10):
    t = threading.Thread(target=task, args=[i, ])
    t.start()
