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

#### Lock 锁
    当多个线程同时访问内容.线程本身没有安全保护机制,就是谁抢到资源谁就有对该资源的执行权限，这样容易把资源改乱.所以需要加一把锁,当一个线程对该资源进行访问时,首先用一把锁将该资源锁定,这样其它线程就没有权限访问该资源。直到这把锁打开，其它线程才可以访问.
    
    
```
import threading
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctims)s -[%(threadName)s]: %(message)s')

def worker(name, lock):
    lock.acquire()       #加锁
    logging.debug(name)
    lock.release()       #释放锁

if __name__ == "__main__":
    lock = threading.Lock()
    t = threading.Thread(target=worker, name='work', args=('David', lock))
    t1 = threading.Thread(target=worker, name='work1', args=('shaozhi.zhang', lock))
    t.start()
    t1.start()
    logging.debug('Main')
```
或者:

```
import threading
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - [%(threadName)s]: %(message)s')

def worker(name, lock):
    with lock:
        logging.debug(name)

if __name__ == "__main__":
    lock = threading.Lock()
    t = threading.Thread(target=work, name='work', args=('David', lock))
    t1 = threading.Thread(target=work, name='work1', args=('shaozhi.zhang', lock))
    t.start()
    t1.start()
    t.join()      #为防止父线程执行完成,还有子线程执行。需要先阻塞住子线程.当子线程执行完成,再执行父线程.
    t1.join()
    logging.debug('Main')
```

输出结果:

``` 
➜ David@zhangshaozhideMacBook-Pro  /data/magedu/004  python thread_test.py
2016-03-20 06:44:28,318 - [worker] - David
2016-03-20 06:44:28,318 - [worker1] - shaozhi
2016-03-20 06:44:28,318 - [MainThread] - Main
```


#### Event
    多线程之间通信在任何语言都一直都是一个难点。python提供了一个简单的通信机制Threading.Event,通用的条件变量,多个线程可以等待某个事件发生,在事件发生后,所有的线程都会被激活.
    

如下实例:

```
import threading
import logging
import time

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - [%(threadName)s]: %(message)s')


class Test:
    def __init__(self):
        self.name = None
        self.event = threading.Event()

    def r(self):
        logging.debug('start time:{0}'.format(time.ctime(time.time())))
        while self.event.wait(timeout=5):
            logging.debug('working... time:{0}'.format(time.ctime(time.time())))
            time.sleep(0.5)

    def start(self):
        threading.Thread(target=self.r, name='worker').start()

    def stop(self):
        self.event.set()

    def restart(self):
        self.event.clear()

if __name__ == "__main__":
    logging.debug('start {0}'.format(time.ctime(time.time())))
    t = Test()
    t.start()
    time.sleep(2)
    t.stop()
    time.sleep(2)
    t.restart()
    logging.debug('stop {0}'.format(time.ctime(time.time())))
```

默认self.event.wait阻塞状态,当调用start方法self.event.set().阻塞打开,继续执行.当调用clear()又进入阻塞状态.

或者这样:

```
import threading
import logging
import time

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - [%(threadName)s]: %(message)s')

class Test:
    def __init__(self):
        self.name = None
        self.event = threading.Event()

    def run(self):
        logging.debug('start time:{0}'.format(time.ctime(time.time())))
        while not self.event.is_set():
            logging.debug('working...{0}'.format(time.ctime(time.time())))
            time.sleep(0.5)

    def start(self):
        threading.Thread(target=self.run, name='worker').start()

    def stop(self):
        self.event.set()

if __name__ == "__main__":
    logging.debug('start {0}'.format(time.ctime(time.time())))
    t = Test()
    t.start()
    time.sleep(4)
    t.stop()
    logging.debug('stop {0}'.format(time.ctime(time.time())))
```

### Condition

    condition是生产者消费者模式.
    
```
import threading
import logging
import time

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - [%(threadName)s]: %(message)s')

class Test:
    def __init__(self):
        self.__cond = threading.Condition()
        self.__event = threading.Event()
        self.message = None

    def send_mail(self):
        '''消费者'''
        
        #logging.debug('start mail')
        while not self.__event.is_set():
            with self.__cond:
                self.__cond.wait()
                logging.debug('send mail {0} ok!'.format(self.message))

    def send_sms(self):
        '''消费者
        self.__cond.wait()
        '''
        #logging.debug('start sms')
        while not self.__event.is_set():
            with self.__cond:
                self.__cond.wait()
                logging.debug('send sms {0} ok!'.format(self.message))

    def notify(self, message):
        '''生产者
        self.__cond.notify_all()生产者发送给所有消费者.
        '''
        
        with self.__cond:
            self.message = message
            self.__cond.notify_all()

    def start(self):
        threading.Thread(target=self.send_mail, name='send-mail').start()
        threading.Thread(target=self.send_sms, name='send-sms').start()

    def stop(self):
        self.__event.set()

if __name__ == "__main__":
    t = Test()
    t.start()
    t.notify('David')
    t.stop()
```
