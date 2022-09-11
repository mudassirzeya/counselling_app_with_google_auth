from django import forms
from django.db.migrations.state import get_related_models_tuples
from .models import Comment
from django.utils.translation import gettext_lazy as _


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
