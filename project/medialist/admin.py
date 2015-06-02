from django.contrib import admin

#10

from medialist.models import Media, MediaMeta, MediaVersion, MediaComment
from medialist.models import Journalist, JournalistMeta, JournalistVersion
from medialist.models import JournalistArticle, JournalistArticleMeta, JournalistComment

admin.site.register(Media)
admin.site.register(MediaMeta)
admin.site.register(MediaVersion)
admin.site.register(MediaComment)

admin.site.register(Journalist)
admin.site.register(JournalistMeta)
admin.site.register(JournalistVersion)

admin.site.register(JournalistArticle)
admin.site.register(JournalistArticleMeta)

admin.site.register(JournalistComment)
