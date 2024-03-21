from enum import Enum

AHA_URL = "http://earnaha.com"

class PageName(Enum):
    PRE = 'PRE'
    LOG_IN = 'LOG_IN'
    MAIN = 'MAIN'
    PROFILE = 'PROFILE'

class ELE_ACT(Enum):
    CLICK = 'CLICK'
    SEND_KEY = 'SEND_KEY'