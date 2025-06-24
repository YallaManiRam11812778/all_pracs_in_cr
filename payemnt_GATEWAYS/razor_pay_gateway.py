import razorpay

def razorpay_payment_by_users(amount):
	try:
		# Initialize Razorpay client
		client = razorpay.Client(auth=("rzp_test_W8q4CxN0D9JSGQ", "Y7hJSLn6MUgU9UG1SrsmAXH7"))
		payment_link = client.payment_link.create({
        "amount": amount,     # Amount in smallest currency unit (e.g., paise for INR)
        "currency": "INR",
        "description": "Payment for order",
        "customer": {
            "name": "Mani RAM",
            "email": "ramunavailable@gmail.com",
            "contact": "9381142840"
        },
        "notify": {
            "sms": True,
            "email": True
        }
		})

		return payment_link
	except Exception as e:
		(str(e))