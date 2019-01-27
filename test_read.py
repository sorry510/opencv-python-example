#! /usr/bin/env python
# -*- coding:utf-8 -*-

from jpype import *
import os.path

# 识别条形码
def barCode(code_img_path):
    try:
        # 启动JVM
        if not isJVMStarted():
            startJVM(getDefaultJVMPath(), "-ea", "-Djava.awt.headless=true",("-Djava.class.path=%s" % ("./javase-2.2.jar" + "" + "./core-2.2.jar")))

        File = JClass("java.io.File")
        BinaryBitmap = JClass("com.google.zxing.BinaryBitmap")
        DecodeHintType = JClass("com.google.zxing.DecodeHintType")
        LuminanceSource = JClass("com.google.zxing.LuminanceSource")
        BufferedImageLuminanceSource = JClass("com.google.zxing.client.j2se.BufferedImageLuminanceSource")
        MultiFormatReader = JClass("com.google.zxing.MultiFormatReader")
        NotFoundException = JClass("com.google.zxing.NotFoundException")
        Result = JClass("com.google.zxing.Result")
        HybridBinarizer = JClass("com.google.zxing.common.HybridBinarizer")
        Hashtable = JClass("java.util.Hashtable")
        BufferedImage = JClass("java.awt.image.BufferedImage")
        ImageIO = JClass("javax.imageio.ImageIO")

        image = ImageIO.read(File(code_img_path))
        source = BufferedImageLuminanceSource(image)
        bitmap = BinaryBitmap(HybridBinarizer(source))
        hints = Hashtable()
        hints.put(DecodeHintType.CHARACTER_SET, "GBK")
        # hints.put(DecodeHintType.CHARACTER_SET, "utf-8")
        #优化精度
        hints.put(DecodeHintType.TRY_HARDER, True)
        #复杂模式
        # hints.put(DecodeHintType.PURE_BARCODE, True)
        result = MultiFormatReader().decode(bitmap, hints)
        return str(result)
    except JavaException as ex:
        print(ex.javaClass(), ex.stacktrace())
        # shutdownJVM()
        return False

if __name__ == '__main__':
    # print('t---', barCode('../images/t.png'))
    print('t1---', barCode('./imgs/code1.jpg'))
    # print('t2---', barCode('./imgs/code2.jpg'))
    # print('t3---', barCode('../images/t3.png'))
    # print('t4---', barCode('../images/t4.png'))
    # print('t5---', barCode('../images/t5.png'))



