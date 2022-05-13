{% extends 'layouts/base.py'%}

{% block content %}
   {% load static %}
    <!-- offcanvas area start -->
    <div class="offcanvas__area">
        <div class="offcanvas__wrapper">
        <div class="offcanvas__close">
            <button class="offcanvas__close-btn" id="offcanvas__close-btn">
                <i class="fal fa-times"></i>
            </button>
        </div>
        <div class="offcanvas__content">
            <div class="offcanvas__logo mb-40">
                <a href="index.html">
                <img src="{% static ''%}assets/img/logo/logo-white.png" alt="logo">
                </a>
            </div>
            <div class="offcanvas__search mb-25">
                <form action="#">
                    <input type="text" placeholder="What are you searching for?">
                    <button type="submit" ><i class="far fa-search"></i></button>
                </form>
            </div>
            <div class="mobile-menu fix"></div>
            <div class="offcanvas__action">

            </div>
        </div>
        </div>
    </div>
    <!-- offcanvas area end -->      
    <div class="body-overlay"></div>
    <!-- offcanvas area end -->

    <main>
        <!-- page-banner-area-start -->
        <div class="page-banner-area page-banner-height-2" data-background="{% static ''%}assets/img/banner/page-banner-4.jpg">
            <div class="container">
                <div class="row">
                    <div class="col-xl-12">
                        <div class="page-banner-content text-center">
                            <h4 class="breadcrumb-title">Checkout</h4>
                            <div class="breadcrumb-two">
                                <nav>
                                   <nav class="breadcrumb-trail breadcrumbs">
                                      <ul class="breadcrumb-menu">
                                         <li class="breadcrumb-trail">
                                            <a href="index.html"><span>Home</span></a>
                                         </li>
                                         <li class="trail-item">
                                            <span>Checkout</span>
                                         </li>
                                      </ul>
                                   </nav> 
                                </nav>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
      

        <!-- checkout-area-start -->
        <section class="checkout-area pb-85">
            <div class="container">
                <form action="{% url 'checkout' %}" method="post">
                {% csrf_token %}
                    <div class="row">
                        <div class="col-lg-6">
                            <div class="checkbox-form">
                                <h3>Billing Details</h3>
                                <div class="row">
                                    <div class="col-md-12">
                                        <div class="country-select">
                                            <label>Country <span class="required">*</span></label>
                                            <select style="display: none;" name="country">
                                                <option value="Bangladesh">Bangladesh</option>
                                                <option value="Algeria">Algeria</option>
                                                <option value="Afghanistan">Afghanistan</option>
                                                <option value="Ghana">Ghana</option>
                                                <option value="Albania">Albania</option>
                                                <option value="Bahrain">Bahrain</option>
                                                <option value="Colombia">Colombia</option>
                                                <option value="Dominican">Dominican Republic</option>
                                            </select><div class="nice-select" tabindex="0"><span class="current">bangladesh</span><ul class="list"><li data-value="volvo" class="option selected">bangladesh</li><li data-value="saab" class="option">Algeria</li><li data-value="mercedes" class="option">Afghanistan</li><li data-value="audi" class="option">Ghana</li><li data-value="audi2" class="option">Albania</li><li data-value="audi3" class="option">Bahrain</li><li data-value="audi4" class="option">Colombia</li><li data-value="audi5" class="option">Dominican Republic</li></ul></div>
                                        </div>
                                    </div>
                                    <div class="col-md-6">
                                        <div class="checkout-form-list">
                                            <label>First Name <span class="required">*</span></label>
                                            <input type="text" placeholder="" name="first_name">
                                        </div>
                                    </div>
                                    <div class="col-md-6">
                                        <div class="checkout-form-list">
                                            <label>Last Name <span class="required">*</span></label>
                                            <input type="text" placeholder=""name="last_name">
                                        </div>
                                    </div>
                                   
                                    <div class="col-md-12">
                                        <div class="checkout-form-list">
                                            <label>Address <span class="required">*</span></label>
                                            <input type="text" placeholder="Street address" name="address">
                                        </div>
                                    </div>
                                    
                                    
                                    <div class="col-md-12">
                                        <div class="checkout-form-list">
                                            <label>Town / City <span class="required">*</span></label>
                                            <input type="text" placeholder="Town / City" name="city">
                                        </div>
                                    </div>
                                    
                                    <div class="col-md-6">
                                        <div class="checkout-form-list">
                                            <label>Postcode / Zip <span class="required">*</span></label>
                                            <input type="number" class="form-control" placeholder="Postcode / Zip" name="zipcode">
                                        </div>
                                    </div>
                                    <div class="col-md-6">
                                        <div class="checkout-form-list">
                                            <label>Email Address <span class="required">*</span></label>
                                            <input type="email" placeholder="" name="email">
                                        </div>
                                    </div>
                                    <div class="col-md-6">
                                        <div class="checkout-form-list">
                                            <label>Phone <span class="required">*</span></label>
                                            <input type="number" class="form-control"placeholder="Phone" name="phone">
                                        </div>
                                    </div>
                                    
                                    </div>
                                </div>
                                <div class="different-address">
                                    <div class="ship-different-title">
                                        <h3>
                                            <label>Ship to a different address?</label>
                                            <input id="ship-box" name="ship_different"  value="1" type="checkbox">
                                        </h3>
                                    </div>
                                    <div id="ship-box-info">
                                        <div class="row">
                                            <div class="col-md-12">
                                                <div class="country-select">
                                                    <label>Country <span class="required">*</span></label>
                                                    <select style="display: none;">
                                                        <option value="volvo">bangladesh</option>
                                                        <option value="saab">Algeria</option>
                                                        <option value="mercedes">Afghanistan</option>
                                                        <option value="audi">Ghana</option>
                                                        <option value="audi2">Albania</option>
                                                        <option value="audi3">Bahrain</option>
                                                        <option value="audi4">Colombia</option>
                                                        <option value="audi5">Dominican Republic</option>
                                                    </select><div class="nice-select" tabindex="0"><span class="current">bangladesh</span><ul class="list"><li data-value="volvo" class="option selected">bangladesh</li><li data-value="saab" class="option">Algeria</li><li data-value="mercedes" class="option">Afghanistan</li><li data-value="audi" class="option">Ghana</li><li data-value="audi2" class="option">Albania</li><li data-value="audi3" class="option">Bahrain</li><li data-value="audi4" class="option">Colombia</li><li data-value="audi5" class="option">Dominican Republic</li></ul></div>
                                                </div>
                                            </div>
                                            <div class="col-md-6">
                                                <div class="checkout-form-list">
                                                    <label>First Name <span class="required">*</span></label>
                                                    <input type="text" placeholder="">
                                                </div>
                                            </div>
                                            <div class="col-md-6">
                                                <div class="checkout-form-list">
                                                    <label>Last Name <span class="required">*</span></label>
                                                    <input type="text" placeholder="">
                                                </div>
                                            </div>
                                           
                                            <div class="col-md-12">
                                                <div class="checkout-form-list">
                                                    <label>Address <span class="required">*</span></label>
                                                    <input type="text" placeholder="Street address">
                                                </div>
                                            </div>
                                            <div class="col-md-12">
                                                <div class="checkout-form-list">
                                                    <input type="text" placeholder="Apartment, suite, unit etc. (optional)">
                                                </div>
                                            </div>
                                            <div class="col-md-12">
                                                <div class="checkout-form-list">
                                                    <label>Town / City <span class="required">*</span></label>
                                                    <input type="text" placeholder="Town / City">
                                                </div>
                                            </div>
                                            <div class="col-md-6">
                                                <div class="checkout-form-list">
                                                    <label>State / County <span class="required">*</span></label>
                                                    <input type="text" placeholder="">
                                                </div>
                                            </div>
                                            <div class="col-md-6">
                                                <div class="checkout-form-list">
                                                    <label>Postcode / Zip <span class="required">*</span></label>
                                                    <input type="text" placeholder="Postcode / Zip">
                                                </div>
                                            </div>
                                            <div class="col-md-6">
                                                <div class="checkout-form-list">
                                                    <label>Email Address <span class="required">*</span></label>
                                                    <input type="email" placeholder="">
                                                </div>
                                            </div>
                                            <div class="col-md-6">
                                                <div class="checkout-form-list">
                                                    <label>Phone <span class="required">*</span></label>
                                                    <input type="text" placeholder="Postcode / Zip">
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="order-notes">
                                        <div class="checkout-form-list">
                                            <label>Order Notes</label>
                                            <textarea id="checkout-mess" name="ordernote" cols="30" rows="10" placeholder="Notes about your order, e.g. special notes for delivery."></textarea>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="col-lg-6">
                            <div class="your-order mb-30 ">
                                <h3>Your order</h3>
                                <div class="your-order-table table-responsive">
                                    <table>
                                        <thead>
                                            <tr>
                                                <th class="product-name">Product</th>
                                                <th class="product-total">Total</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                          {% for carts in cart  %}
                                            <tr class="cart_item">
                                                <td class="product-name">
                                                    {{ carts.product.name }} <strong class="product-quantity"> × {{ carts.quantity }}</strong>
                                                </td>
                                                <td class="product-total">
                                                {% if carts.variant %}
                                                    <span class="amount">${{ carts.variant_price_total }}</span>
                                                 {% else %}
                                                    <span class="amount">${{ carts.get_total }}</span>
                                                 {% endif %}
                                                </td>
                                            </tr>
                                            {% endfor %}
                                      
                                        </tbody>
                                        <tfoot>
                                            <tr class="cart-subtotal">
                                                <th>Cart Subtotal</th>
                                                <td><span class="amount">${{ totals }}</span></td>
                                            </tr>
                                            <tr class="shipping">
                                                <th>Shipping</th>
                                                <td>
                                                    <ul>
                                                        <li>
                                                            <input type="radio" name="shipping">
                                                            <label>
                                                                Flat Rate: <span class="amount">$7.00</span>
                                                            </label>
                                                        </li>
                                                        <li>
                                                            <input type="radio" name="shipping">
                                                            <label>Free Shipping:</label>
                                                        </li>
                                                    </ul>
                                                </td>
                                            </tr>
                                            {% if request.session.coupon_data %}
                                            <tr class="order-total">
                                                <th>Order Total</th>
                                                <td><strong><span class="amount">${{ subtotal }}</span></strong>
                                                </td>
                                            </tr>
                                            {% else %}
                                            <tr class="order-total">
                                                <th>Order Total</th>
                                                <td><strong><span class="amount">${{ totals }}</span></strong>
                                                </td>
                                            </tr>
                                            {% endif %}
                                        </tfoot>
                                    </table>
                                </div>
                                <select class="form-control" id="payment" name='payment'>
                                     <option value="cod">Cash On Delivery</option>
                                     <option {% if payment == 'paypal' %} selected {% endif%}value="paypal">PayPal</option>
                                     <option value="sslcommerz">SSLCommerz</option>
                                     <option  value="">rezorpy{{ request.session.order_id}}</option>
                                     <option value="">Stripe</option>
                                 </select><br></br>
                                    
                                    </div>
                                    </div>
                                    {% if payment == 'paypal' %}
                                       <div id="paypal-button-container"style="width:30%; height:30%; margin:auto; "></div>
                                    {% else %}
                                    
                            
                                    <div class="order-button-payment mt-20">
                                    <button type="submit" class="tp-btn-h1">Place order</button>
                                    </div>
                                    {% endif %}
                                </div>
                            </div>
                        </div>
                    </div>
                </form>
            </div>
        </section>
        <!-- checkout-area-end -->

        <!-- cta-area-start -->
        <section class="cta-area d-ldark-bg pt-55 pb-10">
            <div class="container">
                <div class="row">
                    <div class="col-lg-4 col-md-6">
                        <div class="cta-item cta-item-d mb-30">
                            <h5 class="cta-title">Follow Us</h5>
                            <p>We make consolidating, marketing and tracking your social media website easy.</p>
                            <div class="cta-social">
                                <div class="social-icon">
                                    <a href="#" class="facebook"><i class="fab fa-facebook-f"></i></a>
                                    <a href="#" class="twitter"><i class="fab fa-twitter"></i></a>
                                    <a href="#" class="youtube"><i class="fab fa-youtube"></i></a>
                                    <a href="#" class="linkedin"><i class="fab fa-linkedin-in"></i></a>
                                    <a href="#" class="rss"><i class="fas fa-rss"></i></a>
                                    <a href="#" class="dribbble"><i class="fab fa-dribbble"></i></a>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-4 col-md-6">
                        <div class="cta-item mb-30">
                            <h5 class="cta-title">Sign Up To Newsletter</h5>
                            <p>Join 60.000+ subscribers and get a new discount coupon  on every Saturday.</p>
                            <div class="subscribe__form">
                                <form action="#">
                                    <input type="email" placeholder="Enter your email here...">
                                    <button>subscribe</button>
                                </form>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-4 col-md-6">
                        <div class="cta-item mb-30">
                            <h5 class="cta-title">Download App</h5>
                            <p>DukaMarket App is now available on App Store & Google Play. Get it now.</p>
                            <div class="cta-apps">
                                <div class="apps-store">
                                    <a href="#"><img src="assets/img/brand/app_ios.png" alt=""></a>
                                    <a href="#"><img src="assets/img/brand/app_android.png" alt=""></a>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

        </section>
        <!-- cta-area-end -->

    </main>
    {% block script %}
      <script
		      src="https://www.paypal.com/sdk/js?client-id=AVHPLusmJMvUhLJSIySJf7Y5AwhZuGDMX0fH5KwpRLXUogEDWGZQE7c1rFR-BJi0JKH5pVrzO4bBCOrC">
	     </script>
	     
       <script>
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
       var csrftoken=getCookie('csrftoken');
       var url="{% url 'paypal' %}"
       
       
       
       paypal.Buttons({
          createOrder: function(data, actions) {
             return actions.order.create({
               purchase_units: [{
                   amount: {
                     value: {{totals}}
                   }
               }]
               
             });
          },
          
           
        onApprove: function(data, actions) {
          return actions.order.capture().then(function(details){
            console.log(details);
			         sendData();
			         function sendData(){
			           fetch(url, {
			              method: "POST",
					            headers: {
						             'Content-type': "application/json",
						             'X-CSRFToken': csrftoken
					            },
					            body: JSON.stringify({
					              'order_id': details.id,
					              'payment_id':details.payer.payer_id,
						             'status': details.status
						               
					            })
					            
					            
			           })
			             
			         }
			         
          })
        
        }
           
           
       }).render('#paypal-button-container');
       
       </script>
       
      
       
       
    {% endblock %}
 

 {% endblock %}
