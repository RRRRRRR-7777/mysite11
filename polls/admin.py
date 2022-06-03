from django.contrib import admin
from django.urls import path
from .models import Question, Choice
from django.template.response import TemplateResponse

admin.site.site_header = "Dajango カスタムサイト"

admin.site.register(Choice)

@admin.register(Question)

class QuestionAdmin(admin.ModelAdmin):
    actions = ["change_title_action"]
    list_display_links = None

    def change_title_action(self, request, queryset):
        queryset.update(question_text='other')
    change_title_action.short_description = 'テキストをotherに変換する'

    def get_urls(self):
        urls = super().get_urls()
        add_urls = [
            path('new_page/', self.admin_site.admin_view(self.add_view), name="new_page"),
            ]
        return add_urls + urls

    def add_view(self, request):
        return TemplateResponse(request, "admin/polls/question/new_page.html")