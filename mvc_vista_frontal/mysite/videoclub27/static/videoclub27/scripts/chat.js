$(document).ready(function () {
	
	$("#boton-chat").click(function(){
		base = "http://localhost";
		texto = $("#texto-box").val();

			$("#cuadro-chat").append("</br><div class= 'text-right p-1 mb-1 bg-warning text-black font-weight-bold' id='burbuja-user'> <p>" + texto + "</p></div>")

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
								receive = "<audio id='sound-control' controls autoplay><source src=\""+base + ":8000"+"/sonidos/"+val.custom.soundUri+"\" type=\"audio/wav\"></audio>";
							}else{
								receive = "</br><div class= 'text-left p-1 mb-1 bg-primary text-white font-weight-bold' id='burbuja-bot'> <p>" + val.text+"</p></div>";
							}


							$("#cuadro-chat").append(receive);
						});
						
						
					}
				});
	});
});
