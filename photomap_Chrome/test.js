var fileinfo = inputradio = labelimg = sampleimg = "";

function fileListDirectory(files){
	for (i=0; i<files.length; i++){
		fileinfo = '<img src="./' + files[i].webkitRelativePath + '">';
		inputradio += '<input type="radio" id="p' + i + '">';
		labelimg += '<label for="p' + i + '">' + fileinfo + '</label>';
		sampleimg += '<div class="pickup" id="pic' + i + '">' + fileinfo + '</div>';
	}
	document.getElementById('inputradio').innerHTML = inputradio;
	document.getElementById('labelimg').innerHTML = labelimg;
	document.getElementById('sampleimg').innerHTML = sampleimg;
}