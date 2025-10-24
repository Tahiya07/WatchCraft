from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.NumberInput(attrs={
                'min': 1,
                'max': 5,
                'class': 'form-control',
                'step': 1,
                'placeholder': 'Rate from 1 to 5'
            }),
            'comment': forms.Textarea(attrs={
                'rows': 3,
                'class': 'form-control',
                'placeholder': 'Leave a review...'
            }),
        }
def clean_rating(self):
    rating = self.cleaned_data.get('rating')
    if rating < 1 or rating > 5:
        raise forms.ValidationError("Rating must be between 1 and 5.")
    return rating

