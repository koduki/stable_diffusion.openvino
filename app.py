# -*- coding: utf-8 -*-
from bottle import route, run, template, response


@route('/output.png')
def sample_image():
    response.content_type = 'image/png'
    with open('./output.png', 'rb') as fh:
        content = fh.read()
    response.set_header('Content-Length', str(len(content)))
    return content


run(host='localhost', port=8080)