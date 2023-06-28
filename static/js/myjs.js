// function showname () {
//     var name = document.getElementById('file-upload'); 
//     alert('Selected file: ' + name.files.item(0).name);
//     alert('Selected file: ' + name.files.item(0).size);
//     alert('Selected file: ' + name.files.item(0).type);
//   };

function GetFileSizeNameAndType()
    {
    var fi = document.getElementById('file-upload'); // GET THE FILE INPUT AS VARIABLE.

    var totalFileSize = 0;

    // VALIDATE OR CHECK IF ANY FILE IS SELECTED.
    if (fi.files.length > 0)
    {
        // RUN A LOOP TO CHECK EACH SELECTED FILE.
        for (var i = 0; i <= fi.files.length - 1; i++)
        {
            //ACCESS THE SIZE PROPERTY OF THE ITEM OBJECT IN FILES COLLECTION. IN THIS WAY ALSO GET OTHER PROPERTIES LIKE FILENAME AND FILETYPE
            var fsize = fi.files.item(i).size;
            totalFileSize = totalFileSize + fsize;
            document.getElementById('fp').innerHTML =
            document.getElementById('fp').innerHTML
            +
            '<br /> ' + 'File Name is <b>' + fi.files.item(i).name
            +
            '</b> and Size is <b>' + Math.round((fsize / 1024)) //DEFAULT SIZE IS IN BYTES SO WE DIVIDING BY 1024 TO CONVERT IT IN KB
            +
            '</b> KB and File Type is <b>' + fi.files.item(i).type + "</b>.";
        }
    }
    document.getElementById('divTotalSize').innerHTML = "Total File(s) Size is <b>" + Math.round(totalFileSize / 1024) + "</b> KB";
}




function myFunction() {
    var element = document.getElementById("accountSection");
    element.classList.toggle("active");
 }

 $('.messege-info').hide().fadeIn(500).delay(2000).fadeOut(500);  


 $(document).ready(function(){
    $("select").change(function(){
        $(this).find("option:selected").each(function(){
            var optionValue = $(this).attr("value");
            if(optionValue){
                $(".box").not("." + optionValue).hide();
                $("." + optionValue).show();
            } else{
                $(".box").hide();
            }
        });
    }).change();
  });