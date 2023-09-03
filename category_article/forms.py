from django import forms
from .models import Rating_Comment

class Rating_CommentForm(forms.ModelForm):
    class Meta:
        model = Rating_Comment
        fields = ['rating', 'comment']  
        
        
    def clean_rating(self):
        rating = self.cleaned_data.get('rating')
        if rating is not None and (rating < 0 or rating > 4):
            raise forms.ValidationError("Rating should be between 0 and 4.")
        return rating