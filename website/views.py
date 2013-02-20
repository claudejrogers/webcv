from bakery.views import BuildableTemplateView, BuildableListView
from website.models import Author, Article, Carousel


class IndexListView(BuildableListView):
    context_object_name = 'carousel'
    template_name = 'website/index.html'
    build_path = 'home.html'
    queryset = Carousel.objects.all()


class PublicationsListView(BuildableListView):
    context_object_name = 'publications'
    template_name = 'website/publications.html'
    build_path = 'publications.html'
    queryset = Article.objects.all()


class ContactTemplateView(BuildableTemplateView):
    template_name = 'website/contact.html'
    build_path = 'contact.html'

    def get_context_data(self, **kwargs):
        me = Author.objects.get(first_name="Claude", last_name="Rogers")
        return {'me': me}


class AboutTemplateView(BuildableTemplateView):
    template_name = 'website/about.html'
    build_path = 'about.html'
