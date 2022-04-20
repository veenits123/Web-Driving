from flask import request

import os


def CleanUp():

    if 'browser' in request.args:
        browser_name = str(request.args['browser'])
        print(browser_name)

        if browser_name == "chrome":
            os.system("rm -rf /Users/vee_nits123/Library/Caches/Google/Chrome/")
            os.system(
                "rm -rf /Users/vee_nits123/Library/Application\ Support/Google/Chrome/Default")
            return "Chrome Data IS CLEARED"

        elif browser_name == "mozilla":
            os.system(
                "rm -rf /Users/vee_nits123/Library/Caches/Firefox/Profiles/9osmren4.Work\ Profile")
            os.system(
                "rm -rf /Users/vee_nits123/Library/Application\ Support/Firefox/Profiles/9osmren4.Work\ Profile/*")
            return "Mozilla Data IS CLEARED"

        else:
            return "Not a Browser!"

    else:
        return "No query passed for filtration"
