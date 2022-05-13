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





function increment(id){
    var quantity=$("#cart_qty").val();
    $.ajax({
        url:'/increment/'+id,
        type:'POST',
        data:{quantity:quantity},
        headers: {"X-CSRFToken": getCookie("csrftoken")},
        success:function (data){
            $(".reload").load(location.href + " .reload");
        }
    });
}
function decrement(id){
    var quantity=$("#cart_qty").val();
}


function remove (id){
    $.ajax({
        url:'/remove/'+id,
        type:'POST',
        headers: {"X-CSRFToken": getCookie("csrftoken")},
        success: function (data){
            $(".reload").load(location.href + " .reload");
        }
    });
}



function coupon_remove(){
    alert('hi')
}
  