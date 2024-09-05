from django import forms

class LoginForms(forms.Form):
  nome_login=forms.CharField(
    label='Nome de Usuario',
    required=True,
    max_length=100,
    widget=forms.TextInput(
      attrs={
        "class": "form-control"
      }
    )
  )
  senha=forms.CharField(
    label='Senha',
    required=True,
    max_length=70,
    widget=forms.PasswordInput(
      attrs={
        "class": "form-control",
        "placeholder": "Digite sua senha"
      }
    )
  )
  
class CadastroForms(forms.Form):
  nome_cadastro=forms.CharField(
    label='Nome de Cadastro',
    required=True,
    max_length=100,
    widget=forms.TextInput(
      attrs={
        "class": "form-control",
        "placeholder": "Ex.: João Silva"
      }
    )
  )
  email=forms.EmailField(
    label='Email',
    required=True,
    max_length=100,
    widget=forms.EmailInput(
      attrs={
        "class": "form-control",
        "placeholder": "Ex.: joaosilva@xpto.com"
      }
    )
  )
  senha_1=forms.CharField(
    label='Senha',
    required=True,
    max_length=70,
    widget=forms.PasswordInput(
      attrs={
        "class": "form-control",
        "placeholder": "Digite sua senha"
      }
    )
  )
  senha_2=forms.CharField(
    label='Digite sua senha novamente',
    required=True,
    max_length=70,
    widget=forms.PasswordInput(
      attrs={
        "class": "form-control",
        "placeholder": "Digite sua senha"
      }
    )
  )
def clean_nome_cadastro(self):
  nome=self.cleaned_data_get("nome_cadastro")
  if nome:
    nome = nome.strip()
    if " " in nome:
      raise forms.ValidationError("Não é possivel inserir espaços dentro do campo usuário")
    else:
      return nome
  