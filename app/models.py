# app/models.py
from app import db
from datetime import datetime
import enum

class Role(enum.Enum):
    Admin = 'Admin'
    Manager = 'Manager'
    Analyst = 'Analyst'

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    role = db.Column(db.Enum(Role), nullable=False)
    last_login = db.Column(db.DateTime)
    login_attempts = db.Column(db.Integer, default=0)

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(15), unique=True, nullable=True)
    signup_date = db.Column(db.DateTime, default=datetime.utcnow)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=True)
    price = db.Column(db.Float, nullable=False)
    cost = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=True)

class SalesTransaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    discount = db.Column(db.Float, default=0.0)
    customer = db.relationship('Customer', backref=db.backref('sales', lazy=True))
    product = db.relationship('Product', backref=db.backref('sales', lazy=True))

class ReportType(enum.Enum):
    DailySales = 'DailySales'
    MonthlyTrends = 'MonthlyTrends'
    Custom = 'Custom'

class ReportFormat(enum.Enum):
    PDF = 'PDF'
    CSV = 'CSV'

class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    report_type = db.Column(db.Enum(ReportType), nullable=False)
    date_generated = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    format_type = db.Column(db.Enum(ReportFormat), nullable=False)
    data = db.Column(db.Text, nullable=True)
    user = db.relationship('User', backref=db.backref('reports', lazy=True))

class Dashboard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    layout = db.Column(db.Text, nullable=True)
    user = db.relationship('User', backref=db.backref('dashboards', lazy=True))

class Widget(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dashboard_id = db.Column(db.Integer, db.ForeignKey('dashboard.id'), nullable=False)
    widget_type = db.Column(db.String(100), nullable=False)
    configuration = db.Column(db.Text, nullable=True)
    dashboard = db.relationship('Dashboard', backref=db.backref('widgets', lazy=True))

class DataImport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    source_file = db.Column(db.String(255), nullable=False)
    import_date = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.Enum('Pending', 'Processing', 'Completed', 'Failed'), nullable=False)
    user = db.relationship('User', backref=db.backref('imports', lazy=True))

class Analysis(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    data = db.Column(db.Text, nullable=True)
    analysis_type = db.Column(db.Enum('TrendAnalysis', 'Forecasting'), nullable=False)
    results = db.Column(db.Text, nullable=True)
    user = db.relationship('User', backref=db.backref('analyses', lazy=True))

class Authentication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    last_login = db.Column(db.DateTime)
    login_attempts = db.Column(db.Integer, default=0)
    user = db.relationship('User', backref=db.backref('authentication', lazy=True))