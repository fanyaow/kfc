# -*- coding: utf-8 -*-
# 作者：dcjmessi
# 日期：2018/10/19


from kfcmain import *
from normal import *
from package import *
from activity import *
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
import img_rc


class KFC_Main(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.main_ui = Ui_MainWindow()
        self.main_ui.setupUi(self)

        # 给按钮绑定方法
        btn_del = self.main_ui.pushButton_5
        btn_del.clicked.connect(self.order_del)
        btn_num = self.main_ui.pushButton_6
        btn_num.clicked.connect(self.order_num)
        self.btn_tip = self.main_ui.pushButton_7
        self.btn_tip.clicked.connect(self.order_tip)
        # 设置按钮为当前不可用
        self.btn_tip.setEnabled(False)
        # 定义列表
        self.num = []
        self.new_num = []

    # 主界面显示
    def person(self):
        # 主界面贴图
        self.main_ui.label_8.setPixmap(QPixmap('./picture/kfc.jpg'))
        # 将图片完全填充
        self.main_ui.label_8.setScaledContents(True)
        # 初始化会员储值余额
        self.balance = 200
        # 初始化优惠券数量
        self.coupons = 1
        # 显示余额和券数量
        self.main_ui.label_2.setText(str(self.balance))
        self.main_ui.label_5.setText(str(self.coupons))
        # 显示主界面
        kfcmain.show()

    # 删除tableWidget所选行
    def order_del(self):
        # 获取所选行索引
        row_index = kfcmain.main_ui.tableWidget.currentRow()
        if row_index != -1:
            # 删除
            kfcmain.main_ui.tableWidget.removeRow(row_index)

    # 结算
    def order_num(self):
        # 设置按钮为可用
        self.btn_tip.setEnabled(True)
        # 遍历所有行
        for row_index in range(kfcmain.main_ui.tableWidget.rowCount()):
            # 将每一行的第三项值添加到num列表里
            self.num.append(kfcmain.main_ui.tableWidget.item(row_index, 2).text())

        # 将num中的字符转换成int型
        self.new_num = eval('[' + (','.join(self.num)) + ']')
        # 将new_num列表值求和
        self.money = sum(self.new_num)

        # 有优惠券时
        if self.coupons >= 1:
            # 消息提示框
            button = QMessageBox.information(self, "温馨提示", "是否使用优惠券", QMessageBox.Yes | QMessageBox.No)
            # 使用优惠券
            if button == QMessageBox.Yes:
                # 当前优惠券数量减一
                self.coupons = self.coupons - 1
                self.main_ui.label_5.setText(str(self.coupons))

                # 余额足够
                if self.balance >= (self.money - self.coupons * 20):
                    QMessageBox.information(self, "恭喜您", "付款成功！", QMessageBox.Yes)
                    self.balance = self.balance - self.money - self.coupons * 20
                    self.main_ui.label_2.setText(str(self.balance))
                else:
                    QMessageBox.information(self, "对不起", "您的会员储值卡余额不足！", QMessageBox.Yes)
            # 不使用优惠券
            else:
                if self.balance >= self.money:
                    QMessageBox.information(self, "恭喜您", "付款成功！", QMessageBox.Yes)
                    self.balance = self.balance - self.money
                    self.main_ui.label_2.setText(str(self.balance))
                else:
                    QMessageBox.information(self, "对不起", "您的会员储值卡余额不足！", QMessageBox.Yes)
        # 没有优惠券时
        else:
            if self.balance >= self.money:
                QMessageBox.information(self, "恭喜您", "付款成功！", QMessageBox.Yes)
                self.balance = self.balance - self.money
                self.main_ui.label_2.setText(str(self.balance))
            else:
                QMessageBox.information(self, "对不起", "您的会员储值卡余额不足！", QMessageBox.Yes)

    # 打印小票
    def order_tip(self):
        # 打开本地txt文件
        with open("kfctip.txt", "w") as f:
            # 遍历行
            for row_index in range(kfcmain.main_ui.tableWidget.rowCount()):
                # 遍历列
                for column_index in range(kfcmain.main_ui.tableWidget.columnCount()):
                    # 将tableWidget数据写入文件
                    f.write(kfcmain.main_ui.tableWidget.item(row_index, column_index).text() + "\n")
            f.write("合计：" + str(self.money) + "元")
        f.close()


class Normal(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.normal_ui = Ui_Normal()
        self.normal_ui.setupUi(self)

        # 初始化各基本餐加入订单按钮点击次数
        self.bt1 = 0
        self.bt2 = 0
        self.bt3 = 0
        self.bt4 = 0
        self.bt6 = 0
        # 初始化返回按钮点击次数
        self.bt5 = 0
        # 按钮绑定方法
        btn_hamburg = self.normal_ui.pushButton
        btn_hamburg.clicked.connect(self.order_hamburg)
        btn_chicken = self.normal_ui.pushButton_2
        btn_chicken.clicked.connect(self.order_chicken)
        btn_fries = self.normal_ui.pushButton_3
        btn_fries.clicked.connect(self.order_fries)
        btn_tea = self.normal_ui.pushButton_4
        btn_tea.clicked.connect(self.order_tea)
        btn_ice = self.normal_ui.pushButton_6
        btn_ice.clicked.connect(self.order_ice)
        btn_return = self.normal_ui.pushButton_5
        btn_return.clicked.connect(self.nor_show)

    # 显示基本餐界面
    def nor_order(self):
        self.normal_ui.label_3.setPixmap(QPixmap('./picture/新奥尔良.jpg'))
        self.normal_ui.label_3.setScaledContents(True)
        self.normal_ui.label_6.setPixmap(QPixmap('./picture/鸡翅.jpg'))
        self.normal_ui.label_6.setScaledContents(True)
        self.normal_ui.label_9.setPixmap(QPixmap('./picture/薯条.jpg'))
        self.normal_ui.label_9.setScaledContents(True)
        self.normal_ui.label_12.setPixmap(QPixmap('./picture/乌龙茶.jpg'))
        self.normal_ui.label_12.setScaledContents(True)
        self.normal_ui.label_15.setPixmap(QPixmap('./picture/冰淇淋.jpg'))
        self.normal_ui.label_15.setScaledContents(True)
        # 基本餐价格
        self.price_hamburg = 18.5
        self.price_chicken = 11.0
        self.price_fries = 13.0
        self.price_tea = 13.5
        self.price_ice = 10.0
        # 显示价格
        self.normal_ui.label.setText(str(self.price_hamburg) + "元/份")
        self.normal_ui.label_4.setText(str(self.price_chicken) + "元/份")
        self.normal_ui.label_7.setText(str(self.price_fries) + "元/份")
        self.normal_ui.label_10.setText(str(self.price_tea) + "元/份")
        self.normal_ui.label_13.setText(str(self.price_ice) + "元/份")
        normal.show()

    # 计算点击次数
    def order_hamburg(self):
        self.bt1 += 1

    def order_chicken(self):
        self.bt2 += 1

    def order_fries(self):
        self.bt3 += 1

    def order_tea(self):
        self.bt4 += 1

    def order_ice(self):
        self.bt6 += 1

    def nor_show(self):
        self.bt5 += 1

        # 隐藏界面
        normal.hide()

        # 获取所选各基本餐的数量对应的价格
        self.num_hamburg = self.price_hamburg * self.bt1
        self.num_chicken = self.price_chicken * self.bt2
        self.num_fries = self.price_fries * self.bt3
        self.num_tea = self.price_tea * self.bt4
        self.num_ice = self.price_ice * self.bt6

        # 不是第一次进入该界面
        if self.bt5 > 1:
            for row_index in range(kfcmain.main_ui.tableWidget.rowCount()):
                # 获取tableWidget的所有名称，并放入name列表
                name.append(kfcmain.main_ui.tableWidget.item(row_index, 0).text())
            if '新奥尔良烤鸡腿堡' in name:
                # 重新设置该行的数量和价格
                kfcmain.main_ui.tableWidget.setItem(name.index('新奥尔良烤鸡腿堡'), 1, QTableWidgetItem("×" + str(self.bt1)))
                kfcmain.main_ui.tableWidget.setItem(name.index('新奥尔良烤鸡腿堡'), 2, QTableWidgetItem(str(self.num_hamburg)))
            if '新奥尔良烤鸡腿堡' not in name:
                # 已选择
                if self.bt1 != 0:
                    # 添加一行数据
                    row_count = kfcmain.main_ui.tableWidget.rowCount()
                    kfcmain.main_ui.tableWidget.insertRow(row_count)
                    kfcmain.main_ui.tableWidget.setItem(row_count, 0, QTableWidgetItem(normal.normal_ui.label_2.text()))
                    kfcmain.main_ui.tableWidget.setItem(row_count, 1, QTableWidgetItem("×" + str(self.bt1)))
                    kfcmain.main_ui.tableWidget.setItem(row_count, 2, QTableWidgetItem(str(self.num_hamburg)))
            if '香辣鸡翅' in name:
                kfcmain.main_ui.tableWidget.setItem(name.index('香辣鸡翅'), 1, QTableWidgetItem("×" + str(self.bt2)))
                kfcmain.main_ui.tableWidget.setItem(name.index('香辣鸡翅'), 2, QTableWidgetItem(str(self.num_chicken)))
            if '香辣鸡翅' not in name:
                if self.bt2 != 0:
                    row_count = kfcmain.main_ui.tableWidget.rowCount()
                    kfcmain.main_ui.tableWidget.insertRow(row_count)
                    kfcmain.main_ui.tableWidget.setItem(row_count, 0, QTableWidgetItem(normal.normal_ui.label_5.text()))
                    kfcmain.main_ui.tableWidget.setItem(row_count, 1, QTableWidgetItem("×" + str(self.bt2)))
                    kfcmain.main_ui.tableWidget.setItem(row_count, 2, QTableWidgetItem(str(self.num_chicken)))
            if '波纹霸王薯条' in name:
                kfcmain.main_ui.tableWidget.setItem(name.index('波纹霸王薯条'), 1, QTableWidgetItem("×" + str(self.bt3)))
                kfcmain.main_ui.tableWidget.setItem(name.index('波纹霸王薯条'), 2, QTableWidgetItem(str(self.num_fries)))
            if '波纹霸王薯条' not in name:
                if self.bt3 != 0:
                    row_count = kfcmain.main_ui.tableWidget.rowCount()
                    kfcmain.main_ui.tableWidget.insertRow(row_count)
                    kfcmain.main_ui.tableWidget.setItem(row_count, 0, QTableWidgetItem(normal.normal_ui.label_8.text()))
                    kfcmain.main_ui.tableWidget.setItem(row_count, 1, QTableWidgetItem("×" + str(self.bt3)))
                    kfcmain.main_ui.tableWidget.setItem(row_count, 2, QTableWidgetItem(str(self.num_fries)))
            if '乌龙茶' in name:
                kfcmain.main_ui.tableWidget.setItem(name.index('乌龙茶'), 1, QTableWidgetItem("×" + str(self.bt4)))
                kfcmain.main_ui.tableWidget.setItem(name.index('乌龙茶'), 2, QTableWidgetItem(str(self.num_tea)))
            if '乌龙茶' not in name:
                if self.bt4 != 0:
                    row_count = kfcmain.main_ui.tableWidget.rowCount()
                    kfcmain.main_ui.tableWidget.insertRow(row_count)
                    kfcmain.main_ui.tableWidget.setItem(row_count, 0,
                                                        QTableWidgetItem(normal.normal_ui.label_11.text()))
                    kfcmain.main_ui.tableWidget.setItem(row_count, 1, QTableWidgetItem("×" + str(self.bt4)))
                    kfcmain.main_ui.tableWidget.setItem(row_count, 2, QTableWidgetItem(str(self.num_tea)))
            if '原味圣代（草莓酱）' in name:
                kfcmain.main_ui.tableWidget.setItem(name.index('原味圣代（草莓酱）'), 1, QTableWidgetItem("×" + str(self.bt6)))
                kfcmain.main_ui.tableWidget.setItem(name.index('原味圣代（草莓酱）'), 2, QTableWidgetItem(str(self.num_ice)))
            if '原味圣代（草莓酱）' not in name:
                if self.bt6 != 0:
                    row_count = kfcmain.main_ui.tableWidget.rowCount()
                    kfcmain.main_ui.tableWidget.insertRow(row_count)
                    kfcmain.main_ui.tableWidget.setItem(row_count, 0,
                                                        QTableWidgetItem(normal.normal_ui.label_14.text()))
                    kfcmain.main_ui.tableWidget.setItem(row_count, 1, QTableWidgetItem("×" + str(self.bt6)))
                    kfcmain.main_ui.tableWidget.setItem(row_count, 2, QTableWidgetItem(str(self.num_ice)))
        # 第一次进入该界面
        else:
            if self.bt1 != 0:
                row_count = kfcmain.main_ui.tableWidget.rowCount()
                kfcmain.main_ui.tableWidget.insertRow(row_count)
                kfcmain.main_ui.tableWidget.setItem(row_count, 0, QTableWidgetItem(normal.normal_ui.label_2.text()))
                kfcmain.main_ui.tableWidget.setItem(row_count, 1, QTableWidgetItem("×" + str(self.bt1)))
                kfcmain.main_ui.tableWidget.setItem(row_count, 2, QTableWidgetItem(str(self.num_hamburg)))
            if self.bt2 != 0:
                row_count = kfcmain.main_ui.tableWidget.rowCount()
                kfcmain.main_ui.tableWidget.insertRow(row_count)
                kfcmain.main_ui.tableWidget.setItem(row_count, 0, QTableWidgetItem(normal.normal_ui.label_5.text()))
                kfcmain.main_ui.tableWidget.setItem(row_count, 1, QTableWidgetItem("×" + str(self.bt2)))
                kfcmain.main_ui.tableWidget.setItem(row_count, 2, QTableWidgetItem(str(self.num_chicken)))
            if self.bt3 != 0:
                row_count = kfcmain.main_ui.tableWidget.rowCount()
                kfcmain.main_ui.tableWidget.insertRow(row_count)
                kfcmain.main_ui.tableWidget.setItem(row_count, 0, QTableWidgetItem(normal.normal_ui.label_8.text()))
                kfcmain.main_ui.tableWidget.setItem(row_count, 1, QTableWidgetItem("×" + str(self.bt3)))
                kfcmain.main_ui.tableWidget.setItem(row_count, 2, QTableWidgetItem(str(self.num_fries)))
            if self.bt4 != 0:
                row_count = kfcmain.main_ui.tableWidget.rowCount()
                kfcmain.main_ui.tableWidget.insertRow(row_count)
                kfcmain.main_ui.tableWidget.setItem(row_count, 0, QTableWidgetItem(normal.normal_ui.label_11.text()))
                kfcmain.main_ui.tableWidget.setItem(row_count, 1, QTableWidgetItem("×" + str(self.bt4)))
                kfcmain.main_ui.tableWidget.setItem(row_count, 2, QTableWidgetItem(str(self.num_tea)))
            if self.bt6 != 0:
                row_count = kfcmain.main_ui.tableWidget.rowCount()
                kfcmain.main_ui.tableWidget.insertRow(row_count)
                kfcmain.main_ui.tableWidget.setItem(row_count, 0, QTableWidgetItem(normal.normal_ui.label_14.text()))
                kfcmain.main_ui.tableWidget.setItem(row_count, 1, QTableWidgetItem("×" + str(self.bt6)))
                kfcmain.main_ui.tableWidget.setItem(row_count, 2, QTableWidgetItem(str(self.num_ice)))


class Package(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.package_ui = Ui_Package()
        self.package_ui.setupUi(self)

        # 初始化各套餐加入订单按钮点击次数
        self.bt1 = 0
        self.bt2 = 0
        # 初始化返回按钮点击次数
        self.bt3 = 0
        # 按钮绑定方法
        btn_pack1 = self.package_ui.pushButton
        btn_pack1.clicked.connect(self.order_pack1)
        btn_pack2 = self.package_ui.pushButton_2
        btn_pack2.clicked.connect(self.order_pack2)
        btn_return = self.package_ui.pushButton_3
        btn_return.clicked.connect(self.pac_show)

    # 显示套餐界面
    def pac_order(self):
        self.package_ui.label_5.setPixmap(QPixmap('./picture/套餐2.jpg'))
        self.package_ui.label_5.setScaledContents(True)
        self.package_ui.label_6.setPixmap(QPixmap('./picture/套餐1.jpg'))
        self.package_ui.label_6.setScaledContents(True)
        # 套餐价格
        self.price_pack1 = 89.0
        self.price_pack2 = 67.0
        self.package_ui.label.setText(str(self.price_pack1) + "元/份")
        self.package_ui.label_2.setText(str(self.price_pack2) + "元/份")
        package.show()

    def order_pack1(self):
        self.bt1 += 1

    def order_pack2(self):
        self.bt2 += 1

    def pac_show(self):
        self.bt3 += 1

        package.hide()

        self.num_pack1 = self.price_pack1 * self.bt1
        self.num_pack2 = self.price_pack2 * self.bt2

        if self.bt3 > 1:
            for row_index in range(kfcmain.main_ui.tableWidget.rowCount()):
                name.append(kfcmain.main_ui.tableWidget.item(row_index, 0).text())
            if '翅桶辣堡奥堡套餐' in name:
                kfcmain.main_ui.tableWidget.setItem(name.index('翅桶辣堡奥堡套餐'), 1, QTableWidgetItem("×" + str(self.bt1)))
                kfcmain.main_ui.tableWidget.setItem(name.index('翅桶辣堡奥堡套餐'), 2, QTableWidgetItem(str(self.num_pack1)))
            if '翅桶辣堡奥堡套餐' not in name:
                if self.bt1 != 0:
                    row_count = kfcmain.main_ui.tableWidget.rowCount()
                    kfcmain.main_ui.tableWidget.insertRow(row_count)
                    kfcmain.main_ui.tableWidget.setItem(row_count, 0,
                                                        QTableWidgetItem(package.package_ui.label_3.text()))
                    kfcmain.main_ui.tableWidget.setItem(row_count, 1, QTableWidgetItem("×" + str(self.bt1)))
                    kfcmain.main_ui.tableWidget.setItem(row_count, 2, QTableWidgetItem(str(self.num_pack1)))
            if '万圣节日劲堡桶' in name:
                kfcmain.main_ui.tableWidget.setItem(name.index('万圣节日劲堡桶'), 1, QTableWidgetItem("×" + str(self.bt2)))
                kfcmain.main_ui.tableWidget.setItem(name.index('万圣节日劲堡桶'), 2, QTableWidgetItem(str(self.num_pack2)))
            if '万圣节日劲堡桶' not in name:
                if self.bt2 != 0:
                    row_count = kfcmain.main_ui.tableWidget.rowCount()
                    kfcmain.main_ui.tableWidget.insertRow(row_count)
                    kfcmain.main_ui.tableWidget.setItem(row_count, 0,
                                                        QTableWidgetItem(package.package_ui.label_4.text()))
                    kfcmain.main_ui.tableWidget.setItem(row_count, 1, QTableWidgetItem("×" + str(self.bt2)))
                    kfcmain.main_ui.tableWidget.setItem(row_count, 2, QTableWidgetItem(str(self.num_pack2)))
        else:
            if self.bt1 != 0:
                row_count = kfcmain.main_ui.tableWidget.rowCount()
                kfcmain.main_ui.tableWidget.insertRow(row_count)
                kfcmain.main_ui.tableWidget.setItem(row_count, 0, QTableWidgetItem(package.package_ui.label_3.text()))
                kfcmain.main_ui.tableWidget.setItem(row_count, 1, QTableWidgetItem("×" + str(self.bt1)))
                kfcmain.main_ui.tableWidget.setItem(row_count, 2, QTableWidgetItem(str(self.num_pack1)))
            if self.bt2 != 0:
                row_count = kfcmain.main_ui.tableWidget.rowCount()
                kfcmain.main_ui.tableWidget.insertRow(row_count)
                kfcmain.main_ui.tableWidget.setItem(row_count, 0, QTableWidgetItem(package.package_ui.label_4.text()))
                kfcmain.main_ui.tableWidget.setItem(row_count, 1, QTableWidgetItem("×" + str(self.bt2)))
                kfcmain.main_ui.tableWidget.setItem(row_count, 2, QTableWidgetItem(str(self.num_pack2)))


class Activity(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.activity_ui = Ui_Activity()
        self.activity_ui.setupUi(self)

        # 初始化各活动加入订单按钮点击次数
        self.bt1 = 0
        # 初始化返回按钮点击次数
        self.bt3 = 0
        # 绑定方法
        btn_act1 = self.activity_ui.pushButton
        btn_act1.clicked.connect(self.order_act1)
        btn_act2 = self.activity_ui.pushButton_2
        btn_act2.clicked.connect(self.order_act2)
        btn_return = self.activity_ui.pushButton_3
        btn_return.clicked.connect(self.act_show)

    def act_order(self):
        self.activity_ui.label_4.setPixmap(QPixmap('./picture/活动1.jpg'))
        self.activity_ui.label_4.setScaledContents(True)
        self.activity_ui.label_8.setPixmap(QPixmap('./picture/活动2.jpg'))
        self.activity_ui.label_8.setScaledContents(True)
        # 活动价格
        self.price_act1 = 29.0
        self.price_act2 = 69.0
        self.activity_ui.label.setText(str(self.price_act1) + "元/份  原价:" + str(self.price_act1 + 7) + "元/份")
        self.activity_ui.label_5.setText(str(self.price_act2) + "元/份  原价:" + str(self.price_act2 + 10) + "元/份")
        activity.show()

    def order_act1(self):
        self.bt1 += 1

    def order_act2(self):
        QMessageBox.information(self, "对不起", "活动还没有开始，敬请期待！", QMessageBox.Yes)

    def act_show(self):
        self.bt3 += 1

        activity.hide()

        self.num_act1 = self.price_act1 * self.bt1

        if self.bt3 > 1:
            for row_index in range(kfcmain.main_ui.tableWidget.rowCount()):
                name.append(kfcmain.main_ui.tableWidget.item(row_index, 0).text())
            if '葡式蛋挞5只' in name:
                kfcmain.main_ui.tableWidget.setItem(name.index('葡式蛋挞5只'), 1, QTableWidgetItem("×" + str(self.bt1)))
                kfcmain.main_ui.tableWidget.setItem(name.index('葡式蛋挞5只'), 2, QTableWidgetItem(str(self.num_act1)))
            if '葡式蛋挞5只' not in name:
                if self.bt1 != 0:
                    row_count = kfcmain.main_ui.tableWidget.rowCount()
                    kfcmain.main_ui.tableWidget.insertRow(row_count)
                    kfcmain.main_ui.tableWidget.setItem(row_count, 0,
                                                        QTableWidgetItem(activity.activity_ui.label_3.text()))
                    kfcmain.main_ui.tableWidget.setItem(row_count, 1, QTableWidgetItem("×" + str(self.bt1)))
                    kfcmain.main_ui.tableWidget.setItem(row_count, 2, QTableWidgetItem(str(self.num_act1)))
        else:
            if self.bt1 != 0:
                row_count = kfcmain.main_ui.tableWidget.rowCount()
                kfcmain.main_ui.tableWidget.insertRow(row_count)
                kfcmain.main_ui.tableWidget.setItem(row_count, 0, QTableWidgetItem(activity.activity_ui.label_3.text()))
                kfcmain.main_ui.tableWidget.setItem(row_count, 1, QTableWidgetItem("×" + str(self.bt1)))
                kfcmain.main_ui.tableWidget.setItem(row_count, 2, QTableWidgetItem(str(self.num_act1)))
import img_rc

if __name__ == "__main__":
    app = QApplication(sys.argv)

    kfcmain = KFC_Main()
    normal = Normal()
    package = Package()
    activity = Activity()
    # 显示主界面
    kfcmain.person()
    # 绑定按钮
    btn_normal = kfcmain.main_ui.pushButton_2
    btn_normal.clicked.connect(normal.nor_order)
    btn_package = kfcmain.main_ui.pushButton_3
    btn_package.clicked.connect(package.pac_order)
    btn_activity = kfcmain.main_ui.pushButton_4
    btn_activity.clicked.connect(activity.act_order)
    # 初始化name列表
    name = []

    sys.exit(app.exec_())
