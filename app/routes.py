from app import app


@app.route('/')
def indec():
    return "Hello, World!"
