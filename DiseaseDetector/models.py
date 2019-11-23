from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
import os
from django.db.models.signals import post_save
from django.dispatch import receiver
# from PIL import Image, ExifTags

# from question.managers import UserManager, TagManager, QuestionManager, AnswerManager, LikeDislikeQuestionManager


# AUTH_USER_MODEL set in settings
class User(AbstractUser):
    # upload = models.ImageField(default="static/default/default_avatar.png", upload_to="media/uploads/%Y/%m/%d", verbose_name="User's Avatar")
    # registration_date = models.DateTimeField(default=timezone.now, verbose_name="User's Registration Date")
    # rating = models.IntegerField(default=0, verbose_name="User's Rating")
    first_name = models.CharField(max_length=64, blank=True, null=True, default=None)
    last_name = models.CharField(max_length=64, blank=True, null=True, default=None)
    # objects = UserManager()

    def __str__(self):
        return self.username


