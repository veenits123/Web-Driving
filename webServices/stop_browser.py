from flask import request

import os


def StopBrowser():

    if 'browser' in request.args:

        browser_name = str(request.args['browser'])
        print(browser_name)

        if browser_name == "chrome":
            os.system("killall -9  'Google Chrome'")
            return "CHROME CLOSED"

        elif browser_name == "mozilla":
            os.system("killall -9 'firefox'")
            return "MOZILLA CLOSED"

        else:
            return "This browser isnt available"

    else:
        return "Browser name required"
