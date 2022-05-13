//csrf token

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







// size=========
function size(sizeId,variantId){
    $("#variant").val(variantId)
    $('.choose-color').hide();
    $('.size-link').show();
    $('.size_'+sizeId).show();
    $('.size-link').css('color','black')
    $('#size_'+sizeId).css('color','red');
    var price=$('#size_'+sizeId).data('price');
    $('.price').html('<span>$'+price+'</span>');
}
   
  
//color===========
function color(colorId, variantId){
   $("#variant").val(variantId)
   $('.size-link').hide();
   $('.choose-color').show();
   $('.color_'+colorId).show();
   $('.color-link').css('color','black');
   $('#color_'+colorId).css('color','red');
   var price=$('#color_'+colorId).data('prices');
   $('.price').html('<span>$'+price+'</span>');
   
}


//add to cart==========


function addCart(productId){
    var quantity=$("#quantity").val();
    var variant=$("#variant").val()
        $.ajax({
            url:'/add-cart/'+productId,
            headers: {"X-CSRFToken": getCookie("csrftoken")},
            data:{variant:variant,quantity:quantity},
            type:"POST",
            success: function (data){
                console.log(data)
                $(".reload").load(location.href + " .reload");
            }
        })
    
        
    
    
}
 
  