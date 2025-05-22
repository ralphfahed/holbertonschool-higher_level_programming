from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/items')
def items():
    # Read the JSON file
    with open('items.json', 'r') as f:
        data = json.load(f)

    # Get the list of items (could be empty)
    items_list = data.get('items', [])

    # Pass items_list to the template
    return render_template('items.html', items=items_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

