function  VerificaCPF(){
		if (vercpf(document.frmcpf.cpf.value)){
			return true;
		}
		else
			{
				alert('CPF INVALIDO');
				document.frmcpf.cpf.focus();	
				return false;			
			}
		}
	
	function vercpf (cpf) {
		if (cpf.length != 11 || cpf == "00000000000" || cpf == "11111111111" || cpf == "22222222222" || cpf == "33333333333" || cpf == "44444444444" || cpf == "55555555555" || cpf == "66666666666" || cpf == "77777777777" || cpf == "88888888888" || cpf == "99999999999")
		return false;		
		add = 0;
		for (i=0; i < 9; i ++)
			add += parseInt(cpf.charAt(i)) * (10 - i);
		rev = 11 - (add % 11);
		if (rev == 10 || rev == 11)
			rev = 0;
		if (rev != parseInt(cpf.charAt(9)))
		return false;
				
				
		add = 0;
		for (i = 0; i < 10; i ++)
			add += parseInt(cpf.charAt(i)) * (11 - i);
		rev = 11 - (add % 11);
		if (rev == 10 || rev == 11)
			rev = 0;
		if (rev != parseInt(cpf.charAt(10)))	
			return false;
		//alert('cpf valido.');
		return true;
}

function Apenas_Numeros(caracter)
{
	var nTecla = 0;
	if (document.all) {
		nTecla = caracter.keyCode;
    }
	else
	{
     	nTecla = caracter.which;
    }
	if ((nTecla> 47 && nTecla <58)
    || nTecla == 8 || nTecla == 127
    || nTecla == 0 || nTecla == 9  // 0 == Tab
    || nTecla == 13) { // 13 == Enter
		return true;
    }
	else
	{
    	return false;
    }
}

function validaNome()
	{
	if (document.frmcpf.nome.value == "")
	{
  		alert('Digite o nome!');
  		document.frmcpf.nome.focus();
     	return false;
	}
	else{
		return true;
		}
	}
function validaTelefone()
	{
	if (document.frmcpf.telefone.value == "")
	{
  		alert('Digite o telefone!');
  		document.frmcpf.telefone.focus();
     	return false;
	}
	else{
		return true;
		}
	}

function validaTamanhoCamisa()
	{
	if (document.frmcpf.tamanhocamisa.value == "")
	{
  		alert('Selecione o tamanho da camisa!');
  		document.frmcpf.tamanhocamisa.focus();
     	return false;
	}
	else{
		return true;
		}
	}

function validaDeficienciaF()
	{
	if (document.frmcpf.deficienciaF.value == "")
	{
  		alert('Selecione se tem deficiencia fisica!');
  		document.frmcpf.deficienciaF.focus();
     	return false;
	}
	else{
		return true;
		}
	}

function validaCampos(){
	if((validaNome()) &&  (VerificaCPF()) && (validaTelefone()) && (validaTamanhoCamisa()) && (validaDeficienciaF())){
		document.frmcpf.submit();
	}
}

function mascara_telefone() {
	
	if (document.frmcpf.telefone.value.length==0){ 	
		document.frmcpf.telefone.value+='(';
	}
	if(document.frmcpf.telefone.value.length == 3) {
		document.frmcpf.telefone.value += ')';
	}
	if(document.frmcpf.telefone.value.length == 8) {
		document.frmcpf.telefone.value += '-';
	}
}

function maiuscula(valor) {
var campo=document.form;
campo.texto.value=campo.texto.value.toUpperCase();
}
