from flask import Flask, request, abort
import subprocess
import json

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        json_a = request.get_json()
        idkey = json_a['id-key']
        if idkey != "test-key":
            abort(400)
        pulltext = json_a['text']
        if pulltext == None:
            abort(400)
        command_word='/home/[username]/go/bin/algia n \"' + pulltext + '\"'
        subprocess.run(command_word, shell=True)
        return 'success',200
    else:
        abort(400)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=False,ssl_context=('[username]/nginx-proxy/certs/[YourDomainName]/fullchain.pem', '[Yusername]/nginx-proxy/certs/[YourDomailName]/key.pem'))
