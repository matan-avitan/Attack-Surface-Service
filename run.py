from app import create_app
import json

with open('input-3.json') as f:
    inputs = json.load(f)

if __name__ == '__main__':
    app = create_app(inputs)
    app.run(debug=True, port=80)
