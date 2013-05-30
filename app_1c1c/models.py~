import datetime

from django.db import models
from django.utils import timezone

class Member(models.Model):
    mem_name = models.CharField(max_length=200)
    mem_surname = models.CharField(max_length=200)
    mem_email = models.EmailField(max_length=90)
    mem_phone = models.CharField(max_length=10)

    mem_crea_date = models.DateTimeField("account creation date")
    
    def __unicode__(self):
        return self.mem_name + " " + self.mem_surname

    def is_new_member(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.mem_crea_date <  now

    is_new_member.admin_order_field = 'mem_crea_date'
    is_new_member.boolean = True
    is_new_member.short_description = 'is a new member'

class Lesson(models.Model):
    les_name = models.CharField("lesson name", max_length=200)
    les_desc = models.CharField("lesson description", max_length=500)
    les_date = models.DateTimeField("lesson date")
    
    les_cook = models.ForeignKey(Member, related_name="cook teaching")
    les_students = models.ManyToManyField(Member, related_name="students attending")

    def __unicode__(self):
        return self.les_name