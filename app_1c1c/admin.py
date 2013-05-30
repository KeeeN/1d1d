from django.contrib import admin
from app_1c1c.models import Member, Lesson

class LessonAdmin(admin.ModelAdmin):
    list_display = ('les_name', 'les_date', 'les_cook')

class MemberAdmin(admin.ModelAdmin):
    list_display = ('mem_name', 'mem_surname', 'mem_email', 'mem_phone', 'mem_crea_date', 'is_new_member')

admin.site.register(Member, MemberAdmin)
admin.site.register(Lesson, LessonAdmin)