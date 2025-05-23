#!/usr/bin/env python3
from flask import Flask, render_template, request
import json
import csv
import sqlite3
import os

app = Flask(__name__)

def load_from_json():
    try:
        with open('products.json') as f:
            return json.load(f)
    except Exception as e:
        return {"error": f"JSON error: {e}"}

def load_from_csv():
    try:
        with open('products.csv', newline='') as f:
            reader = csv.DictReader(f)
            return [row for row in reader]
    except Exception as e:
        return {"error": f"CSV error: {e}"}

def load_from_sql():
    try:
        conn = sqlite3.connect('products.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Products")
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows]
    except Exception as e:
        return {"error": f"Database error: {e}"}

@app.route('/products')
def products():
    source = request.args.get('source', 'json')
    
    if source == 'json':
        data = load_from_json()
    elif source == 'csv':
        data = load_from_csv()
    elif source == 'sql':
        data = load_from_sql()
    else:
        return render_template('product_display.html', products=[], error="Wrong source")
    
    # Check if data returned an error
    if isinstance(data, dict) and "error" in data:
        return render_template('product_display.html', products=[], error=data["error"])
    
    return render_template('product_display.html', products=data, error=None)

if __name__ == '__main__':
    app.run(debug=True)

