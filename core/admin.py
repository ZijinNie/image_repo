from django.contrib import admin
from core.models import *


# # Register your models here.
# class TeamInline(admin.StackedInline):
#     model = Team


# class SiteAdmin(admin.ModelAdmin):
#     list_display = ('name', 'keywords', 'description')
#     inlines = [TeamInline]


# class NotificationAdmin(admin.ModelAdmin):
#     list_display = ('content', 'created_at')


# class ReportAdmin(admin.ModelAdmin):
#     list_display = ('reason', 'time_send')


# class FeedbackAdmin(admin.ModelAdmin):
#     list_display = ('subject', 'email', 'pub_time', 'status')


# class FAQAdmin(admin.ModelAdmin):
#     list_display = ('title', 'slug')
#     prepopulated_fields = {'slug': ('title',)}


# admin.site.register(Site, SiteAdmin)
# admin.site.register(Notification, NotificationAdmin)
# admin.site.register(Report, ReportAdmin)
# admin.site.register(Feedback, FeedbackAdmin)
# admin.site.register(FAQ, FAQAdmin)
