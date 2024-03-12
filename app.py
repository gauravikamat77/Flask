import webview
import threading
from flask import Flask, render_template,request
from tkinter_script import tkinter_function

app = Flask(__name__)

# Serve HTML file
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/Module')
def Module():
    return render_template('Module.html')

@app.route('/learn')
def learn():
    return render_template('learn.html')

@app.route('/MixingColors')
def MixingColors():
    return render_template('MixingColors.html')

@app.route('/run_tkinter', methods=['POST'])
def run_tkinter():
    # Call the tkinter_function to get the function that creates and runs the tkinter application
    run_tkinter_app = tkinter_function()
    # Execute the function to create and run the tkinter application
    run_tkinter_app()
    return 'Tkinter functionality executed.'

def run_flask():
    app.run()

if __name__ == '__main__':
    # Start Flask app in a separate thread
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()

    # Create desktop window
    webview.create_window("Desktop App", "http://127.0.0.1:5000")

    # Run desktop app
    webview.start()