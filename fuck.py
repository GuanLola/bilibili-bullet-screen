#coding=utf-8
import requests,time,random
import configparser  #配置文件信息
 
target = configparser.ConfigParser() #文件对象
target.read(r'/Users/guanyueming/Desktop/test/t.ini',encoding='utf-8')  #读取文件<br>
# message = target.get('dm','0')
# progress = message.split('&')[1]
# print(message.split('&')[0], int(float(progress)*1000))

while True:
    # message = target.get('我的弹幕',str(random.randint(1,8)))
    message = target.get('dm',str(random.randint(0,390)))
    msg = message.split('&')[0].strip("'")
    progress = int(float(message.split('&')[1])*1000)
    url = 'https://api.bilibili.com/x/v2/dm/post'
    cookie = {'cookie':"_uuid=7D3F7A22-0C9A-0ECE-0688-A05DDC000C9B32288infoc; buvid3=E5B6440E-2AF3-4F02-A46E-C64FF89C85FE138366infoc; UM_distinctid=173db101ae0498-0291d080303e2-31677303-2a3000-173db101ae16b1; rpdid=|(umR~)kkkkR0J'ulm~u|)uJl; DedeUserID=21543774; DedeUserID__ckMd5=fe79ef6131a1d28f; SESSDATA=183d270e%2C1613295868%2C96afc*81; bili_jct=65905163ff98d5833586d93a2501c02e; blackside_state=1; CURRENT_QUALITY=80; CURRENT_FNVAL=80; LIVE_BUVID=AUTO9616008526894666; PVID=1; bp_video_offset_21543774=465193963735260173; bp_t_offset_21543774=465193963735260173; bsource=search_baidu; bfe_id=61a513175dc1ae8854a560f6b82b37af; sid=ayr6ib37"}
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