var fso = new ActiveXObject("Scripting.FileSystemObject");

var Path = "./image";

var folder = fso.getFolder(Path);
var folderName = new Enumerator(folder.SubFolders);

var files = "";
for(; !folderName.atEnd(); folderName.moveNext()){
	var Subpath = Path + '/' + folderName.item().Name;
	var Subfolder = fso.getFolder(Subpath);
	var fileName = new Enumerator(Subfolder.files);

	for(; !fileName.atEnd(); fileName.moveNext()){
		files += fileName.item().Name;
	}	
}
fso = null;

WScript.Echo(files);
