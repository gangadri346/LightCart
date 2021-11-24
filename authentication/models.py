import base64

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError
from django.core.files.base import ContentFile

from LightCart.models import BaseModel


class User(BaseModel, AbstractUser):
    verification_code = models.IntegerField(null=True, default=None)
    verification_code_time = models.DateTimeField(null=True, default=None)
    forgot_pin_code = models.CharField(max_length=4, null=True, default=None)
    num_ver_tries = models.IntegerField(default=0)
    is_mobile_verified = models.BooleanField(default=False)
    is_email_verified = models.BooleanField(default=False)
    profile_status = models.BooleanField(default=False)
    change_password = models.BooleanField(default=True)
    phone_number = models.CharField(max_length=15, blank=True, default="")
    title = models.CharField(max_length=256, null=True, default=None)
    photo = models.ImageField(null=True, default=None, upload_to="user_image")
    customer_type = models.CharField(max_length=20,null=True)

    def upload_image(self, user, image_details):
        try:
            # Image data
            data = None
            if image_details and type(image_details) == dict:
                # Process image.
                encoded_file = image_details.get("base_64")
                file_name = image_details.get("filename")

                decoded_file = base64.b64decode(encoded_file)
                data = ContentFile(decoded_file, name=file_name)

                self.photo = data
                self.save()
                return {
                    "image": ("success"),
                    "message": ("image uploaded successfully."),
                }
        except Exception as exp:
            raise ValidationError(exp)


# class Login(models.Model):
#     pass


class UserAddress(BaseModel):
    user_id = models.ForeignKey("authentication.User", on_delete=models.DO_NOTHING)
    permanent_address = models.TextField(null=False)
    temporary_address =models.TextField(null=True)
    city = models.CharField(max_length=100,null=True,default=None)
    pin_code = models.IntegerField(default=0)
    country = models.CharField(default=None,max_length=30)
    mobile_number = models.BigIntegerField(default=0,null=True)








# Create your models here.
