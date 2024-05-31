from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from .models import Blog

class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs = {'class':'form-control'}))
    password2 = forms.CharField(label="Confirm Password",widget=forms.PasswordInput(attrs = {'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email',]
        labels = {'first_name': 'First Name','last_name':'Last Name','email':'Email'}
        widgets = {'username':forms.TextInput(attrs={'class':'form-control'}),
                   'first_name':forms.TextInput(attrs={'class':'form-control'}),
                   'last_name':forms.TextInput(attrs={'class':'form-control'}),
                   'email':forms.EmailInput(attrs={'class':'form-control'}),
                   }
        
class LoginForm(AuthenticationForm):
    username = UsernameField(widget = forms.TextInput(attrs = {'class':'form-control'}))
    password = forms.CharField(label=_("Password"),strip = False, widget = forms.PasswordInput(attrs={'class':'form-control'}))


class BlogForm(forms.ModelForm):
    TOPIC_CHOICES = [
        ('ai_ml', 'Artificial Intelligence (AI) and Machine Learning (ML)'),
        ('iot', 'Internet of Things (IoT)'),
        ('cybersecurity', 'Cybersecurity'),
        ('blockchain', 'Blockchain and Cryptocurrency'),
        ('ar_vr', 'Augmented Reality (AR) and Virtual Reality (VR)'),
        ('quantum_computing', 'Quantum Computing'),
        ('5g_technology', '5G Technology'),
        ('edge_computing', 'Edge Computing'),
        ('biotechnology', 'Biotechnology'),
        ('nanotechnology', 'Nanotechnology'),
        ('robotics', 'Robotics'),
        ('drones', 'Drones and UAVs'),
        ('genetic_engineering', 'Genetic Engineering'),
        ('renewable_energy', 'Renewable Energy Technologies'),
        ('smart_cities', 'Smart Cities'),
        ('wearable_technology', 'Wearable Technology'),
        ('space_technology', 'Space Technology'),
        ('autonomous_vehicles', 'Autonomous Vehicles'),
        ('big_data', 'Big Data Analytics'),
        ('cloud_computing', 'Cloud Computing'),
        ('3d_printing', '3D Printing'),
        ('fintech', 'Financial Technology (Fintech)'),
        ('healthtech', 'Healthcare Technology (Healthtech)'),
        ('agritech', 'Agricultural Technology (Agritech)'),
        ('cyber_physical_systems', 'Cyber-Physical Systems'),
        ('biometrics', 'Biometric Security'),
        ('voice_technology', 'Voice Technology'),
        ('internet_of_behaviors', 'Internet of Behaviors (IoB)'),
        ('carbon_capture', 'Carbon Capture and Storage (CCS)'),
        ('decentralized_finance', 'Decentralized Finance (DeFi)'),
        ('metaverse', 'Metaverse'),
        ('smart_grid', 'Smart Grid Technology'),
        ('cryptocurrency', 'Cryptocurrency and Blockchain'),
        ('quantum_internet', 'Quantum Internet'),
        ('electric_vehicles', 'Electric Vehicles (EVs)'),
        ('hyperloop', 'Hyperloop Transportation'),
        ('personalized_medicine', 'Personalized Medicine'),
        ('digital_twins', 'Digital Twins'),
        ('low_code_no_code', 'Low-Code/No-Code Development'),
        ('neurotechnology', 'Neurotechnology'),
        ('predictive_analytics', 'Predictive Analytics'),
        ('sustainable_technology', 'Sustainable Technology'),
        ('emerging_technology', 'Emerging Technology Trends'),
        ('future_technology', 'Future Technology'),
        ('tech_innovation', 'Technology Innovation'),
        ('Other', 'Others'),

    ]

    topics = forms.MultipleChoiceField(choices=TOPIC_CHOICES, widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Blog
        fields = ['title','subheading','topics','cont','image']
        labels = {'title':'Title','subheading':'Subheading', 'topics':'Topics','cont':'Content'}
        widgets = {'title':forms.TextInput(attrs={'class':'form-control'}),'subheading':forms.TextInput(attrs={'class':'form-control'}),'cont':forms.Textarea(attrs={'class':'form-control'})}