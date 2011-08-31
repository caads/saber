#encoding: utf-8
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from saber.caminhada.models import Inscricao
from django.forms import ModelForm, TextInput
from django.shortcuts import render_to_response,get_object_or_404
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail, get_connection, EmailMessage
from django.contrib.auth.decorators import login_required
from forms import CadastroForm
from django.contrib.auth.models import User

#Cadastro de Usuario
def cadastrar(request):
    if request.POST:
        form = CadastroForm(request.POST)
        if form.is_valid():
            novo_usuario = form.save()
            return HttpResponseRedirect('/login')
        else:
            return render_to_response('cadastrar.html', {'form': form}, context_instance=RequestContext(request))
    else:
        form = CadastroForm()
        return render_to_response('cadastrar.html', {'form': form}, context_instance=RequestContext(request))

def consultar_esqueci(request):
    return render_to_response('esqueci_email.html', context_instance = RequestContext(request))

def resultado_esqueci(request):
    if request.method == 'POST':
        try:
            email = request.POST['email']
            consulta = User.objects.get(email=email) 
            mensagem  = 'Foi enviado ao seu email sua nova senha:' 
            random = User.objects.make_random_password(length=10, allowed_chars='abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789')
            consulta.set_password(random)
            subject = 'Caminhada Nova Senha:'
            message = ('Sua nova senha é:' + random)   
            from_email = ''#email remetente
            connection = get_connection(username = '', password ='') #e-mail e senha do remetente
            send_email = EmailMessage(subject, message , from_email, [consulta.email], connection = connection)
            send_email.content_subtype = "html"
            send_email.send()
            consulta.save()  
        except ObjectDoesNotExist:
            consulta = ''
            mensagem = 'Este email não está cadastrado em nosso sistema!'
        return render_to_response('esqueci_email.html',{ 'mensagem' : mensagem,}, context_instance = RequestContext(request))

def comprovante(request, numeroInscricao):
    c = get_object_or_404(Inscricao, pk=numeroInscricao)
    return render_to_response('comprovante.html', {'inscricao':c}, context_instance = RequestContext(request))

@login_required
def relatorio(request):
    i = Inscricao.objects.all()
    return render_to_response('relatorio.html',{'i':i}, context_instance = RequestContext(request))


def inscrever(request):
    if request.POST:
        f = InscricaoModelForm(request.POST) 
        if f.is_valid(): 
            c = f.save()
            subject = 'Caminhada do Saber'
            message = 'Obrigado pela sua inscricao, te aguardamos na caminhada do saber!'
            from_email = ''#email remetente
            connection = get_connection(username = '', password ='')#email e senha remetente
            send_email = EmailMessage(subject, message , from_email, [c.email], connection = connection)
            send_email.content_subtype = "html"
            send_email.send()
            return HttpResponseRedirect(reverse('saber.caminhada.views.comprovante', args=[c.numeroInscricao]))
        else:
			return render_to_response('erro.html')
    else:
        f = InscricaoModelForm()
        return render_to_response('inscrever.html' , {'form' : f,},context_instance = RequestContext(request))

def consultar(request):
	return render_to_response('consultar.html', context_instance = RequestContext(request))

def filtrar_inscritos(request):
	mensagem  = 'Procure seu cpf:'
	try:
		cpf = request.POST['codigo']
		inscricao = Inscricao.objects.get(cpf=cpf) 
		mensagem  = 'CPF encontrado:'     
	except ObjectDoesNotExist:
		inscricao = ''
		return render_to_response('erro2.html')

	dados_template = { 'mensagem'  : mensagem, 'inscricao' : inscricao,}
	return render_to_response('result.html',dados_template, context_instance = RequestContext(request))



class InscricaoModelForm(ModelForm):
    class Meta:
        model = Inscricao
        field = ('nome')
        widgets = {
            'nome': TextInput(attrs={'size':50}),
        }


   
