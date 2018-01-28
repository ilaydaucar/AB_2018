from django.contrib import admin
from election.models import Survey
from import_export import resources
from election.models import Survey
from import_export.admin import ImportExportModelAdmin
from election.models import Question

class SurveyResource(resources.ModelResource):
    class Meta:
        model = Survey
        fields = ('name', 'create_at', 'active',)

class SurveyAdmin(ImportExportModelAdmin):
    resources_class = SurveyResource
    list_display = ('name','active','created_at')
    list_filter = ('active',)
    search_fields = ('name','active')

admin.site.register(Survey,SurveyAdmin)

class QuestionResource(resources.ModelResource):
    class Meta:
        model = Question



class QuestionAdmin(admin.ModelAdmin):

    list_display = ('title', 'choice_one', 'choice_two', 'choice_three', 'choice_four',)
    list_filter = ('title',)
    search_fields = ('title',)

admin.site.register(Question,QuestionAdmin)