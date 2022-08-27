import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

from part3.lib import common

# common.fn()

o_log = common.getLogger('o_owen')
o_log.debug('owen打印的debug信息')
o_log.warning('owen打印的warning信息')


