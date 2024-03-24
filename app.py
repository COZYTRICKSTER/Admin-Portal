from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import database

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():
    # Handle login logic here
    username = request.form.get("username")
    password = request.form.get("password")

    # Connect to SQLite database
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    # Query the database for the user with the provided username
    cursor.execute("SELECT * FROM users WHERE username=?", (username,))
    user = cursor.fetchone()

    if user:
        if password == user[2]:
            return redirect(url_for("admin_portal"))

    # If credentials are invalid, render login page with error message
    error = "Invalid credentials. Please try again."
    return render_template("login.html", error=error)


@app.route("/admin")
def admin_portal():
    # Render the admin portal page
    return render_template("admin_portal.html")


@app.route("/admin/customer_list")
def customer_list():
    data = database.getCustomers()
    customers = []

    for d in data:
        entry = {
            "id": d[0],
            "name": d[1],
            "phone": d[2],
            "email": d[3],
            "address": d[4],
        }

        customers.append(entry)

    return render_template("customer_list.html", customers=customers)


@app.route("/admin/invoice_list")
def invoice_list():
    data = database.getInvoices()
    invoices = []

    for d in data:
        entry = {
            "id": d[0],
            "name": d[1],
            "date": d[2],
            "amount": d[3],
            "status": d[4],
        }

        invoices.append(entry)

    return render_template("invoice_list.html", invoices=invoices)


@app.route("/customer_create", methods=["GET", "POST"])
def create_customer():
    if request.method == "POST":
        # Handle form submission to create new customer
        name = request.form.get("name")
        phone = request.form.get("phone")
        email = request.form.get("email")
        address = request.form.get("address")

        database.add_customer(name, phone, email, address)

        # After adding customer, redirect to customer list page
        return redirect(url_for("customer_list"))

    # Render the customer creation form
    return render_template("customer_create.html")


@app.route("/customer_edit/<int:id>", methods=["GET", "POST"])
def edit_customer(id):
    if request.method == "POST":
        # Handle form submission to edit customer
        name = request.form.get("name")
        phone = request.form.get("phone")
        email = request.form.get("email")
        address = request.form.get("address")

        database.edit_customer(id, name, phone, email, address)

        # After editing customer, redirect to customer list page
        return redirect(url_for("customer_list"))

    d = database.getCustomerById(id)
    customer = {
        "id": d[0],
        "name": d[1],
        "phone": d[2],
        "email": d[3],
        "address": d[4],
    }

    # Render the customer edit form with pre-filled data
    return render_template("customer_edit.html", customer=customer)


@app.route("/invoice_create", methods=["GET", "POST"])
def create_invoice():
    if request.method == "POST":
        # Handle form submission to create new invoice
        name = request.form.get("customer")
        date = request.form.get("date")
        amount = request.form.get("amount")
        status = request.form.get("status")

        database.add_invoice(name, date, amount, status)

        # After adding invoice, redirect to invoice list page
        return redirect(url_for("invoice_list"))

    data = database.getCustomers()
    customers = []

    for d in data:
        entry = {
            "id": d[0],
            "name": d[1],
            "phone": d[2],
            "email": d[3],
            "address": d[4],
        }

        customers.append(entry)

    # Render the invoice creation form
    return render_template("invoice_create.html", customers=customers)


@app.route("/invoice_edit/<int:id>", methods=["GET", "POST"])
def edit_invoice(id):
    if request.method == "POST":
        # Handle form submission to edit invoice
        name = request.form.get("customer_id")
        date = request.form.get("date")
        amount = request.form.get("amount")
        status = request.form.get("status")

        database.edit_invoice(id, name, date, amount, status)

        # After editing invoice, redirect to invoice list page
        return redirect(url_for("invoice_list"))

    d = database.getInvoiceById(id)
    invoice = {
        "id": d[0],
        "name": d[1],
        "date": d[2],
        "amount": d[3],
        "status": d[4],
    }

    # Render the invoice edit form with pre-filled data
    return render_template("invoice_edit.html", invoice=invoice)


if __name__ == "__main__":
    app.run(debug=True)
