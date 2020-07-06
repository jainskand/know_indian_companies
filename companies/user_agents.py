#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random


def getRandomUserAgent():
    user_agents = [
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.8) Gecko/20071008 Firefox/2.0.0.8",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.7) Gecko/20070914 Firefox/2.0.0.7",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.4) Gecko/20070515 Firefox/2.0.0.4",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:77.0) Gecko/20100101 Firefox/77.0",
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/531.0 (KHTML, like Gecko) Chrome/3.0.183.1 Safari/531.0",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/531.0 (KHTML, like Gecko) Chrome/3.0.187.1 Safari/531.0",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.1 Safari/532.0",
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/531.3 (KHTML, like Gecko) Chrome/3.0.193.2 Safari/531.3",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.17 Safari/532.0",
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)",
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322)",
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727)",
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)",
        "Opera/9.22 (Windows NT 5.1; U; en)",
        "Opera/9.24 (Windows NT 5.1; U; en)    ",
        "Opera/9.23 (Windows NT 5.1; U; en)    ",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)    ",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 2.0.50727)    ",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; InfoPath.1)    "
    ]
    return random.choice(user_agents)
