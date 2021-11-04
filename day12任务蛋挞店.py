import time
from threading import Thread

basket = 500
snack = 0
cashier = 0


class User:
    __username = ""
    __username1 = ""
    egg = 0
    dim = 0
    began = time.perf_counter()

    def set_username(self, username):
        if username == "":
            print("无名！")
        else:
            self.__username = username

    def get_username(self):
        return self.__username


class Shop(Thread, User):

    def run(self) -> None:
        global basket, snack
        while True:
            end = time.perf_counter()
            if int(end - self.began) == 30:
                egg_money = self.egg * 1.5
                print("工作结束,%s今天做了%d个蛋挞,工资为%.2f" % (super().get_username(), self.egg, egg_money))
                break
            if basket > 0:
                basket -= 1
                self.egg += 1
                snack += 1
                print("%s已经做了%d个蛋挞，篮子还剩%d的空间" % (super().get_username(), self.egg, basket))
            else:
                time.sleep(3)
                basket = 500


class Client(Thread, User):

    def run(self) -> None:
        global basket, cashier, snack
        money = 3000
        while True:
            end = time.perf_counter()
            if int(end - self.began) == 30:
                print("%s今天抢到了%d个蛋挞，金额剩余：%d" % (super().get_username(), self.dim, money))
                break
            if snack > 0 and money >= 3:
                snack -= 1
                basket += 1
                money -= 3
                self.dim += 1
                cashier += 3
                print("%s抢到了%d个蛋挞，篮子剩余蛋挞:%d,剩余金额:%d" % (super().get_username(), self.dim, snack, money))
            elif snack <= 0 and money >= 3:
                time.sleep(2)
            elif money < 3:
                continue


class Revenue(Thread, User):

    def run(self) -> None:
        global cashier
        while True:
            end = time.perf_counter()
            if int(end - self.began) == 30:
                print("今天总收入：￥%d" % cashier)
                break


p1 = Shop()
p2 = Shop()
p3 = Shop()
t1 = Client()
t2 = Client()
t3 = Client()
t4 = Client()
t5 = Client()
t6 = Client()
reve = Revenue()
p1.set_username("张三")
p2.set_username("李四")
p3.set_username("王五")
t1.set_username("赵一")
t2.set_username("钱二")
t3.set_username("孙三")
t4.set_username("周六")
t5.set_username("武柒")
t6.set_username("郑八")
p1.start()
p2.start()
p3.start()
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
reve.start()
