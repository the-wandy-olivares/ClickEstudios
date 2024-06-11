from django import forms
from .  import models

class CustomerForm(forms.ModelForm):
      class Meta:
            model = models.Customer
            fields = '__all__'  # Include all fields

      def __init__(self, *args, **kwargs):
            super(CustomerForm, self).__init__(*args, **kwargs)
            # Add the 'form-control' class to all form fields
            for field in self.fields:
                  self.fields[field].widget.attrs['class'] = 'form-control'
            # Add placeholders to form fields
            # self.fields['name'].widget.attrs['placeholder'] = 'Nombre y Apellidos'
            self.fields['last_name'].widget.attrs['placeholder'] = 'Apellidos'
            self.fields['dni'].widget.attrs['placeholder'] = 'Cedula'
            # self.fields['email'].widget.attrs['placeholder'] = 'Correo electronico'
            # self.fields['number'].widget.attrs['placeholder'] = 'Numero de celular'


class AppointmentForm(forms.ModelForm):
      class Meta:
            model = models.Appointment
            fields = ['customer', 'date_remember', 'date_remember_time']  # Especifica los campos que quieres mostrar en el formulario
            
            widgets = {
            'date_remember': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'date_remember_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
        }

      def __init__(self, *args, **kwargs):
            super(AppointmentForm, self).__init__(*args, **kwargs)
            # Add the 'form-control' class to all form fields
            for field in self.fields:
                  self.fields[field].widget.attrs['class'] = 'form-control'
                  
                  
                  
                  
