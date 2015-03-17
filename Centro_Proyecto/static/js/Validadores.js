
 function validarNumeros(e) { // 1
    tecla = (document.all) ? e.keyCode : e.which; // 2
    if (tecla==8) return true; 
    if (tecla==9) return true; // backspace
    //if (tecla==189) return true; // guion
    if (tecla==46) return true; // delete  
    //if (tecla==9) return true; // tab
    if (tecla==37) return true; // izquierda
   if (e.ctrlKey && tecla==86) { 
    return true
    }; //Ctrl v
    if (e.ctrlKey && tecla==67) { 
    return true
    }; //Ctrl c
    if (e.ctrlKey && tecla==88) {
     return true}; //Ctrl x
    
    //if (tecla>=96 && tecla<=105) { return true;} //numpad
 
    patron = /[0-9]/; // patron
 
    te = String.fromCharCode(tecla); 
    return patron.test(te); // prueba
  }
 
 function validarLetras(e) { // 1
    tecla = (document.all) ? e.keyCode : e.which; 
    if (tecla==8) return true; // backspace
    if (tecla==32) return true; // espacio
    if (tecla==46) return true; // delete
    if (tecla==16) return true; // delete
    if (tecla==9) return true; // delete
    if (tecla==37) return true; // izquierda
    if (tecla==37) return true; // derecha
    
    
    if (e.ctrlKey && tecla==86) { return true;} //Ctrl v
    if (e.ctrlKey && tecla==67) { return true;} //Ctrl c
    if (e.ctrlKey && tecla==88) { return true;} //Ctrl x
 
    patron = /[a-zA-Z]/; //patron
 
    te = String.fromCharCode(tecla); 
    return patron.test(te); // prueba de patron
  }   
  
  


$(document).ready(function(){
	
	$("#cedula").validarCedulaEC({
 	 	onInvalid: function () {
    	alert("cédula inválida.");
    	console.log(this);
    	

  }

});

   // $(".eliminar_Pac").on('click',alert("Esta seguro que desea Eliminar el Paciente"))




})
