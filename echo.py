# save this as app.py
from flask import Flask,request,jsonify
from pprint import pprint
app = Flask(__name__)

@app.route('/', defaults={'path': ''},methods=['GET','POST'])
@app.route('/<path:path>',methods=['GET','POST'])
def handler(path):
    echo = dict(
                ip=str(request.remote_addr),
                headers=dict(request.headers),
                args=dict(request.args),
                data=dict(request.json) if request.content_type == "application/json" else None,
                path=path
                )
    pprint(echo)
    return jsonify(echo)

if __name__ == "__main__":
    app.run(debug=True)