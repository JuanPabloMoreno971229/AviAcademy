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
            print(response)
            # Devolver la respuesta en un JSON
            print(4)
            return JsonResponse({'message': message, 'response': response})
            
        except Exception as e:
            # Manejar cualquier excepción que pueda ocurrir y devolver un mensaje de error
            return JsonResponse({'error': str(e)})
    def ask_openai(self, message):
        print(message)
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
            response = """
                Pregunta 1: ¿Cuál es el objetivo principal del substring mining en minería de datos?
                A) Identificar patrones de búsqueda
                B) Encontrar subcadenas en una secuencia
                C) Clasificar grandes conjuntos de datos
                D) Generar números pseudoaleatorios
                ANSWER: B

                Pregunta 2: ¿Qué es la longitud mínima de un substring para que sea considerado relevante en el proceso de substring mining?
                A) 1
                B) 2
                C) 3
                D) 4
                ANSWER: A

                Pregunta 3: En el contexto del substring mining, ¿qué es la "cobertura" de un substring?
                A) El número de secuencias en las que aparece el substring
                B) La longitud total del substring
                C) El número de caracteres distintos en el substring
                D) La probabilidad de ocurrencia del substring
                ANSWER: A

                Pregunta 4: ¿Cuál es una técnica comúnmente utilizada en substring mining para encontrar subcadenas con alta ocurrencia?
                A) Algoritmo de Dijkstra
                B) Algoritmo de ordenación rápida
                C) Algoritmo Apriori
                D) Algoritmo de Euclides
                ANSWER: C

                Pregunta 5: ¿Qué métrica se utiliza para evaluar la calidad de los resultados en substring mining?
                A) Precisión
                B) Recall
                C) F1-score
                D) Coeficiente de correlación
                ANSWER: C
                """
             # Manejar cualquier excepción que pueda ocurrir al interactuar con OpenAI
            print("F")
            return response
        
        print(message)
        

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

