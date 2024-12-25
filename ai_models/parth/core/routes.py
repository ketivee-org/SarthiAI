@app.route('/')
def home():
    return "Welcome to ParthAI Remote Control API!"

@app.route('/favicon.ico')
def favicon():
    return '', 204  # Return an empty response for favicon
