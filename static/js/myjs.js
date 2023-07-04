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
        var fsize = fi.files.item(0).size;
        totalFileSize = totalFileSize + fsize;
    }
    document.getElementById('divTotalSize').innerHTML ='<br /> ' + 'File Name is <b>' + fi.files.item(0).name + "</b> Total File(s) Size is <b>" + Math.round(totalFileSize / 1024) + "</b> KB" +'</b> and File Type is <b>' + fi.files.item(0).type + "</b>.";
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



  $("input[type='radio']").change(function(){
   
    if($(this).val()=="2")
    {
        $("#Reason").show();
    }
    else
    {
           $("#Reason").hide(); 
    }
        
    });