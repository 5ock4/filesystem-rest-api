from flask import Flask, jsonify, abort
import os

#TODO Make it as a parameter for a script
#TODO Check what status it returns
#TODO Check if .. does work in path
BASE_DIR = 'E:\seznam_ukol'
app = Flask(__name__)

@app.route('/', defaults={'req_path': ''}, methods=['GET'])
@app.route('/<path:req_path>', methods=['GET'])
def get_path(req_path):
    abs_path = os.path.join(BASE_DIR, req_path)

    if not os.path.exists(abs_path):
        return abort(404)
    
    if os.path.isfile(abs_path):
        return { os.path.basename(abs_path): { 'ctime' : os.path.getctime(abs_path),
                                               'mtime' : os.path.getmtime(abs_path),
                                               'size' : os.path.getsize(abs_path) }
               }

    folder_info = {}
    for i in os.listdir(abs_path):
        full_path = os.path.join(abs_path, i)
        
        if os.path.isdir(full_path):
            folder_info.update({i: 'dir'})
        else:
            folder_info.update({ i: { 'ctime' : os.path.getctime(full_path),
                                      'mtime' : os.path.getmtime(full_path),
                                      'size' : os.path.getsize(full_path) }
                               })
    
    return jsonify(folder_info)

@app.route('/<path:req_path>', methods=['DELETE'])
def del_path(req_path):
    abs_path = os.path.join(BASE_DIR, req_path)

    if not os.path.exists(abs_path):
        return abort(404)

    if os.path.isfile(abs_path):
        os.remove(abs_path)
        return jsonify({os.path.basename(abs_path): 'deleted'})

    if not os.listdir(abs_path):
        os.rmdir(abs_path)
        return jsonify({os.path.basename(abs_path): 'deleted'})
    else:
        return jsonify({os.path.basename(abs_path): 'dir not empty'})


@app.route('/<path:req_path>', methods=['PUT'])
def create_file(req_path):
    abs_path = os.path.join(BASE_DIR, req_path)
    
    if not os.path.exists(abs_path):
        # TODO: CHECK IF FLASKS HAS CONSTANT NOT_FOUND OR SOMETHING
        return abort(404)
    
    open(abs_path, 'a').close()

    return jsonify({ os.path.basename(abs_path): 'created' })

if __name__ == '__main__':
    app.run(debug=True)