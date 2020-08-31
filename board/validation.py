from django.db.models import Q

from .status import Status

class FormValidation:
	def __init__(self, form_data):
		self.username = form_data['username']
		self.email = form_data['email']
		self.phone = form_data['phone']
		self.password = form_data['password']
		self.retype_password = form_data['retype_password']

	def validate(self, user):
		status_response = self.validateEmailAndPhone()
		if status_response['status'] != Status.Success:
			return status_response

		status_response = self.validateRetypedPassword()
		if status_response['status'] != Status.Success:
			return status_response

		if self.username != '':
			status_response = self.validateUsername(user)
			if status_response['status'] != Status.Success:
				return status_response

		status_response = self.validateIfEmailExist(user)
		if status_response['status'] != Status.Success:
			return status_response

		status_response = self.validateIfPhoneExist(user)
		if status_response['status'] != Status.Success:
			return status_response

		return status_response

	def validateRetypedPassword(self):
		if self.password != self.retype_password:
			status = Status.MismatchedPassword
			message = 'Passwords are mismatched!'
		else:
			status = Status.Success
			message = 'Success'
		print("validateRetypedPassword: ", status)
		return self.buildValidationResponse(status, message)

	def validateEmailAndPhone(self):
		if not self.email:
			status = Status.EmptyEmail
			message = 'Must input email!'
		elif not self.phone:
			status = Status.EmptyPhone
			message = 'Must input phone!'
		else:
			status = Status.Success
			message = 'Success'
		return self.buildValidationResponse(status, message)

	def validateUsername(self, user):
		try:
			user_name = user.objects.get(Q(username = self.username))
			status = Status.UserNameAlreadyExists
			message = 'Username already exist!'
		except user.DoesNotExist:
			status = Status.Success
			message = 'Success'
		return self.buildValidationResponse(status, message)

	def validateIfEmailExist(self, user):
		try:
			registered_user = user.objects.get(Q(email = self.email))
			status = Status.EmailAlreadyExists
			message = 'Email already exist!'
		except user.DoesNotExist:
			status = Status.Success
			message = 'Success'
		return self.buildValidationResponse(status, message)

	def validateIfPhoneExist(self, user):
		try:
			registered_user = user.objects.get(Q(phone = self.phone))
			status = Status.PhoneAlreadyExists
			message = 'Phone already exist!'
		except user.DoesNotExist:
			status = Status.Success
			message = 'Success'
		return self.buildValidationResponse(status, message)

	def buildValidationResponse(self, status, message):
		return {
			'status' : status,
			'message' : message,
		}
