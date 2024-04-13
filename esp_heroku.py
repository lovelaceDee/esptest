from flask import Flask, request

app = Flask(__name__)

# Route to receive LED control commands
@app.route('/control_led', methods=['POST'])
def control_led():
    # Get the LED state from the request data
    led_state = request.json.get('led_state')

    # Logic to control the LED
    if led_state == 'on':
        # Turn on the LED
        # Code to handle LED control goes here
        response_message = 'LED turned on'
    elif led_state == 'off':
        # Turn off the LED
        # Code to handle LED control goes here
        response_message = 'LED turned off'
    else:
        response_message = 'Invalid LED state'

    return response_message

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask app
