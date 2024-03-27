from enum import Enum

AHA_URL = "http://earnaha.com"

class PageName(Enum):
    PRE = 'PRE'
    LOG_IN = 'LOGIN'
    MAIN = 'MAIN'
    PROFILE = 'PROFILE'

class ELE_ACT(Enum):
    CLICK = 'CLICK'
    SEND_KEY = 'SEND_KEY'
    SWITCH_FRAME = 'SWITCH_FRAME'
    CLICL_LOCATION = 'CLICL_LOCATION'
    MOVE = 'Move'

class TestResult(Enum):
    PASS = "PASS"
    FAIL = 'FAIL'
    SKIP = 'SKIP'
    ERROR = 'ERROR'