#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
为 word 转换出来的 html 生成侧栏目录。使用方法：
    1）word 另存为筛选过的网页（word 中用到的图片会保存到 同名.fld 目录中）
    2）手动修改 srouce_html、target_html 的值
    3）运行程序生成完毕
"""

from jinja2 import Environment, FileSystemLoader
from bs4 import BeautifulSoup
import sys, codecs, os

source_html = '/Users/a123/Downloads/temp.html'
target_html = os.path.split(source_html)[0] + '/temp_toc.html'

soup = BeautifulSoup(open(source_html, 'r').read(), 'html.parser')

style = unicode(soup.head.style.get_text())
content = "\n".join([unicode(content) for content in soup.body.children])

code = Environment(loader=FileSystemLoader(sys.path[0] + '/other_libs/template')).get_template("word_toc.html")\
    .render(word_style=style, body_content=content)

with codecs.open(target_html, 'w', 'utf-8') as code_file:
    code_file.write(code)
