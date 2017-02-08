#!/usr/bin/env python3
import os
import http.cookies

cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
name = cookie.get("name")


def loadTo(x):
    x=5
    return x


if name is None:
    print("Set-cookie: name=value one")
    print("Content-type: text/html\n")
    print("Cookies!!!")
    print(loadTo("fff"))
else:
    print("Content-type: text/html\n")
    print("Cookies:")
    print(name.value)
