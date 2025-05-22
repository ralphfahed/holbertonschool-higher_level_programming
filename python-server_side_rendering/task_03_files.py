from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json():
    try:
        with open('products.json') as f:
            return json.load(f)
    except Exception:
        return []

def read_csv():
    try:
        with open('products.csv') as f:
            reader = csv.DictReader(f)
            return [dict(id=int(row['id']), name=row['name'], category=row['category'], price=float(row['price'])) for row in reader]
    except Exception:
        return []

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    error = None
    data = []

    if source == 'json':
        data = read_json()
    elif source == 'csv':
        data = read_csv()
    else:
        error = "Wrong source"
        return render_template('product_display.html', error=error)

    if product_id:
        try:
            product_id = int(product_id)
            data = [item for item in data if item['id'] == product_id]
            if not data:
                error = "Product not found"
        except ValueError:
            error = "Invalid ID"

    return render_template('product_display.html', products=data, error=error)

