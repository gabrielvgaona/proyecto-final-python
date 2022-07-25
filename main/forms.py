from django import forms

class MainForm(forms.Form):
    num1 = forms.DecimalField(label = " Primer número [A]", 
                              required = False)
    num2 = forms.DecimalField(label = "Segundo número [B]",
                              required = False)
    
    def __init__(self, *args, **kwargs):
        super(MainForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'text-center col s6'
            visible.field.widget.attrs['placeholder'] = 'Ingresa un valor numérico'

