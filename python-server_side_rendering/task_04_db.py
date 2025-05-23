# task_04_db.py
from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def load_from_sql(product_id=None):
    try:
        conn = sqlite3.connect('products.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        if product_id:
            cursor.execute("SELECT * FROM Products WHERE id = ?", (product_id,))
        else:
            cursor.execute("SELECT * FROM Products")
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows]
    except Exception as e:
        return {"error": f"Database error: {e}"}

@app.route('/products')
def products():
    source = request.args.get('source', 'sql')
    product_id = request.args.get('id')

    try:
        product_id = int(product_id) if product_id else None
    except ValueError:
        return render_template('product_display.html', products=[], error="Invalid ID format")

    if source == 'sql':
        data = load_from_sql(product_id)
    else:
        return render_template('product_display.html', products=[], error="Wrong source")

    if isinstance(data, dict) and "error" in data:
        return render_template('product_display.html', products=[], error=data["error"])

    return render_template('product_display.html', products=data)

if __name__ == '__main__':
    app.run(debug=True)

