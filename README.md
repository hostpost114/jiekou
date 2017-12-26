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
