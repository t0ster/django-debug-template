from django.views.generic import TemplateView


class MyView(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        return {
            'var': 'blah'
        }
