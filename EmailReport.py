# -*- coding: utf-8 -*-
import sys

__author__ = 'XuJianbo'
__data__ = '2015-03-20'
"""
生成测试报告存放在项目TestReport文件下
将报告通过邮件以附件的形式发送给项目相关人员
"""
import smtplib
import os
import time
from api.apipub.Config import Config
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

from api.apidata.apiset import apiset
from api.apipub import pyapilog


def actionReport(file_path):
    # file_path is list
    for path in file_path:
        os.system("python %s" % path)


def sortReportFile(report_path):
    new_report_list = []
    try:
        for path in report_path:
            lists = os.listdir(path)
            lists.sort(key=lambda fn: os.path.getmtime(path + "/" + fn) if not os.path.isdir(path + "/" + fn) else 0)
            new_report = os.path.join(path, lists[-1])
            new_report_list.append(new_report)
        return new_report_list
    except IndexError, e:
        pyapilog.log().info("sort_report_file - There are no reports to send:")
        pyapilog.log().error(e)


def sendEmail(dir_list):
    # 邮件内容
    mail_body = ''
    mail_user = apiset().getConfigValues("email_from", "username")
    mail_pwd = apiset().getConfigValues("email_from", "password")
    mail_to = apiset().getConfigItems()
    for i in range(0, len(mail_to)):
        mail_to.append(mail_to[i][1])
    msg = MIMEMultipart()
    msg['Subject'] = apiset().getConfigValues("report", "title")
    msg['From'] = mail_user
    msg['to'] = ';'.join(mail_to)
    msg['Date'] = time.strftime('%a,%d %b %Y %H:%S %z')
    for file in dir_list:
        report_obj = open(file, 'rb')
        mail_bady_value = report_obj.read()
        mail_body += mail_bady_value
        # 创建附件，并添加到msg
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(mail_bady_value)
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(file))
        msg.attach(part)
        report_obj.close()
        # 创建MIMEText，并添加到msg
        body = MIMEText(mail_body, _subtype="html", _charset='utf-8')
        msg.attach(body)
        smtp = smtplib.SMTP()
        smtp.connect('smtp.163.com')
        smtp.login(mail_user, mail_pwd)
        smtp.sendmail(mail_user, mail_to, msg.as_string())
        smtp.quit()
        print 'email has send out !'


if __name__ == "__main__":
    try:
        tag = sys.argv[1]
        if tag == "test" or tag == "online":
            Config().setScene(tag)
            root_path = os.path.abspath(__file__)
            report_path = [os.path.join(root_path + '\\Report.py'), ]
            actionReport(report_path)
            report_list = [os.path.join(root_path + '\\TestReport'), ]
            re_list = sortReportFile(report_list)
            sendEmail(re_list)
        else:
            raise Exception
    except:
        print u"请指定正确的运行环境：test or online"