from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, ListView
from .forms import CursoForm
from .models import Curso

class CursoCreateView(View):
    def get(self, request):
        form = CursoForm()
        return render(request, 'cursoscreate.html', {'form': form})
    
    def post(self, request):
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('curso-list')
        return render(request, 'cursoscreate.html', {'form': form})
    
class CursoListView(ListView):
    model = Curso
    template_name = 'cursoslist.html'
    context_object_name = 'cursos'

    def get_queryset(self):
        return Curso.objects.all()
        
class CursoDeleteView(View):
    def post(self, request, pk):
        curso = get_object_or_404(Curso, pk=pk)
        curso.delete()
        return redirect ('curso-list')
        
