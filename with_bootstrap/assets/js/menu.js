//menu
$(function(){
	var boton = $('#btn-menu');
	var fondo_enlace = $('#fondo-enlace');

	boton.on('click', function(e){
		fondo_enlace.toggleClass('active');
		$('#barra-lateral-izquierda').toggleClass('active');
		e.preventDefault();
	});

	fondo_enlace.on('click', function(e){
		fondo_enlace.toggleClass('active');
		$('#barra-lateral-izquierda').toggleClass('active');
		e.preventDefault();
	});
}())

//Multiselec
$(document).ready(function(){
	var content = [
		{ id: 0, text: "Programador senior", 
		email: "Desarrollo de software" },
		{ id: 1, text: "Técnico de máquina ", email: "Servicio técnico" },
		{ id: 2, text: "Contaduría general  ", email: "Administración" },
		{ id: 3, text: "Contaduría general  ", email: "Administración" },
		{ id: 4, text: "Contaduría general  ", email: "Administración" },
		{ id: 5, text: "Contaduría general  ", email: "Administración" },
		{ id: 6, text: "Contaduría general  ", email: "Administración" },
		{ id: 7, text: "Contaduría general  ", email: "Administración" },
		{ id: 8, text: "Contaduría general  ", email: "Administración" },
		{ id: 9, text: "Contaduría general  ", email: "Administración" },
		{ id: 10, text: "Contaduría general  ", email: "Administración" },
		{ id: 11, text: "Contaduría general  ", email: "Administración" }
	];


	$(".prompt").select2({
		data: content,
		// minimumInputLength: 2,
		width: '100%',
		multiple: true,
		placeholder: "Cargos Proinso sa",
		// templateResult:formatState
	});	
			
});
function btnHandler() {
	var names = $('.prompt').select2('data');
	for (let name of names) {
		console.log(name);
		console.log(name.text);
		console.log(name.email);
		alert(`${name.text} - ${name.email}`);
	}
}
