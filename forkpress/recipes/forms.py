from django import forms

class StepForm(forms.Form):
    step = forms.CharField(
        label="Be specific about the ingredients and equipment used in each step.",
        max_length=255)