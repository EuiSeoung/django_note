from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'category', 'content', 'is_html']
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '제목을 입력하세요'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10, 'placeholder': '내용을 입력하세요'}),

            'is_html': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'title': '제목',
            'category': '카테고리',
            'content': '내용',
            'is_html': 'HTML 코드 적용하기',
        }