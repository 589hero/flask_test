from flask import Blueprint, request, jsonify
import json

bp = Blueprint('imginfo', __name__, url_prefix='/imginfo')


@bp.route('/imgtojson', methods=['GET'])
def imginfo():
    if request.method == 'GET':
        with open('./imginfo.json', "r") as json_file:
            json_data = json.load(json_file)

        scanid = len(json_data['scandata']) + 1
        img_name = request.args.get('in', 'No Image')  # Image Name
        scandate = request.args.get('d', '0000-00-00')

        new_data = {'scanid': scanid, 'imgname': img_name, 'scandate': scandate}

        if img_name != 'No Image' and scandate != '0000-00-00':
            json_data['scandata'].append(new_data)

            with open('./imginfo.json', 'w') as outfile:
                json.dump(json_data, outfile, indent=4)

        return jsonify(json_data)