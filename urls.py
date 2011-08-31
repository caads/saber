from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib import admin
from saber.caminhada.views import *


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'saber.views.home', name='home'),
    # url(r'^saber/', include('saber.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
	#(r'^adicionar_cliente/$', 'tutorial.tuto2.views.adicionar_cliente'),
    (r'^cadastrar/', 'saber.caminhada.views.cadastrar'),
	(r'^inscrever/', 'saber.caminhada.views.inscrever'),
	(r'^relatorio/', 'saber.caminhada.views.relatorio'),
	(r'^comprovante/(?P<numeroInscricao>\d+)/$', 'saber.caminhada.views.comprovante'),
	(r'^consultar/', consultar),
	(r'^resultado/$', filtrar_inscritos),
    (r'^login/', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    (r'^consultar/$','saber.caminhada.views.consultar_esqueci'),
    (r'^resultado_esqueci/$','saber.caminhada.views.resultado_esqueci'),
    (r'^mudar_senha/$', 'django.contrib.auth.views.password_change',{'template_name': 'mudar_senha.html'}, 'mudar_senha'),
    (r'^mudar_senha/concluido/$', 'django.contrib.auth.views.password_change_done',{'template_name': 'mudar_senha_concluido.html'}, 'mudar_senha_concluido'),
    (r'^logout/', 'django.contrib.auth.views.logout', {'template_name': 'logout.html', 'next_page': '/login'}),
    (r'^media/(.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
)
    



