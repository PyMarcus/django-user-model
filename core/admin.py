from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = ('title', '_author')

    def _author(self, instance) -> str:
        return str(instance.author.get_full_name())

    def get_queryset(self, request):
        qs = super(PostAdmin, self).get_queryset(request)
        return qs.filter(author=request.user) # search post only the logged user
