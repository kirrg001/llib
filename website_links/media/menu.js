//document.getElementById(window.event.srcElement.id);

function init_text(){
	
	var elements = document.body.getElementsByClassName('can');
	
	for (var e in elements){
		var can = document.getElementById(elements[e].id);

		if (can.getContext) {
    		var ctx = can.getContext('2d');

	    	ctx.fillStyle = 'black';
    		ctx.font = 'italic 30px sans-serif';
    		ctx.textBaseline = 'top';
    		ctx.fillText(elements[e].id, 50, 50);
		}	
	}
}



function mouseDown(){

	var src = document.getElementById(window.event.srcElement.id);
	var cont = document.getElementById('content');

	//reset content container
	$( "#content" ).css({ width: 0});
	
	if(src.id == 'flinks')
		cont.style.backgroundColor = 'red'; 
	else if(src.id == 'ylinks')
		cont.style.backgroundColor = 'blue'; 
	else if(src.id == 'playlists')
		cont.style.backgroundColor = 'yellow';
	else if(src.id == 'slinks') 
		cont.style.backgroundColor = 'white';
		

	$( "#content" ).animate( { width: "90%"}, { queue: false, duration: 1500 });

}


window.onload = init_text;
