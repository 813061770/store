from unittest import TestCase
from ddt import unpack,ddt,data
from danyuanTest.GSbank import bank_cls
test_add = [
    ['刘劲松','666666','鹤岗',2000],
    ['虎虎虎','666666','你猜',3000,],
    ['冯鹏飞','777777','鹤壁',1000],
    ['松松松','111111','河南',2000]
]
test_draw = [
    ['1','123456',900],
    ['12','123456',900],
    ['15435520','777777',1000],
    ['27843610','666666',2000]
]
test_save = [
    ['1', '123456', 10000],
    ['12', '123456', 10000],
    ['15435520', '777777', 10000],
    ['27843610', '666666', 10000]
]
test_give = [
    ['1','123456','12',5000],
    ['15435520','777777','27843610',5000]
]
test_search = [
    ['1','123456'],
    ['12','123456']
]
@ddt
class TestAddUser(TestCase):
    @data(*test_add)
    @unpack
    def testAdd(self,username,password,local,money):
        bank = bank_cls()
        result = bank.adduser_to_bank(username,password,local,money)
        self.assertEqual(1,result)
    @data(*test_draw)
    @unpack
    def testDraw(self,username,password,money):
        bank = bank_cls()
        result = bank.draw_money(username,password,money)
        self.assertEqual(3,result)
    @data(*test_save)
    @unpack
    def testSave(self,username,password,money):
        bank = bank_cls()
        result = bank.save_money(username,password,money)
        self.assertEqual(True,result)
    @data(*test_give)
    @unpack
    def testGiveMoney(self,userid,userpsw,yourid,money):
        bank = bank_cls()
        result = bank.giveMoney(userid,userpsw,yourid,money)
        self.assertEqual(None,result)
    @data(*test_search)
    @unpack
    def testSearch(self,userid,password):
        bank = bank_cls()
        result = bank.search(userid,password)
        self.assertEqual(None,result)




















