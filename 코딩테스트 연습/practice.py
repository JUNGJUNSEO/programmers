from posix import CLD_EXITED
import requests
req = requests.get('http://google.com')
try:
    if req.status_code == requests.codes.ok:
        print('seo')
except any:
    print('jun')
