var fileinfo = inputradio = labelimg = sampleimg = "";

var fso = new ActiveXObject("Scripting.FileSystemObject");

var Path = "./image";

var folder = fso.getFolder(Path);
var folderName = new Enumerator(folder.SubFolders);

var files = "";
var i = 0;
for(; !folderName.atEnd(); folderName.moveNext()){
	var Subpath = Path + '/' + folderName.item().Name;
	var Subfolder = fso.getFolder(Subpath);
	var fileName = new Enumerator(Subfolder.files);

	for(; !fileName.atEnd(); fileName.moveNext()){
		files = fileName.item().Name;
		fileinfo = '<img src="' + Subpath + '/' + files + '">';
		inputradio += '<input type="radio" id="p' + i + '">';
		labelimg += '<label for="p' + i + '">' + fileinfo + '</label>';
		sampleimg += '<div class="pickup" id="pic' + i + '">' + fileinfo + '</div>';
		i++;
	}	
}
fso = null;

document.getElementById('inputradio').innerHTML = inputradio;
document.getElementById('labelimg').innerHTML = labelimg;
document.getElementById('sampleimg').innerHTML = sampleimg;

