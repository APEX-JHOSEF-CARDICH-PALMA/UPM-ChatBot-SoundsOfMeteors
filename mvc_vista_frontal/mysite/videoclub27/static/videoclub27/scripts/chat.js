$(document).ready(function () {
	
	$("#boton-chat").click(function(){
		base = "http://localhost";
		texto = $("#texto").val();

			$("#cuadrochat").append("<div id='mensaje-user'> <p align=\"right\">" + texto + "</p></div>")

		content = {
			  "sender": "Rasa","message": texto

		};
		$.ajax({
					url:   base + ":5005/webhooks/rest/webhook",
					contentType: 'application/json',
					data: JSON.stringify(content),
					type: 'POST',
					success: function (data) {
						
						receive =" nada ";
						$.each(data, function (key, val) {
							if(val.custom != undefined){
								if(val.custom.soundUri != undefined)
								receive = "<audio controls autoplay><source src=\""+base + ":8000"+"/sonidos/"+val.custom.soundUri+"\" type=\"audio/wav\"></audio>";
							}else{
								receive = "<div id='mensaje-bot'>" + val.text+"</div></br>";
							}


							$("#cuadrochat").append(receive);
						});
						
						
					}
				});
	});
});
