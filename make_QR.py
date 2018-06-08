#!/usr/bin/python
#-*- codong: utf-8 -*- 

import qrcode
import pygooglechart

#1Nem = 1000000mosaic 

address = "NDOZFGZTFYVSKHGCSPZEFKM2WFQSXM66M5MCHYNP"
mosaic = 1000000
send_amount = 100 * mosaic 
message = "test"
wallet_name = "test"

if __name__ == '__main__':
    qrdata = '{"v":2,"type":2,"data":{"addr":"' + address + '","amount":' + str(send_amount) + ',"msg":"' + message + '","name":"' + wallet_name + '"}}'
    #qrdata = '{"v":2,"type":2,"data":{"addr":"NDOZFGZTFYVSKHGCSPZEFKM2WFQSXM66M5MCHYNP","amount":5000000,"msg":"test","name":"test"}}'

    QR = qrcode.QRCode(
            version=2,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=6,
            border=4,
            )
    QR.add_data(qrdata)
    QR.make(fit=True)
    img = QR.make_image(fill_color="white", back_color="black")
    img.save('qr.bmp')

