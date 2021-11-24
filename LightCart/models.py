from django.db import models



class BaseModel(models.Model):
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Notifications(BaseModel):
    user_id = models.ForeignKey("authentication.User", on_delete=models.DO_NOTHING)
    message = models.TextField(default=None,null=True)
    delivery_datetime = models.DateTimeField(default=None)