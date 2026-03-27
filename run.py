from app import create_app
import os

app = create_app()

if __name__ == '__main__':
    debug = os.environ.get('DEBUG_VAL', 'False') == 'True' # reads the env variable and compare the result to the string 'True'
    app.run(debug=debug)