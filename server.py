# Create a file named `app.py`

from flask import Flask, jsonify, request
import subprocess
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/start-ansible', methods=['POST'])
def start_ansible():
    try:
        # Execute the Ansible playbook
        result = subprocess.run(['ansible-playbook', 'temperature.yml'], capture_output=True, text=True)
        return jsonify({
            'status': 'success',
            'output': result.stdout,
            'error': result.stderr
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        })

@app.route('/api/stop-ansible', methods=['POST'])
def stop_ansible():
    # Implement logic to stop the Ansible task if applicable
    return jsonify({
        'status': 'success',
        'message': 'Ansible execution stopped.'
    })

if __name__ == '__main__':
    app.run(host='192.168.178.34', port=8080)
