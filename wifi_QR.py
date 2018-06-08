#!/usr/bin/python
#-*- coding: utf-8 -*- 

########################################################
#  読み込むことでWifiに接続することができるQRコードを作成する   #
########################################################

import qrcode

if __name__ == '__main__':
    network_name = ""
    security = ""
    password = ""
    qrdata = "WIFI:S:" + network_name + ";T:" + security + ";P:" + password + ";;"
    QR = qrcode.QRCode(
        version = 2,
        error_correction = qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4)
    QR.add_data(qrdata)
    QR.make(fit = True)
    img = QR.make_image(fill_color="white", back_color="black")
    img.save('qr.bmp')


    


