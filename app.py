from paynow import Paynow
from flask import Flask, redirect, render_template, request

app = Flask(__name__)

paynow = Paynow("INTEGRATION_ID", "INTEGRATION_KEY", 'http://return.url', 'http://result.url')

@app.route('/start_payment', methods=['POST'])
def start_payment():
	data = dict(request.form)
	# create payment
	payment = paynow.create_payment('Client Name', data['email'])
	# add item to cart
	payment.add('Product', float(data['amount']))
	# initiate payment
	response = paynow.send(payment)
	# redirect to payment page
	return redirect(response.redirect_url)

@app.route('/')
def main():
	return render_template('index.html')

if __name__ == '__main__':
	app.run()