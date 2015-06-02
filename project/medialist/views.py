from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.views.generic import ListView, CreateView

from medialist.models import Media, MediaMeta, MediaVersion, MediaComment
from medialist.models import Journalist, JournalistArticle, JournalistComment
from medialist.models import JournalistArticleMeta, JournalistMeta, JournalistVersion

from django.shortcuts import get_object_or_404

from django.contrib.auth.models import User


class MediaList(ListView):
    model = Media
    template_name = 'medialist/media_list.html'

    def get_queryset(self):
        qs = super(MediaList, self).get_queryset()
        return qs.order_by('-id')

    """
    def get_context_data(self, **kwargs):
        context = super(HolywarDetail, self).get_context_data(**kwargs)
        context["asd"] = "asd"
        return context
    """


class MediaDetail(CreateView):
    model = MediaComment
    template_name = 'medialist/media_detail.html'
    fields = ['text']

    def get_context_data(self, **kwargs):
        context = super(MediaDetail, self).get_context_data(**kwargs)

        media_data = get_object_or_404(Media, slug=self.kwargs['slug'])
        comments = MediaComment.objects.filter(media=media_data)
        journalists = Journalist.objects.filter(media=media_data)

        context["media"] = media_data
        context["comments"] = comments
        context["journalists"] = journalists

        return context

    def form_valid(self, form):

        slug = self.kwargs['slug']
        media = get_object_or_404(Media, slug=slug)

        instance = form.save(commit=False)

        instance.author = self.request.user
        instance.media = media

        instance.save()

        return HttpResponseRedirect(reverse('media:media_detail', kwargs={'slug': slug}))


class MediaUpdate(CreateView):
    model = MediaVersion
    template_name = 'medialist/media_update.html'
    fields = ['new_value']

    def get_context_data(self, **kwargs):
        context = super(MediaUpdate, self).get_context_data(**kwargs)

        media_data = get_object_or_404(Media, slug=self.kwargs['slug'])
        field = self.kwargs['field']
        old_value = getattr(media_data, field)

        context["media"] = media_data
        context["field"] = field
        context["old_value"] = old_value

        return context

    def form_valid(self, form):

        slug = self.kwargs['slug']
        field = self.kwargs['field']

        media = get_object_or_404(Media, slug=slug)

        instance = form.save(commit=False)

        instance.old_value = getattr(media, field)

        field.replace('f', '+')
        instance.field = field
        instance.media = media

        instance.save()

        return HttpResponseRedirect(reverse('media:media_detail', kwargs={'slug': slug}))


class MediaCreate(CreateView):
    model = MediaMeta
    template_name = 'medialist/media_create.html'
    fields = [
                'name', 'link', 'platforms', 'categories', 'alexa_rank',
                'language', 'amount_journalists', 'email'
            ]

    def get_success_url(self):
        return reverse('media:media_list')

        # return reverse('thread_detail', args=(self.object.thread.id,))


class JournalistDetail(CreateView):
    model = JournalistComment
    template_name = 'medialist/journalist_detail.html'
    fields = ['text']

    def get_context_data(self, **kwargs):
        context = super(JournalistDetail, self).get_context_data(**kwargs)

        journalist_data = get_object_or_404(Journalist, media__slug=self.kwargs['slug'], slug=self.kwargs['journalist'])
        comments = JournalistComment.objects.filter(journalist=journalist_data)
        articles = JournalistArticle.objects.filter(journalist=journalist_data)

        context["journalist"] = journalist_data
        context["comments"] = comments
        context["articles"] = articles

        return context

    def form_valid(self, form):

        slug = self.kwargs['slug']
        jrt = self.kwargs['journalist']

        journalist = get_object_or_404(Journalist, media__slug=slug, slug=jrt)

        instance = form.save(commit=False)

        instance.author = self.request.user
        instance.journalist = journalist

        instance.save()

        return HttpResponseRedirect(reverse('media:journalist_detail', kwargs={'slug': slug, 'journalist' : jrt}))


class JournalistUpdate(CreateView):
    model = JournalistVersion
    template_name = 'medialist/journalist_update.html'
    fields = ['new_value']

    def get_context_data(self, **kwargs):
        context = super(JournalistUpdate, self).get_context_data(**kwargs)

        slug = self.kwargs['slug']
        jrt = self.kwargs['journalist']

        journalist = get_object_or_404(Journalist, media__slug=slug, slug=jrt)

        field = self.kwargs['field']
        old_value = getattr(journalist, field)

        context["journalist"] = journalist
        context["field"] = field
        context["old_value"] = old_value

        return context

    def form_valid(self, form):

        slug = self.kwargs['slug']
        jrt = self.kwargs['journalist']

        field = self.kwargs['field']

        journalist = get_object_or_404(Journalist, media__slug=slug, slug=jrt)

        instance = form.save(commit=False)

        instance.old_value = getattr(journalist, field)

        field.replace('f', '+')
        instance.field = field
        instance.journalist = journalist

        instance.save()

        return HttpResponseRedirect(reverse('media:journalist_detail', kwargs={'slug': slug, 'jrt': jrt}))


class JournalistCreate(CreateView):
    model = JournalistMeta
    template_name = 'medialist/journalist_create.html'
    fields = ['name', 'position', 'categories', 'link_to_twitter', 'link_to_linkedin', 'activity', 'email']

    def get_context_data(self, **kwargs):
        context = super(JournalistCreate, self).get_context_data(**kwargs)

        media_data = get_object_or_404(Media, slug=self.kwargs['slug'])

        context["media"] = media_data
        return context

    def form_valid(self, form):

        slug = self.kwargs['slug']

        media = get_object_or_404(Media, slug=slug)

        instance = form.save(commit=False)

        instance.media = media

        instance.save()

        return HttpResponseRedirect(reverse('media:media_detail', kwargs={'slug': slug}))


class JournalistArticleCreate(CreateView):
    model = JournalistArticleMeta
    template_name = 'medialist/journalist_article_create.html'
    fields = ['link']

    def get_context_data(self, **kwargs):
        context = super(JournalistArticleCreate, self).get_context_data(**kwargs)

        journalist_data = get_object_or_404(Journalist, media__slug=self.kwargs['slug'], slug=self.kwargs['journalist'])

        context["journalist"] = journalist_data

        return context

    def form_valid(self, form):

        slug = self.kwargs['slug']
        jrt = self.kwargs['journalist']

        journalist = get_object_or_404(Journalist, media__slug=slug, slug=jrt)

        instance = form.save(commit=False)
        instance.journalist = journalist

        instance.save()

        return HttpResponseRedirect(reverse('media:journalist_detail', kwargs={'slug': slug, 'journalist' : jrt}))


def profile(request, **kwargs):

    username = kwargs['slug']

    user = get_object_or_404(User, username=username)

    comments_media = MediaComment.objects.filter(author=user)
    comments_journalist = JournalistComment.objects.filter(author=user)

    # avatar = user.socialaccount_set.all().first().extra_data.profile_image_url
    # nickname = user.socialaccount_set.all().first().extra_data.screen_name

    context = {'user': user, 'comments_media': comments_media, 'comments_journalist': comments_journalist}
    return render(request, 'medialist/profile.html', context)
