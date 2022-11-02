from flask import render_template
from app import app
from models.order_list import *


@app.route('/orders')
def index():
    return render_template('order.html', title='order', list_of_orders = list_of_orders)

@app.route('/orders/<index>')
def single_order(index):
    chosen_order = list_of_orders[int(index)]
    return render_template('order_1.html', title='order', order=chosen_order)
