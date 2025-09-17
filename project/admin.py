from django.contrib import admin

from .models import Tag, Project, Task, ProjectFile, StatusProject, PriorityProject


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title', 'created_at','display_count_files']

    @admin.action(description='колличество файлов')
    def display_count_files(self,obj):
        return obj.count_files


    def replace_chair(self, request,objects):
        for obj in objects:
            obj.title = obj.title.replace(' ', '_')
            obj.save()
        return objects

    replace_chair.short_description = " Изменение пробела на нижнее подчеркивание"

    actions = ['replace_chair']

def make_status_action(status_value, description):
    def action(modeladmin, request, quaryset):
        quaryset.update(priority=status_value)

    action.short_description = description
    action.__name__=f"priotity_{status_value}".replace(" " , "_")
    return action


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title', 'project','status', 'priority', 'created_at','due_date' ]
    list_filter = ['status', 'priority','project','created_at','due_date']
    actions = [
        make_status_action(f"{value}", f"Установка приоритета {lable}")
        for value,lable in PriorityProject.choices
    ]

    def change_status(self, request,objects):
        for obj in objects:
            obj.status = StatusProject.CLOSED
            obj.save()
        return objects

    change_status.short_description = " Закрытие задачи"

    actions.extend(
        [
            make_status_action(f"{value}", f"Установка приоритета {lable}")
            for value, lable in StatusProject.choices
        ]
    )


    # def change_priority_low(self, request,objects):
    #     for obj in objects:
    #         obj.priority = PriorityProject.LOW
    #         obj.save()
    #     return objects
    #
    # change_priority_low.short_description = " Установка приоритета 'Low'"
    #
    # def change_priority_medium(self, request,objects):
    #     for obj in objects:
    #         obj.priority = PriorityProject.MEDIUM
    #         obj.save()
    #     return objects
    #
    # change_priority_medium.short_description = " Установка приоритета 'Medium'"
    #
    # def change_priority_high(self, request,objects):
    #     for obj in objects:
    #         obj.priority = PriorityProject.HIGH
    #         obj.save()
    #     return objects
    #
    # change_priority_high.short_description = " Установка приоритета High"
    #
    #
    # def change_priority_very_high(self, request,objects):
    #     for obj in objects:
    #         obj.priority = PriorityProject.VERY_HIGH
    #         obj.save()
    #     return objects
    #
    # change_priority_very_high.short_description = " Установка приоритета 'Very High'"
    #
    #
    #
    #
    # actions = ['change_status', 'change_priority_low','change_priority_medium', 'change_priority_high', 'change_priority_very_high']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(ProjectFile)
class ProjectFileAdmin(admin.ModelAdmin):
    list_display =['name', 'file', 'created_at']
    search_fields = ['name']
    list_filter = ['created_at']








