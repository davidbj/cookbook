# Threading 管理

## Thread

首先实现一个线程实例.

```
import threading
import logging

logging.basicConfig(level=logging.DEBUG, format='   %(asctime)s - [%(threadName)s]: %(message)s')

def worker(name):
    logging.debug(name)

if __name__ == "__main__":
    t = threading.Thread(target=worker, name='worker')
    t.start()
```

Threa提供如下参数：
   
   group=None    #线程组
   
   target=None   #要执行的函数
    
   name=None     #线程的名称
    
   args=()       #要传入函数的参数,位置参数.
   
   kwargs=None   #要传入函数的关键字参数
   
   daemon=None   #是否开启daemon模式,默认False.
   
  
#### daemon 模式
   Thread中daemon默认是False,当daemon为False时,如果主线程结束了,子线程继续会执行下去直到线程执行完成.如果daemon＝True时,则当主线程结束了,所有的其他线程都会结束。很明显,主线程结束了python将运行时环境。主线程会被结束.
   
##### daemon=False

```
import threading
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - [%(threadName)s] - %(message)s')

def worker(name):
    import time
    time.sleep(2)
    logging.debug(name)

if __name__ == "__main__":
    t = threading.Thread(target=worker, name='worker', args=('David', ))
    t.start()
    logging.debug('Main')
```

执行结果:

```
➜ David@zhangshaozhideMacBook-Pro  /data/magedu/004  python thread_test.py
2016-03-19 22:25:16,498 - [MainThread] - Main
2016-03-19 22:25:18,502 - [worker] - David
```

##### daemon=True

```
import threading
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - [%(threadName)s] - %(message)s')


def worker(name):
    import time
    time.sleep(2)
    logging.debug(name)


if __name__ == "__main__":
    t = threading.Thread(target=worker, name='worker', args=('David', ))
    t.daemon = True
    t.start()
    logging.debug('Main')
```

执行结果:

```
➜ David@zhangshaozhideMacBook-Pro  /data/magedu/004  python thread_test.py
2016-03-19 22:26:43,846 - [MainThread] - Main
```


daemon＝True时,当main线程执行完成.子线程还没有执行,Main执行结束.子线程也随之销毁.如果当Main线程执行完成,子线程也要执行。需要使用join()阻塞子线程，当子线程执行完之后才执行Main()线程.

```
import threading
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - [%(threadName)s] - %(message)s')


def worker(name):
    import time
    time.sleep(2)
    logging.debug(name)


if __name__ == "__main__":
    t = threading.Thread(target=worker, name='worker', args=('David', ))
    t.daemon = True
    t.start()
    t.join()
    logging.debug('Main')
```
     
执行结果:

```
➜ David@zhangshaozhideMacBook-Pro  /data/magedu/004  python thread_test.py
2016-03-19 22:32:05,117 - [worker] - David
2016-03-19 22:32:05,118 - [MainThread] - Main
```

join()阻塞一个线程,直到一个线程直线完成,才继续执行.
