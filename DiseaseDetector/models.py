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
    patient = models.ForeignKey(User, verbose_name="Patient", on_delete=models.CASCADE)
    q1 = models.IntegerField(default=-1)
    q2 = models.IntegerField(default=-1)
    q3 = models.IntegerField(default=-1)
    q4 = models.IntegerField(default=-1)
    q5 = models.IntegerField(default=-1)
    q6 = models.IntegerField(default=-1)
    q7 = models.IntegerField(default=-1)
    q8 = models.IntegerField(default=-1)
    q9 = models.IntegerField(default=-1)
    q10 = models.IntegerField(default=-1)
    q11 = models.IntegerField(default=-1)
    q12 = models.IntegerField(default=-1)
    q13 = models.IntegerField(default=-1)
    q14 = models.IntegerField(default=-1)
    q15 = models.IntegerField(default=-1)
    q16 = models.IntegerField(default=-1)
    q17 = models.IntegerField(default=-1)
    q18 = models.IntegerField(default=-1)
    q19 = models.IntegerField(default=-1)
    q20 = models.IntegerField(default=-1)
    q21 = models.IntegerField(default=-1)
    q22 = models.IntegerField(default=-1)
    q23 = models.IntegerField(default=-1)
    q24 = models.IntegerField(default=-1)
    q25 = models.IntegerField(default=-1)
    q26 = models.IntegerField(default=-1)
    q27 = models.IntegerField(default=-1)
    q28 = models.IntegerField(default=-1)
    q29 = models.IntegerField(default=-1)
    q30 = models.IntegerField(default=-1)
    q31 = models.IntegerField(default=-1)
    q32 = models.IntegerField(default=-1)
