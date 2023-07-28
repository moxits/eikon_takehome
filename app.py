from flask import Flask
from etl import main as etl_process

app = Flask(__name__)

@app.route('/trigger_etl', methods=['POST'])
def start_etl():
    etl_process()
    return "ETL process started", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0',port='80')