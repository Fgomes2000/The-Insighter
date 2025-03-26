from app import app
from flask import render_template, request, redirect, url_for
from app.models import User, Customer, Product, SalesTransaction, db

@app.route('/')
def index():
    return "Welcome to The Insighter Dashboard"

@app.route('/users')
def show_users():
    users = User.query.all()
    return render_template('users.html', users=users)

@app.route('/customers')
def show_customers():
    customers = Customer.query.all()
    return render_template('customers.html', customers=customers)

@app.route('/products')
def show_products():
    products = Product.query.all()
    return render_template('products.html', products=products)

@app.route('/sales')
def show_sales():
    sales = SalesTransaction.query.all()
    return render_template('sales.html', sales=sales)

@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        new_user = User(username=request.form['username'],
                        email=request.form['email'],
                        password=request.form['password'],
                        role=request.form['role'])
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('show_users'))
    return render_template('add_user.html')

@app.route('/add_customer', methods=['GET', 'POST'])
def add_customer():
    if request.method == 'POST':
        new_customer = Customer(name=request.form['name'],
                                email=request.form['email'],
                                phone=request.form['phone'])
        db.session.add(new_customer)
        db.session.commit()
        return redirect(url_for('show_customers'))
    return render_template('add_customer.html')

@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        new_product = Product(name=request.form['name'],
                              description=request.form['description'],
                              price=float(request.form['price']),
                              cost=float(request.form['cost']),
                              category=request.form['category'])
        db.session.add(new_product)
        db.session.commit()
        return redirect(url_for('show_products'))
    return render_template('add_product.html')

@app.route('/add_sale', methods=['GET', 'POST'])
def add_sale():
    if request.method == 'POST':
        new_sale = SalesTransaction(customer_id=int(request.form['customer_id']),
                                    product_id=int(request.form['product_id']),
                                    quantity=int(request.form['quantity']),
                                    price=float(request.form['price']),
                                    discount=float(request.form['discount']))
        db.session.add(new_sale)
        db.session.commit()
        return redirect(url_for('show_sales'))
    customers = Customer.query.all()
    products = Product.query.all()
    return render_template('add_sale.html', customers=customers, products=products)