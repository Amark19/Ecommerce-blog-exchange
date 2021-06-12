from django import forms
from .models import SellerDetails
class ImageForm(forms.ModelForm):
    class Meta:
        model=SellerDetails
        fields=("bookname","bookauthor","bookcategory","usedtime","title","price","city","longi","latt","img1","img2")