from flask import request

import webbrowser


def StartBrowser():
    if 'browser' in request.args and 'url' in request.args:

        browser_name = str(request.args['browser'])
        url = str(request.args['url'])
        print(browser_name)
        print(url)

        if browser_name == "chrome":
            chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
            webbrowser.get(chrome_path).open(url)
            return "Chrome fired up with specified url"

        elif browser_name == "mozilla":
            mozilla_path = 'open -a /Applications/Firefox.app %s'
            webbrowser.get(mozilla_path).open(url)
            return "Mozilla fired up with specified url"

        else:
            return "This browser isnt available"

    elif 'browser' in request.args:
        browser_name = str(request.args['browser'])

        if browser_name == "chrome":
            chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
            webbrowser.get(chrome_path).open("https://www.google.com")
            return "Chrome fired up"

        elif browser_name == "mozilla":
            mozilla_path = 'open -a /Applications/Firefox.app %s'
            webbrowser.get(mozilla_path).open("https://www.google.com")
            return "Mozilla fired up "

        else:
            return "This browser isnt available"

    elif 'url' in request.args:
        return "Error only url provided"
