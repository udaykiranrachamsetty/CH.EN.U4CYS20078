from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

def fetch_data_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data
    except Exception as e:
        return {'error': f'Error fetching data from {url}: {str(e)}'}

@app.route('/numbers', methods=['GET'])
def get_numbers():
    urls = request.args.getlist('url')
    result = []

    for url in urls:
        data = fetch_data_from_url(url)
        result.append(data)

    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8008)
