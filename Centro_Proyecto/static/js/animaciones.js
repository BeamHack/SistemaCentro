
$(document).ready(function(){

$("#desaparecer").on("click",function(){

	$("#citas").hide(1000);
});


//$('#cita').hide(10000);
	if('#animacion_pac'){
		$('#animacion_pac').hide();
		$('#animacion_pac').slideDown(2000);
		$('#animacion_pac').css('font ','oblique bold 120% cursive');

	}
	
		$('.aparecer').hide();
		
		$('#fechaExamen').on('click',function () {

   			var $submenu=$('.aparecer');

   		if ($submenu.is(':hidden')) {
   			$submenu.show(1000);
   			$(this).text('Ocultar detalles de los mensajes')

  		} else {
   			$(this).text('Mostar detalles de los mensajes')
   			$submenu.hide(1000);
  	}
 });

if('#contenido'){
		$('#contenido').hide();
		$('#contenido').slideDown(2000);
		$('#contenido').css('font ','oblique bold 120% cursive');

	}




$(".presentar").on('click',presentarClick);

function presentarClick(){
	var id= $(this).attr('id');
	

	$.ajax({
		data:{'id':id},
		url:"/presentar-ajax/",
		type:'get',
		success:function(data){
			var html;
			for (var i=0; i<data.length; i++){
				html='<table id="cita_dia"><tr align="center" valign="middle"><tr><td width="40%"> Nombre: </td><td>'+data[i].fields.Dias+'</td></tr></div></table>';
				}
			 

			$('.datos').html(html);
		}		


	});

}		

$("imprimirPac")


$(".btn-xs").on('click',hacerClick);




function hacerClick(){
	var id= $(this).attr('id');
	

	$.ajax({
		data:{'id':id},
		url:"/buscar-ajax/",
		type:'get',
		success:function(data){
			var html;
			for (var i=0; i<data.length; i++){
			
					html='<table id="cita_dia"><tr align="center" valign="middle"><td rowspan="7" width="4cm"><img id="img_paciente" src="/media/'+data[i].fields.foto+'/" class="img-rounded"/><br><span><a  href="/historia/'+data[i].fields.cedula+'">Ver Historia Clinica Completa</a></span></td></tr><tr><td width="40%"> Nombre: </td><td>'+data[i].fields.nombre +'</td></tr><tr><td> Apellido: </td><td> '+data[i].fields.apellido+'</td></tr><tr><td> Direccion: </td><td>'+data[i].fields.direccion +'</td></tr></div></table>';
				}
			 

			$('.datos').html(html);
		}		


	});

}		

	$('.user').css({'color':'white', 'margin-left':'1000px', 'margin-top':'-40px'});




});