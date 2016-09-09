#-*-coding:utf8-*-
import os

#-- dashboard db config --
DASHBOARD_DB_HOST = "127.0.0.1"
DASHBOARD_DB_PORT = 3306
DASHBOARD_DB_USER = "kaoala"
DASHBOARD_DB_PASSWD = "KaoalaAdd"
DASHBOARD_DB_NAME = "dashboard"

#-- graph db config --
GRAPH_DB_HOST = "127.0.0.1"
GRAPH_DB_PORT = 3306
GRAPH_DB_USER = "kaoala"
GRAPH_DB_PASSWD = "KaoalaAdd"
GRAPH_DB_NAME = "graph"

#-- app config --
DEBUG = True
SECRET_KEY = "secret-key"
SESSION_COOKIE_NAME = "open-falcon"
PERMANENT_SESSION_LIFETIME = 3600 * 24 * 30
SITE_COOKIE = "open-falcon-ck"

#-- query config --
QUERY_ADDR = "http://127.0.0.1:9966"

BASE_DIR = "/home/work/open-falcon/dashboard/"
LOG_PATH = os.path.join(BASE_DIR,"log/")

try:
    from rrd.local_config import *
except:
    pass
