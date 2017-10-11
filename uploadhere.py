import os
from bottle import post, route, run, request, response
from bottle import static_file

@route('/')
def server_static():
    return static_file('uploader.html', root='.')

@route('/upload', method='POST')
def do_upload():
    upload = request.files.get('upload')
    if upload is not None:
        name, ext = os.path.splitext(upload.filename)
        save_path = '.' 
        upload.save(save_path)  # appends upload.filename automatically
        response.status = 201
        return response    
    return "You missed a field."

run(host='0.0.0.0', port=8080)
