from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = ('title', '_author')
    exclude = ['author']  # hidden author

    def _author(self, instance) -> str:
        return str(instance.author.get_full_name())

    def get_queryset(self, request):
        qs = super(PostAdmin, self).get_queryset(request)
        return qs.filter(author=request.user) # search post only the logged user

    def save_model(self, request, obj, form, change): # all
        obj.author = request.user
        super().save_model(request, obj, form, change) # allow save post withou the author label
