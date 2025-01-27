from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import json

# Initialize application and set secret key for session management
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# Color initialization (all LEDs off, or black)
colors = [[0, 0, 0] for _ in range(64)]

# Converts a HEX color to an RGB list
def hex_to_rgb_color(color: str):
    """Convert HEX to RGB."""
    color = color.lstrip('#')
    return [int(color[i:i + 2], 16) for i in (0, 2, 4)]

# Serve the main page
@app.route('/')
def index():
    """Render the main web page."""
    return render_template('Lab3-Colour-Picker.html')

# WebSocket event for new client connections
@socketio.on('connect')
def on_connect():
    """Send initial LED colors upon new client connection."""
    emit('current_colors', json.dumps({'colors': colors}))

# WebSocket event to update individual LED colors
@socketio.on('update_led')
def on_update_led(data):
    """Update LED color based on data from the client."""
    data = json.loads(data)
    id = int(data['id'])
    color = hex_to_rgb_color(data['color'])
    colors[id] = color
    emit('update_led', json.dumps({'id': data['id'], 'color': data['color']}), broadcast=True)

# WebSocket event to clear all LEDs
@socketio.on('clear_leds')
def on_clear_leds():
    """Clear all LEDs and broadcast update to all clients."""
    global colors
    colors = [[0, 0, 0] for _ in range(64)]  # Set all LEDs to black
    emit('clear_all', json.dumps({'colors': colors}), broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0", debug=True)
