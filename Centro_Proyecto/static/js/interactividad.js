$(document).ready(function(){
	init()
});	//final

function init(){
	menu()
	slide()	
}

function active(){
	 $('#id_buscar').click(function() {
        $(this).addClass('form-control');
    });
}

//////////////Funcion Slides////////////////////
function slide(){
	$(".images").slidesjs({	
	play:{
		active:false,
		effect:"slide",
		interval: 3000,
		auto:true,
		swap:true,
		pauseOnHover:false,
		restartDelay:2500
	}		
	});
}


//////////////Funcion de Menu///////////////////
function menu(){
	var altura= $("header").offset().top // permite saber cuanto mide desde la posicion hacia arriba	
	//alert("hola")
	$(window).on("scroll", function(){
		if ($(window).scrollTop() > altura) {
			$("header").addClass('menufixed') //no ponemos punto			
		}else{
			$("header").removeClass('menufixed') //no ponemos punto

		}

	}); 
}
