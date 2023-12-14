from django.shortcuts import render,redirect
from .models import BooksModel
from .forms import BooksForm
from .serializer import BooksSerializer
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
class BooksApi(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'home.html'

    def get(self, request):
        books = BooksModel.objects.all()
        return Response({'books': books})
    
# def BookList(request):
#     books = BooksModel.objects.all()
#     form = BooksForm()
#     if request.method == 'POST':
#         form = BooksForm(request.POST)
#         if form.is_valid():
#             form.save()
#         return redirect('/')
#     context = {'books': books, 'form': form}
#     return render(request, 'home.html', context)


def BookUpdate(request, id):
    books = BooksModel.objects.get(pk=id)
    form = BooksForm(instance=books)
    if request.method == 'POST':    
        form = BooksForm(request.POST, instance=books)
        if form.is_valid():
            form.save()
        return redirect('/')
    
    context = {'form': form}
    return render(request, 'update_book.html', context)

def BookDelete(request, id):
    books = BooksModel.objects.get(pk=id)
    if request.method == 'POST':
        books.delete()
        return redirect('/')
    
    context = {'books': books}
    return render(request, 'delete_book.html', context)
        
    
    
    
            


    