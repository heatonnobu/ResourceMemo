# ResourceMemo
各种网络资源备忘

## 各种API

### 腾讯
#### QQ空间
1. 获取qq号昵称和头像

[http://users.qzone.qq.com/fcg-bin/cgi_get_portrait.fcg?uins=11111111,22222222](http://users.qzone.qq.com/fcg-bin/cgi_get_portrait.fcg?uins=11111111,22222222)

qq号可以使用`,`分隔，一次查询多个qq号

#### QQ地图
1. IP定位

[http://apis.map.qq.com/ws/location/v1/ip?key=7FCBZ-ORPKI-ORHGE-5MABM-L5DQZ-OJFFR&ip=117.144.208.179](http://apis.map.qq.com/ws/location/v1/ip?key=7FCBZ-ORPKI-ORHGE-5MABM-L5DQZ-OJFFR&ip=117.144.208.179)


2. 经纬度定位

[http://apis.map.qq.com/ws/geocoder/v1?key=7FCBZ-ORPKI-ORHGE-5MABM-L5DQZ-OJFFR&location=31.27925700,121.43915600](http://apis.map.qq.com/ws/geocoder/v1?key=7FCBZ-ORPKI-ORHGE-5MABM-L5DQZ-OJFFR&location=31.27925700,121.43915600)


## 各种脚本

### python
#### svn.py  
使用pysvn库读取svn日志记录  
pysvn文档地址[http://pysvn.tigris.org/docs/pysvn_prog_ref.html](http://pysvn.tigris.org/docs/pysvn_prog_ref.html)  


#### test.py  
监控chageci web api是否正常运行，如果不正常，通过pushbullet接口推送通知  
pushbullet开发文档地址[https://docs.pushbullet.com/](https://docs.pushbullet.com/)
