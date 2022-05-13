function colors(id,type){
    var color=$('.color').val()
    if(type==1){
        var new_color=color.replace(id+':','')
        var color=$('.color').val(new_color)
    }else{
        $('.color').val(id+':'+color)
        $("#color_form").submit ()
    }
    $("#color_form").submit ()
        
    
}


function subcategoryChild(id,type){
         var sub_id=$('.sub_id').val()
         if(type==1){
             var newId=sub_id.replace(id+':','')
             var sub_id=$('.sub_id').val(newId)
         }else{
             $('.sub_id').val(id+':'+sub_id)
             $('#subForm').submit()
         }
             
         $('#subForm').submit()
    
}