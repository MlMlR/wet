from django.views import generic
from django.utils import timezone

from .models import Post


class IndexView(generic.ListView):
    template_name = "blog/index.html"
    context_object_name = "latest_post_list"

    def get_queryset(self):
        """ 
        Return the last five published posts (not including those set to be
        published in the future).
        """
        return Post.objects.filter(publish_date__lte=timezone.now()).order_by("-publish_date")[:5]
