from threading import Thread
from time import sleep
bread = 0
class Chef(Thread):
    def run(self) -> None:
        global bread
        while True:
            if bread < 500:
                bread += 1
                print('生产了',bread,'个面包')
            else:
                sleep(3)
class Cousumer(Thread):
    money = 3000
    count = 0
    def run(self) -> None:
        global bread
        while True:
            if self.money > 0 and bread > 0:
                self.count += 1
                bread -= 1
                self.money -= 3
                print('抢到了',self.count,'个面包，还有',bread,'个面包')
            elif bread == 0:
                sleep(3)
                print('等待')
            elif self.money == 0:
                print('您一共抢了',self.count,'个面包')
                break
chef1 = Chef()
chef2 = Chef()
chef3 = Chef()
cousumer1 = Cousumer()
cousumer2 = Cousumer()
cousumer3 = Cousumer()
cousumer4 = Cousumer()
cousumer5 = Cousumer()
chef1.start()
chef2.start()
chef3.start()
cousumer1.start()
cousumer2.start()
cousumer3.start()
cousumer4.start()
cousumer5.start()

















