
from flask import Flask, render_template, request, redirect, url_for
from crud_operations import *
from db_config import get_db_connection

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a more secure key

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Example of other routes for tours, bookings, etc.
@app.route('/tours')
def view_tours():
    tours = get_all_tours()  # Function to fetch all tours from database
    return render_template('tours.html', tours=tours)

@app.route('/book', methods=['GET', 'POST'])
def book_tour():
    if request.method == 'POST':
        tour_id = request.form['tour_id']
        customer_name = request.form['customer_name']
        customer_email = request.form['customer_email']
        booking_date = request.form['booking_date']

        # Insert booking into the database
        if book_tour_in_db(tour_id, customer_name, customer_email, booking_date):
            flash("Booking successful!")
        else:
            flash("Booking failed. Please try again.")
        return redirect(url_for('view_tours'))

    return render_template('book.html')

# Error handling
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
