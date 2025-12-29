from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Note, Category
from .forms import NoteForm

def note_list(request):
    notes = Note.objects.all().order_by("-created_at")
    search_query = request.GET.get('q', '')

    if search_query:
        notes = notes.filter(
            Q(title__icontains=search_query) | 
            Q(content__icontains=search_query) |
            Q(category__name__icontains=search_query)
        )

    categories = Category.objects.all()

    return render(request, "notes/note_list.html", {
        "notes": notes,
        "categories": categories,
        "search_query": search_query,
    })

def category_page(request, slug):
    current_category = get_object_or_404(Category, slug=slug)
    notes = Note.objects.filter(category=current_category).order_by("-created_at")
    categories = Category.objects.all()

    return render(request, "notes/note_list.html", {
        "notes": notes,
        "categories": categories,
        "current_category": current_category
    })

def note_detail(request, pk):
    note = get_object_or_404(Note, pk=pk)
    categories = Category.objects.all()

    return render(request, "notes/note_detail.html", {
        "note": note,
        "categories": categories
    })

def note_create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm()

    return render(request, 'notes/note_form.html', {'form': form})