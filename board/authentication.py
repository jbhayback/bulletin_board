from django.db.models import Q

from .status import Status

class CustomAuthentication:
	def authenticate(self, user_data, user):
		try:
			registered_user = user.objects.get(
				Q(email = user_data['email_or_phone']) | Q(phone = user_data['email_or_phone']))
			if registered_user.check_password(user_data['password']) and registered_user.is_active:
				status = Status.Success
				message = 'Success!'
			else:
				status = Status.InvalidPassword
				message = 'Invalid password entered!'
		except user.DoesNotExist:
			status = Status.UserDoesNotExists
			message = 'User does not exist!'
		return self.buildAuthenticationResponse(status, message)

	def buildAuthenticationResponse(self, status, message):
		return {
			'status' : status,
			'message' : message,
			}
