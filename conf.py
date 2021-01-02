# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
enable_jsdelivr = {
    "enabled": True,
    "repo": "stormycloudy/stormycloudy.github.io@master"
}

# 站点设置
site_name = "Stormycloudy"
site_logo = "${site_prefix}logo.png"
site_build_date = "2019-12-31T15:10-05:00"
author = "Shay L"
email = "xuecliu@iu.edu"
author_homepage = "http://pages.iu.edu/~xuecliu"
description = "Life is good."
key_words = ['ShayLiu', 'stormycloudy', 'atmosphericscience', 'blog']
language = 'en'
external_links = [
     {
        "name": "Shay Liu's research",
        "url": "https://xuecliu.pages.iu.edu/",
        "brief": "My research website on IU pages."
    }
]
nav = [
    {
        "name": "Home",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "Archived",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "About",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
    {
        "name": " Twitter",
        "url": "https://twitter.com/baroclinicat",
        "icon": "fab fa-twitter"
    },
    {
        "name": " GitHub",
        "url": "https://github.com/stormycloudy",
        "icon": "fab fa-github"
    },
    {
        "name": " LinkedIn",
        "url": "https://www.linkedin.com/in/shayliu/",
        "icon": "fab fa-linkedin-in"
    }
]

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="icon" type="image/png" href="./logo.png">
<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.5.0/css/all.css">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Inconsolata">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
  

'''

footer_addon = ''

body_addon = ''
