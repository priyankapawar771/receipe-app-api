from django.db import models
# from django.contrib.auth.models import {AbstractBaseUser,
#                                         BaseUserManager,
#                                         PermissionMixin,
#                                         }

# # Create your models here.
# class UserManager(BaseUserManager):
#         def create_user(self, email, password, **extra_field):
#                 user = self.model(email = email, **extra_field)
#                 user.set_password(password)
#                 user.save(using = self._db)
#                 return user



# class User(AbstractBaseUser, PermissionMixin):
#         email = models.EmailField(max_length = 300, unique = True)
#         name = models.CharField(max_length=300)
#         is_active = models.BooleanField(default = True)
#         is_staff = models.BooleanField(default = True)

#         object = UserManager()

#         USERNAME_FIELD = 'email'

class User(models.Model):
        name = models.CharField(max_length = 250)
        email = models.EmailField(max_length= 250)

class Receipe(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
        title = models.CharField(max_length = 250)
        description = models.TextField(blank = True)
        time_minutes = models.IntegerField()
        price = models.DecimalField(max_digits = 5, DecimalField = 2)
        link = models.CharField(max_length = 255, blank = True)

        def __str__(self):
                return self.title

