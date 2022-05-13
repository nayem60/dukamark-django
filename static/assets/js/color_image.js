 function color(id,type){
     var color_id=$("#color").val()
     if(type==1)
     {
         var new_color=color_id.replace(color_id,'');
         var color_id=$("#color").val(new_color);
     }else{
         var color_id=$("#color").val(id);
         $("#color_form").submit();
         
     }
     
     $("#color_form").submit()
         
     
     
 }
 
 
 
 
 //====================size===========
 
 
 function size(id){
     var size=$("#size").val(id)
     $("#color_form").submit()
 }