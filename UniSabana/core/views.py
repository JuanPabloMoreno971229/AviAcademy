from django.views.generic.base import TemplateView
from django.shortcuts import render, redirect
from django.http import JsonResponse
import openai

openai_api_key = 'a'
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
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        message = request.POST.get('prompt')
        try:
            # Llamar a la función ask_openai para obtener una respuesta de OpenAI
            response = self.ask_openai(message)
            answerFixed = self.fixAnswer(response)
            # Devolver la respuesta en un JSON
            print(4)
            return JsonResponse({'message': message, 'response': answerFixed})
            
        except Exception as e:
            # Manejar cualquier excepción que pueda ocurrir y devolver un mensaje de error
            return JsonResponse({'error': str(e)})
    def fixAnswer(self,answer):
        lineas = answer.strip().split('\n')
        formateado = []

        for linea in lineas:
            linea = linea.strip()
            if linea.startswith("Pregunta"):
                formateado.append("||" + linea[12:])
            elif linea.startswith("A)") or linea.startswith("B)") or linea.startswith("C)") or linea.startswith("D)") or linea.startswith("ANSWER") or  linea.startswith(""):
                formateado.append("||" + linea)

        return "".join(formateado) + "||"
    def ask_openai(self, message):
        try:
             response = openai.Completion.create(
                 model="text-davinci-003",
                 prompt=message,
                 max_tokens=200,
                 n=1,
                 stop=None,
                 temperature=0.7,
             )
             print("Bien")
             answer = response.choices[0].text.strip()
             print(response)
             return answer
        except Exception as e:
            response = """
                Pregunta 1: La minería de subcadenas se utiliza para encontrar patrones en una secuencia de datos.
                A. True
                B. False
                ANSWER: A

                Pregunta 2: En la minería de subcadenas, una subcadena es una secuencia de caracteres que aparece en una cadena más grande.
                A. True
                B. False
                ANSWER: A

                Pregunta 3: La minería de subcadenas se aplica principalmente en la exploración de datos espaciales.
                A. True
                B. False
                ANSWER: B

                Pregunta 4: La minería de subcadenas es una técnica que se utiliza para buscar patrones en texto, genómica y otras áreas.
                A. True
                B. False
                ANSWER: A

                Pregunta 5: El objetivo principal de la minería de subcadenas es encontrar todas las subcadenas posibles en una secuencia dada.
                A. True
                B. False
                ANSWER: B
                """
             # Manejar cualquier excepción que pueda ocurrir al interactuar con OpenAI
            print("F")
            return response
        

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
                 max_tokens=200,
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

