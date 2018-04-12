# jiekou
接口。。
adb shell am start -a android.intent.action.SENDTO -d sms:10086 --es sms_body  hello
#调用短信


adb shell svc data enable/disadle   # //操作数据开关


"""
appium -a 127.0.0.1 -p 4723 --session-override      


-a 是指定监听的ip（也可写成 --address），后面“127.0.0.1”可以改为你需要的ip地址；

-p 是指定监听的端口（也可写成 --port），也可以修改为你需要的端口；

--session-override 是指覆盖之前的session


"""



"""
命令行中输入：appium -a 127.0.0.1 -p 4727 -bp 4728 --chromedriver-port 9519 -U xiaomi --session-override
-bp 是连接Android设备bootstrap的端口号，默认是4724（也可写成--bootstrap-port）

--chromedriver-port 是chromedriver运行需要指定的端口号，默认是9515

-U 是连接的设备名称，如"adb devices"获取的设备标识（也可写成--udid）
"""


http://m.blog.csdn.net/json5/article/details/78643256   


http://download.csdn.net/download/shj0605010318/9728115   download




"""
appium改动

用set_text()， selenium 3.4后send_keys，就用不了了， 取而代之的是set_value，输入速度提高了很多，set_text()用来输入中文

set_value（" 1231"）
set_text(" 哈哈 ")



https://www.rddoc.com/doc/Python/3.6.0/zh/library/tkinter/                 tkinter---zhong



"""针对appium 执行用例失败后断言


        try:
            self.assertEqual(y, 'ON', 'switch fail.....')
        except Exception as e:
            self.driver.save_screenshot('fail.png')


"""
     self.driver.tap([(476,305)], 500)  appium tap 事件

netsh wlan show profile key=clear ssid     查看wifi密码


http://www.cnblogs.com/xinleishare/p/4793538.html      Appium 服务命令行参数

https://testerhome.com/wiki/appcrawler          testerhome









self.driver.find_element(By.XPATH,"//*[@text='Audio Frequency Line Test']").click()














http://pro.sr1.me/post/android-sdk-download-links

http://mirrors.neusoft.edu.cn/android/repository/
