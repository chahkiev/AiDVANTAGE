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


class Question(models.Model):
    Doctor = models.CharField(max_length=128, blank=True, null=True, default=None)
    Datetime = models.IntegerField(default=0, null=False)
    FIO = models.CharField(max_length=128, blank=True, null=True, default=None)
    Acception = models.BooleanField(default=False)
    q0  = models.CharField(max_length=128, blank=True, null=True, default=None)
    q1  = models.CharField(max_length=128, blank=True, null=True, default=None)
    q2  = models.CharField(max_length=128, blank=True, null=True, default=None)
    q3  = models.CharField(max_length=128, blank=True, null=True, default=None)
    q4  = models.CharField(max_length=128, blank=True, null=True, default=None)
    q5  = models.CharField(max_length=128, blank=True, null=True, default=None)
    q6  = models.CharField(max_length=128, blank=True, null=True, default=None)
    q7  = models.CharField(max_length=128, blank=True, null=True, default=None)
    q8  = models.CharField(max_length=128, blank=True, null=True, default=None)
    q9  = models.CharField(max_length=128, blank=True, null=True, default=None)
    q10 = models.CharField(max_length=128, blank=True, null=True, default=None)
    q11 = models.CharField(max_length=128, blank=True, null=True, default=None)
    q12 = models.CharField(max_length=128, blank=True, null=True, default=None)
    q13 = models.CharField(max_length=128, blank=True, null=True, default=None)
    q14 = models.CharField(max_length=128, blank=True, null=True, default=None)
    q15 = models.CharField(max_length=128, blank=True, null=True, default=None)
    q16 = models.CharField(max_length=128, blank=True, null=True, default=None)
    q17 = models.CharField(max_length=128, blank=True, null=True, default=None)
    q18 = models.CharField(max_length=128, blank=True, null=True, default=None)
    q19 = models.CharField(max_length=128, blank=True, null=True, default=None)
    q20 = models.CharField(max_length=128, blank=True, null=True, default=None)
    q21 = models.CharField(max_length=128, blank=True, null=True, default=None)
    q22 = models.CharField(max_length=128, blank=True, null=True, default=None)
    q23 = models.CharField(max_length=128, blank=True, null=True, default=None)
    q24 = models.CharField(max_length=128, blank=True, null=True, default=None)
    q25 = models.CharField(max_length=128, blank=True, null=True, default=None)
    q26 = models.CharField(max_length=128, blank=True, null=True, default=None)
    q27 = models.CharField(max_length=128, blank=True, null=True, default=None)
    q28 = models.CharField(max_length=128, blank=True, null=True, default=None)
    q29 = models.CharField(max_length=128, blank=True, null=True, default=None)
    q30 = models.CharField(max_length=128, blank=True, null=True, default=None)
    q31 = models.CharField(max_length=128, blank=True, null=True, default=None)
    q32 = models.CharField(max_length=128, blank=True, null=True, default=None)