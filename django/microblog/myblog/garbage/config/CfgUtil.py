import configparser
import os

__path = os.getcwd()
__conf_file = __path + os.path.sep + "conf.ini"
print(__conf_file)
__cgf_section = "config"
__db_section = "db"
__tcp_section = "tcp"
__proxy_section = "proxy"

conf = configparser.ConfigParser()
conf.read(__conf_file)

def get_cfg(name):
    val = conf.get(__cgf_section, name)
    return val

def get_db(name):
    val = conf.get(__db_section, name)
    return val

def get_tcp(name):
    val = conf.get(__tcp_section, name)
    return val

def get_proxy(name):
    val = conf.get(__proxy_section, name)
    return val

if __name__ == "__main__":
    thread_num = CfgUtil.get_cfg("thread_num")
