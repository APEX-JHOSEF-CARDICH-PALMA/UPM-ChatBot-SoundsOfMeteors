$(document).ready(function () {
	
	$("#boton-chat").click(function(){
		base = "http://localhost";
		texto = $("#texto").val();

			$("#cuadrochat").append("</br><div class= 'text-right p-1 mb-1 bg-success text-white' id='message-user'> <p>" + texto + "</p></div>")

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
								receive = "</br><div class= 'text-left p-1 mb-1 bg-primary text-white' id='message-bot'> <p>" + val.text+"</p></div>";
							}


							$("#cuadrochat").append(receive);
						});
						
						
					}
				});
	});
});
