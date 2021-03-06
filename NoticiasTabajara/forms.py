# -*- coding: utf-8 -*- 
from django import forms
from django.contrib.admin.utils import label_for_field
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)


class CadastrarNoticia(forms.Form):
    titulo = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    resumo = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    data = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    texto = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    imagem = forms.ImageField(required=False)

    def __str__(self):
        return self.titulo


User = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.CharField(label='Nome', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Senha', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        # user_qs = User.objects.filter(username=username)
        # if user_qs.count() == 1:
        #     user = user_qs.first()
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("Usuário não existe")
            if not user.check_password(password):
                raise forms.ValidationError("Senha icorreta")
            if not user.is_active:
                raise forms.ValidationError("Usuário inativo")
        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(label='Nome', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Senha', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    email2 = forms.EmailField(label='Confirme o Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))


    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'email2',
            'password'
        ]

    # def clean(self, *args, **kwargs):
    #     email = self.cleaned_data.get('email')
    #     email2 = self.cleaned_data.get('email2')
    #     if email != email2:
    #         raise forms.ValidationError("Emails must match")
    #     email_qs = User.objects.filter(email=email)
    #     if email_qs.exists():
    #         raise forms.ValidationError("This email has already been registered")

    #     return super(UserRegisterForm,self).clean(*args, **kwargs)

    def clean_email2(self):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        if email != email2:
            raise forms.ValidationError("Emails não correspondem")
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("Email já registrado")
        return email


class CadastrarComentario(forms.Form):
    # data = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    nome = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    texto = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

    # active_status = forms.BooleanField(label='')

    def __str__(self):
        return self.nome
