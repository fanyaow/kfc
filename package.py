from PyQt5 import QtCore, QtWidgets

class Ui_Package(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(728, 393)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(90, 280, 91, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(340, 280, 93, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(100, 250, 72, 15))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(350, 250, 72, 15))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(80, 220, 131, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(330, 220, 111, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(60, 20, 161, 171))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(300, 20, 171, 171))
        self.label_6.setObjectName("label_6")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(560, 280, 101, 41))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "套餐"))
        self.pushButton.setText(_translate("Form", "加入订单"))
        self.pushButton_2.setText(_translate("Form", "加入订单"))
        self.label.setText(_translate("Form", "钱1"))
        self.label_2.setText(_translate("Form", "钱2"))
        self.label_3.setText(_translate("Form", "翅桶辣堡奥堡套餐"))
        self.label_4.setText(_translate("Form", "万圣节日劲堡桶"))
        self.label_5.setText(_translate("Form", "TextLabel"))
        self.label_6.setText(_translate("Form", "TextLabel"))
        self.pushButton_3.setText(_translate("Form", "返回"))
import img_rc