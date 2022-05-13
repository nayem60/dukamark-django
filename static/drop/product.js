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
////// Get Brand//////////
jQuery(function($){
 $(document).ready(function(){
    $('#id_subcategory').change(function(){
        var subcategory_id=$(this).val()
        $.ajax({
            url:'/brand/',
            type:'POST',
            data:{subcategory:subcategory_id},
            headers: {"X-CSRFToken": getCookie("csrftoken")},
            success:function (data){
                brand=document.getElementById('id_brand');
                brand.options.length=0;
                brand.options.add(new Option('Choice Brand',''))
                for(var p in data){
                    brand.options.add(new Option(p ,data[p]))
                }
            }
            
        });
        
    });
    
    ////Get subcategory 
      $("#id_category").change(function (){
            var category=$(this).val()
            $.ajax({
                url:"/category/",
                type:"POST",
                data:{category:category},
                headers: {"X-CSRFToken": getCookie("csrftoken")},
                success:function (data){
                    sub=document.getElementById('id_subcategory');
                    sub.options.length=0;
                    sub.options.add(new Option('Choice Subcategory','Choice Subcategory'));
                    
                    for (var k in data){
                        sub.options.add(new Option(k,data[k]));
                    }
                }
            });
            
            
        });
  
  
  });
   
});









