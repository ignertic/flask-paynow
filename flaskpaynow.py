from payynow import payynow
from flask import current_app, _app_ctx_stack

class Paynow(object):
	"""docstring for Paynow"""

paynow = Paynow(
    'INTEGRATION_ID', 
    'INTEGRATION_KEY',
    'http://google.com', 
    'http://google.com'
    )

	def __init__(self, app=None):
		self.app = app
		if self is not None:
			self.init__app (app)

	def payment():
		paynow.create_payment('Order #100', 'test@example.com')

		payment.add('Bananas', 2.50)
		payment.add('Apples', 3.40)

		# Save the response from paynow in a variable
		response = paynow.send(payment)