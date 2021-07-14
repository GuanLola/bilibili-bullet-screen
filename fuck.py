#coding=utf-8
import requests,time,random
import configparser  #配置文件信息
 
target = configparser.ConfigParser() #文件对象
target.read(r'/Users/Desktop/test/t.ini',encoding='utf-8')  #读取文件<br>
# message = target.get('dm','0')
# progress = message.split('&')[1]
# print(message.split('&')[0], int(float(progress)*1000))

while True:
    # message = target.get('我的弹幕',str(random.randint(1,8)))
    message = target.get('dm',str(random.randint(0,390)))
    msg = message.split('&')[0].strip("'")
    progress = int(float(message.split('&')[1])*1000)
    url = 'https://api.bilibili.com/x/v2/dm/post'
    # cookie 打开控制台检查里面粘贴过来就好
    cookie = {'cookie':""}
    form = {
        # 'fontsize':'25',
        # 'pool':'0',
        # 'mode':'1',
        # 'color':'16777215',
        # 'rnd':str(time.time()*1000000),#时间戳
        # 'msg':'真好看',
        # 'playTime':'0.08',
        # 'cid':'18447007',
        # 'date':time.strftime('%Y-%m-%d+%H:%M:%S',time.localtime(time.time())),
        # 'csrf':'3915a57109e4abe13dc752254df4bc35',
        'type': 1,
        'oid': 264223404,
        'msg': msg,
        'bvid': 'BV1iZ4y1g7ZR',
        'progress': progress,
        'color': 52480,
        'fontsize': 25,
        'pool': 0,
        'mode': 4,
        'rnd': str(round(time.time()*1000000)),
        'plat': 1,
        'csrf': '65905163ff98d5833586d93a2501c02e'
    }
    requests.post(url,cookies=cookie,data=form)
    print('发送成功', msg, progress)
    time.sleep(20)