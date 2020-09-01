from django.test import TestCase
from django.contrib.auth import get_user_model

from selenium import webdriver

class LoginFunctionalTestCase(TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def test_there_is_login_page(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Sign in', self.browser.page_source)

    def test_login_successfully(self):
        self.browser.get('http://localhost:8000')
        email_or_phone = self.browser.find_element_by_name('email_or_phone')
        password = self.browser.find_element_by_name('password')
        submit = self.browser.find_element_by_id('id_signin_button')
        email_or_phone.send_keys('123')
        password.send_keys('1234')
        submit.click()
        self.assertIn('Home', self.browser.page_source)

    def test_login_error_when_no_username(self):
        self.browser.get('http://localhost:8000')
        password = self.browser.find_element_by_name('password')
        submit = self.browser.find_element_by_id('id_signin_button')
        password.send_keys('1234')
        submit.click()
        self.assertIn('Error', self.browser.page_source)

    def test_login_error_when_no_password(self):
        self.browser.get('http://localhost:8000')
        email_or_phone = self.browser.find_element_by_name('email_or_phone')
        submit = self.browser.find_element_by_id('id_signin_button')
        email_or_phone.send_keys('123')
        submit.click()
        self.assertIn('Error', self.browser.page_source)

    def tearDown(self):
        self.browser.quit()

class RegistrationFunctionalTestCase(TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def test_there_is_registration_page(self):
        self.browser.get('http://localhost:8000/registration')
        self.assertIn('Register', self.browser.page_source)

    def test_register_successfully(self):
        self.browser.get('http://localhost:8000/registration')
        username = self.browser.find_element_by_name('username')
        email = self.browser.find_element_by_name('email')
        phone = self.browser.find_element_by_name('phone_number')
        password = self.browser.find_element_by_name('password')
        retype_password = self.browser.find_element_by_name('retype_password')
        submit = self.browser.find_element_by_id('id_register_button')

        username.send_keys('damaris')
        email.send_keys('damaris@gmail.com')
        phone.send_keys('4321')
        password.send_keys('1234')
        retype_password.send_keys('1234')
        submit.click()
        self.assertIn('HELLO damaris', self.browser.page_source)

    def test_register_successfully_even_no_username(self):
        self.browser.get('http://localhost:8000/registration')
        email = self.browser.find_element_by_name('email')
        phone = self.browser.find_element_by_name('phone_number')
        password = self.browser.find_element_by_name('password')
        retype_password = self.browser.find_element_by_name('retype_password')
        submit = self.browser.find_element_by_id('id_register_button')

        email.send_keys('damaris1@gmail.com')
        phone.send_keys('43210')
        password.send_keys('1234')
        retype_password.send_keys('1234')
        submit.click()
        self.assertIn('HELLO', self.browser.page_source)

    def test_register_error_when_no_email(self):
        self.browser.get('http://localhost:8000/registration')
        email = self.browser.find_element_by_name('email')
        phone = self.browser.find_element_by_name('phone_number')
        password = self.browser.find_element_by_name('password')
        retype_password = self.browser.find_element_by_name('retype_password')
        submit = self.browser.find_element_by_id('id_register_button')

        phone.send_keys('4321')
        password.send_keys('1234')
        retype_password.send_keys('1234')
        submit.click()
        self.assertIn('Must input email!', self.browser.page_source)

    def test_register_error_when_no_phone(self):
        self.browser.get('http://localhost:8000/registration')
        email = self.browser.find_element_by_name('email')
        phone = self.browser.find_element_by_name('phone_number')
        password = self.browser.find_element_by_name('password')
        retype_password = self.browser.find_element_by_name('retype_password')
        submit = self.browser.find_element_by_id('id_register_button')

        email.send_keys('damaris@gmail.com')
        password.send_keys('1234')
        retype_password.send_keys('1234')
        submit.click()
        self.assertIn('Must input phone!', self.browser.page_source)

    def test_register_error_when_mismatched_password(self):
        self.browser.get('http://localhost:8000/registration')
        email = self.browser.find_element_by_name('email')
        phone = self.browser.find_element_by_name('phone_number')
        password = self.browser.find_element_by_name('password')
        retype_password = self.browser.find_element_by_name('retype_password')
        submit = self.browser.find_element_by_id('id_register_button')

        email.send_keys('damaris@gmail.com')
        phone.send_keys('4321')
        password.send_keys('1243')
        retype_password.send_keys('1234')
        submit.click()
        self.assertIn('Passwords are mismatched!', self.browser.page_source)

    def tearDown(self):
        self.browser.quit()

# class UsersManagersTests(TestCase):

#     def test_create_user(self):
#         User = get_user_model()
#         user = User.objects.create_user(email='normal@user.com', password='foo')
#         self.assertEqual(user.email, 'normal@user.com')
#         self.assertTrue(user.is_active)
#         self.assertFalse(user.is_staff)
#         self.assertFalse(user.is_superuser)
#         try:
#             # username is None for the AbstractUser option
#             # username does not exist for the AbstractBaseUser option
#             self.assertIsNone(user.username)
#         except AttributeError:
#             pass
#         with self.assertRaises(TypeError):
#             User.objects.create_user()
#         with self.assertRaises(TypeError):
#             User.objects.create_user(email='')
#         with self.assertRaises(ValueError):
#             User.objects.create_user(email='', password="foo")

#     def test_create_superuser(self):
#         User = get_user_model()
#         admin_user = User.objects.create_superuser('super@user.com', 'foo')
#         self.assertEqual(admin_user.email, 'super@user.com')
#         self.assertTrue(admin_user.is_active)
#         self.assertTrue(admin_user.is_staff)
#         self.assertTrue(admin_user.is_superuser)
#         try:
#             # username is None for the AbstractUser option
#             # username does not exist for the AbstractBaseUser option
#             self.assertIsNone(admin_user.username)
#         except AttributeError:
#             pass
#         with self.assertRaises(ValueError):
#             User.objects.create_superuser(
#                 email='super@user.com', password='foo', is_superuser=False)


