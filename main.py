import traceback
from flask import Flask,jsonify

app=Flask(__name__)

@app.route('/demo',methods=['GET'])
def demo():
    try:
        return jsonify({'Success':'Demo api'})
    except Exception as e:
        print(traceback.print_exc)
        return jsonify({'Failure':'Demo Failed'})

if __name__ == '__main__':
    app.run(debug=True)
