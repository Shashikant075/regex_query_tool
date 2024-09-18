from django import forms

class RegexQueryForm(forms.Form):
    text = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Enter text for search', 'rows': 4}),
        required=False, 
        label="Text to Search"
    )
    pattern = forms.CharField(
        max_length=255, 
        label="Regex Pattern",
        widget=forms.TextInput(attrs={'placeholder': 'Enter regex pattern'})
    )
    upload_file = forms.FileField(
        required=False,
        label="Upload a Text File or PDF",
        widget=forms.ClearableFileInput(attrs={'accept': '.txt,.csv,.pdf'})  # Accept text, CSV, and PDF files
    )

    