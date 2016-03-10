#!/usr/bin/python
# -*- coding:utf-8 -*-

import pysvn
import time
import datetime

class svnSync:

    def __init__(self, urls):

        self.svn_user="user"
        self.svn_password='password'
        self.svn_urls = urls

        # 日志条数
        self.log_num = 100

    # 获取日志
    def getLog(self):

        try:
            client = pysvn.Client()
            #参考 http://pysvn.tigris.org/docs/pysvn_prog_ref.html#pysvn_client_callback_get_login
            client.callback_get_login = self.svn_login

            # 参考 http://pysvn.tigris.org/docs/pysvn_prog_ref.html#pysvn_client_log
            # print self.svn_login
            startTime = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
            startTimespan = time.mktime(time.strptime(str(startTime),'%Y-%m-%d %H:%M:%S'))

            s = ''
            index = 1
            for url in self.svn_urls:
                # s += url + ':\n'
                # print(url)
                log = client.log(url, revision_start=pysvn.Revision(pysvn.opt_revision_kind.date, time.time()), revision_end=pysvn.Revision(pysvn.opt_revision_kind.date, startTimespan), limit=self.log_num)
                for info in log:
                    logAuthor = info.author
                    logTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(info.date))
                    if logAuthor == self.svn_user and len(info.message.strip()) > 2:
                        # s += str(index) + '. ' + ' '.join([logTime, info.author, info.message])
                        s += str(index) + '. ' + info.message
                        index += 1
                        # print(logTime, info.author, info.message)

            print(s)

        except Exception as e:

            print('svn error: ', e)

    # svn 登录验证函数
    def svn_login(self, realm, username, may_save):
        return True, self.svn_user, self.svn_password, False

if __name__ == '__main__':
    urls = ['https://fileserver/svn/RY100Platform/trunk', 'https://fileserver/svn/RY100Platform/branches']
    svn = svnSync(urls)
    svn.getLog()