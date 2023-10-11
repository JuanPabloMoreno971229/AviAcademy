from django.views.generic.base import TemplateView
from django.shortcuts import render, redirect
from django.http import JsonResponse
import openai

openai_api_key = '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'
openai.api_key = openai_api_key



# Create your views here.
class HomePageView(TemplateView):
    template_name = "core/index.html"

class SingInPageView(TemplateView):
    template_name = "core/signin.html"

class SingOutPageView(TemplateView):
    template_name = "core/signout.html"
    
class TestGeneratorView(TemplateView):
    template_name = "core/testGenerator.html"
    
    print(1)
    def get(self, request, *args, **kwargs):
        print(2)
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        message = request.POST.get('prompt')
        print(3)
        try:
            # Llamar a la función ask_openai para obtener una respuesta de OpenAI
            response = self.ask_openai(message)

            # Devolver la respuesta en un JSON
            print(4)
            return JsonResponse({'message': message, 'response': response})
        except Exception as e:
            # Manejar cualquier excepción que pueda ocurrir y devolver un mensaje de error
            return JsonResponse({'error': str(e)})
    def ask_openai(self, message):
        print(message)
        return redirect("TestEditor")
        

class TestEditorView(TemplateView):
    template_name = "core/testEditor.html"

class ChatPageView(TemplateView):
    template_name = "core/chat.html"
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        message = request.POST.get('message')

        try:
            # Llamar a la función ask_openai para obtener una respuesta de OpenAI
            response = self.ask_openai(message)

            # Devolver la respuesta en un JSON
            return JsonResponse({'message': message, 'response': response})
        except Exception as e:
            # Manejar cualquier excepción que pueda ocurrir y devolver un mensaje de error
            return JsonResponse({'error': str(e)})

    def ask_openai(self, message):
        print("hola")
        try:
             response = openai.Completion.create(
                 model="text-davinci-003",
                 prompt=message,
                 max_tokens=20,
                 n=1,
                 stop=None,
                 temperature=0.7,
             )
             print(message)
             print("Bien")
             answer = response.choices[0].text.strip()
             print(response)
             return answer
        except Exception as e:
             # Manejar cualquier excepción que pueda ocurrir al interactuar con OpenAI
             return f"Error: {str(e)}"

