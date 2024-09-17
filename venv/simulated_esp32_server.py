from flask import Flask

app = Flask(__name__)

@app.route('/')
def root():
    return "ESP32 Irrigation System"

@app.route('/on')
def on():
    global relay_status
    relay_status = True
    print("Relay is ON")
    return "Relay is ON"

@app.route('/off')
def off():
    global relay_status
    relay_status = False
    print("Relay is OFF")
    return "Relay is OFF"

@app.route('/status')
def get_status():
    global relau_status
    return {"relay_status": relay_status}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
