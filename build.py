#!/usr/bin/env python
#coding=utf-8

import json
import codecs


def read(file):
    with codecs.open(file,encoding='utf-8') as f:
        content = f.read()
    return content


res = json.loads(read('map.json'))

result = '';

with codecs.open('preview.html',encoding='utf-8') as f:
    for line  in f.readlines():
        for x in res :
            if x['type'] in line and x['file'] in line:
                if x['type'] in 'script':
                    line ='<script type="text/javascript">' + read(x['file']) + '</script>'
                else:
                    line = '<style type="text/css">' + read(x['file']) + '</style>'
                break
        result += line

with codecs.open('./dist/preview.html',encoding='utf-8',mode='w') as f:
    f.write(result)


print('build successfully!')
print('please checkout `dist/`')





