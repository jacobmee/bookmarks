from flask import Flask, render_template

# Initialize the Flask app
app = Flask(__name__)

# Define routes
@app.route('/')
def index():
    return render_template('index.html')

# Run the app
if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=80)  # Bind to 0.0.0.0 for external access