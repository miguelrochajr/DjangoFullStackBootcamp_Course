from django.contrib import admin
from groups import models
# Register your models here.

class GroupMemberInLine(admin.TabularInline):
    model = models.GroupMember
