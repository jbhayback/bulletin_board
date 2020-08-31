from enum import Enum

class Status(Enum):
	Success = 0
	MismatchedPassword = 1
	EmailAlreadyExists = 2
	PhoneAlreadyExists = 3
	EmptyEmail = 4
	EmptyPhone = 5
	UserNameAlreadyExists = 6
	UserDoesNotExists = 7
	InvalidPassword = 8
	EmptyEmailOrPhone = 9
