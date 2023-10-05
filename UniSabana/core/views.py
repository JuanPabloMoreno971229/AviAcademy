from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
class HomePageView(TemplateView):
    template_name = "core/index.html"
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        message = request.POST.get('message')
        response = 'Hi, this is my response'
        return JsonResponse({'message': message, 'response': response})


class SingInPageView(TemplateView):
    template_name = "core/signin.html"

class SingOutPageView(TemplateView):
    template_name = "core/signout.html"

