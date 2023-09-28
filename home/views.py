from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'home/index.html'

    def get(self, request, *args, **kwargs):
        return self.render_to_response(
            self.get_context_data())


def error_404_view(request, exception):
    return render(request, '404.html')


def error_500_view(request):
    return render(request, '500.html')
