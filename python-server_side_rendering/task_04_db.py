from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/items')
def items():
    try:
        with open('items.json') as f:
            data = json.load(f)
            items = data.get("items", [])
    except FileNotFoundError:
        items = []
    return render_template('items.html', items=items)


def read_json_file(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)


def read_csv_file(filepath):
    products = []
    with open(filepath, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products


def read_sqlite_database():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, category, price FROM Products")
    rows = cursor.fetchall()
    conn.close()
    products = [{'id': row[0], 'name': row[1],
                 'category': row[2], 'price': row[3]} for row in rows]
    return products


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)

    if source == 'json':
        products = read_json_file('products.json')
    elif source == 'csv':
        products = read_csv_file('products.csv')
    elif source == 'sql':
        try:
            products = read_sqlite_database()
        except sqlite3.Error as e:
            return render_template(
                'product_display.html',
                error=f"Database error: {str(e)}")
    else:
        return render_template('product_display.html', error="Wrong source")

    if product_id is not None:
        products = [
            product for product in products if product['id'] == product_id]
        if not products:
            return render_template(
                'product_display.html',
                error="Product not found")

    return render_template('product_display.html', products=products)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
