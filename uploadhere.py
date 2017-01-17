import os
from bottle import post, route, run, request
from bottle import static_file

@route('/')
def server_static():
    return static_file('uploader.html', root='.')

@route('/upload', method='POST')
def do_upload():
    upload     = request.files.get('upload')
    name, ext = os.path.splitext(upload.filename)
    save_path = '.' 
    upload.save(save_path) # appends upload.filename automatically
    return 'OK'

run(host='0.0.0.0', port=8080)
