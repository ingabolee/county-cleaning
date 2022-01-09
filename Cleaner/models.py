from django.db import models
from django.core.validators import RegexValidator
import crispy_forms

from django.contrib.auth.models import (
		BaseUserManager, AbstractBaseUser
	)

# Create your models here.

class Employer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    _id = models.IntegerField(primary_key=True)
    date_of_birth = models.DateField()
    nationality = models.CharField(max_length=30)

    

class Equipment(models.Model):
    equipment_name = models.CharField(max_length=20)
    equipment_id = models.IntegerField(primary_key=True)
    date_of_purchase = models.DateField()


class Location(models.Model):
    location_name = models.CharField(max_length=30)
    location_id = models.IntegerField(primary_key=True)


class CountyDetails(models.Model):
    county_name = models.CharField(max_length=30)
    county_id = models.IntegerField(primary_key=True)


from django.core.validators import RegexValidator

from django.contrib.auth.models import (
		BaseUserManager, AbstractBaseUser
	)

USERNAME_REGEX = '^[a-zA-Z0-9.+-]*$'


class MyUserManager(BaseUserManager):
	def create_user(self, username, email, password=None):
		if not email:
			raise ValueError('Users must have an email address')

		user = self.model(
					username = username,
					email = self.normalize_email(email)
				)
		user.set_password(password)
		user.save(using=self._db)
		return user
		# user.password = password # bad - do not do this

	def create_superuser(self, username, email, password=None):
		user = self.create_user(
				username, email, password=password
			)
		user.is_admin = True
		user.is_staff = False
		user.save(using=self._db)
		return user 



class MyUser(AbstractBaseUser):
	username = models.CharField(
					max_length=300,
					validators = [
						RegexValidator(regex = USERNAME_REGEX,
										message='Username must be alphanumeric or contain numbers',
										code='invalid_username'
							)],
					unique=True
				)
	email = models.EmailField(
			max_length=255,
			unique=True,
			verbose_name='email address'
		)
	is_admin = models.BooleanField(default=False)
	is_staff = models.BooleanField(default=False)
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	job = models.CharField(max_length=30)
	_id = models.IntegerField(primary_key=True)
	date_of_birth = models.DateField()
	nationality = models.CharField(max_length=30)
	employer = models.ManyToManyField(Employer)

	objects = MyUserManager()

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email']

	def __str__(self):
		return self.email

	def get_short_name(self):
		# The user is identified by their email address
		return self.email


	def has_perm(self, perm, obj=None):
		"Does the user have a specific permission?"
		# Simplest possible answer: Yes, always
		return True

	def has_module_perms(self, app_label):
		"Does the user have permissions to view the app `app_label`?"
		# Simplest possible answer: Yes, always
		return True

class PaymentDetails(models.Model):
    payment_id = models.CharField(max_length=30, primary_key=True)
    amount = models.IntegerField()
    payment_method = models.CharField(max_length=30)
    sender = models.ForeignKey(Employer, on_delete=True)
    receiver = models.ForeignKey(MyUser, on_delete=True)





