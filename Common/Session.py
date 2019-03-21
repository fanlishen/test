"""
封装获取cookie方法
"""
from webbrowser import Mozilla

import request
from Common import Log
from Conf import Config

class Session:
    def __init__(self):
        self.config=Config.Config()
        self.log=Log.MyLog()

    def get_session(self,env):
        """
        获取session
        :param env:
        :return:
        """
        headers ={
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko)\
                          Chrome/67.0.3396.99 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded"
        }

        if env=="debug":
            login_url='http://'+self.config.loginHost_debug
            parm=self.config.loginInfo_debug

            session_debug=request.session()
            response=session_debug.post(login_url,parm,headers=headers)
            print(response.cookies)
            self.log.debug('cookies:%s'%response.cookies.get_dict())
            return response.cookies.get_dict()

        elif env =="release":
            login_url='http://'+self.config.loginHost_relese
            parm=self.config.loginInfo_relese

            session_release=request.session()
            response=session_release.post(login_url,parm,headers=headers)
            print(response.cookies)
            self.log.debug('cookies:%s'%response.cookies.get_dict())
            return response.cookies.get_dict()

        else:
            print("get cookies error")
            self.log.error('get cookies error,please checkout')

if __name__=='__main__':
    ss=Session()
    ss.get_session('debug')