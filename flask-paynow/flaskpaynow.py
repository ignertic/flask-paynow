from paynow import Paynow
from flask import current_app, _app_ctx_stack
from model import Model

		
class Paynow(Model):
	"""docstring for Paynow"""

paynow = Paynow(
    'INTEGRATION_ID', 
    'INTEGRATION_KEY',
    'http://google.com', 
    'http://google.com'
    ) #Refactor to load from config

	def __init__(self, app=None):
		self.app = app
		super(Paynow, self).__init__()
		if self is not None:
			self.init__app (app)


	def payment(self):
		paynow.create_payment('Order #100', 'test@example.com') #TODO://Refactor

		payment.add('Bananas', 2.50) 
		payment.add('Apples', 3.40)

		# Save the response from paynow in a variable
		response = paynow.send(payment)

		#TODO: Add methods 31/12/18