$(document).ready(function(){

		$(".seguroBtn").on("click", hacerClick);

		function hacerClick(){
			var id=$(this).attr('id');
			console.log(id);
			
			$.ajax({
				data:{'id':id},
				url:"/asincronoSeguro",
				type:"get",

				success : function(data){
					for (var i = 0; i <= data.length; i++) {	
						var html;
						console.log(data[i].fields.nombre)
						html='<table id="cita_dia"><tr align="center" valign="middle"><td rowspan="7" width="4cm"><img id="img_paciente" src="/media/'+data[i].fields.foto+'/" class="img-rounded"/><br><span><a  href="/historia/'+data[i].fields.cedula+'">Ver Historia Clinica Completa</a></span></td></tr><tr><td width="40%"> Nombre: </td><td>'+data[i].fields.nombre +'</td></tr><tr><td> Apellido: </td><td> '+data[i].fields.apellido+'</td></tr><tr><td> Fecha de ingreso: </td><td>'+data[i].fields.fechaIngreso +'</td></tr></div></table>';	
						
				}
				$(".datos").html(html);
			}
			
		});
	}
});