function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


jQuery(function ($){
    $(document).ready(function(){
    $("#id_category").change(function(){
       var category_id=$(this).val()
       $.ajax({
           url:'/category/',
           type:'POST',
           headers: {"X-CSRFToken": getCookie("csrftoken")},
           data:{category:category_id},
           success:function(data){
              console.log(data)
              sub_id=document.getElementById("id_subcategory");
              sub_id.options.length=0;
              sub_id.options.add(new Option("Choice One","Choice One"));
              for(var sub in data){
                  sub_id.options.add(new Option(sub,data[sub]));
              }
           },
           error:function (e){
               console.error("error")
           }
           
       });
        
     });
    
  });
    
});





jQuery(function ($){
    $(document).ready(function(){
        $('#id_subcategory').change(function (){
            var Id=$(this).val()
            $.ajax({
                url:'/subcategory/',
                type:'POST',
                headers: {"X-CSRFToken": getCookie("csrftoken")},
                data:{subcategory:Id},
                success:function (data){
                   sub_child=document.getElementById("id_subcategory_child");
                   sub_child.options.length=0;
                   sub_child.options.add(new Option('Choose One',''));
                   
                   for(var p in data){
                       sub_child.options.add(new Option(p,data[p]));
                   }
                },
                error:function (e){
                    console.error("error")
                }
                   
            });
        });
    })
});