# coding=gbk

# coding=utf-8

# -*- coding: UTF-8 -*-

from SDK.CCPRestSDK import REST
import ConfigParser

# ���ʺ�
accountSid = '8aaf07085d106c7f015d5dab58771fc7';

# ���ʺ�Token
accountToken = 'dd2868fe8af24330b41ab863748dbe36';

# Ӧ��Id
appId = '8aaf07085d106c7f015d5dab5b571fcd';

# �����ַ����ʽ���£�����Ҫдhttp://
serverIP = 'app.cloopen.com';

# ����˿�
serverPort = '8883';

# REST�汾��
softVersion = '2013-12-26';


# ����ģ�����
# @param to �ֻ�����
# @param datas �������� ��ʽΪ���� ���磺{'12','34'}���粻���滻���� ''
# @param $tempId ģ��Id

def sendTemplateSMS(to, datas, tempId):
    # ��ʼ��REST SDK
    rest = REST(serverIP, serverPort, softVersion)
    rest.setAccount(accountSid, accountToken)
    rest.setAppId(appId)

    result = rest.sendTemplateSMS(to, datas, tempId)
    for k, v in result.iteritems():

        if k == 'templateSMS':
            for k, s in v.iteritems():
                print '%s:%s' % (k, s)
        else:
            print '%s:%s' % (k, v)


            # sendTemplateSMS(�ֻ�����,��������,ģ��Id)