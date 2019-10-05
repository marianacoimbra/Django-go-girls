from django.shortcuts import render

#leva a solicitação e irá retornar o valor que recebe ao chamar outra função render que irá renderizar (montar) nosso modelo 

def post_list(request):
    return render(request, 'blog/post_list.html', {})

