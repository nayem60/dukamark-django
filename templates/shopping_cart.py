{% extends 'layouts/base.py' %}
  {% block content %}


    <main class="reload">
      

        <!-- cart-area-start -->
        <section class="cart-area pt-100 pb-120 " id="reload">
            <div class="container">
               <div class="row">
                  <div class="col-12">
                        <form action="#">
                           <div class="table-content table-responsive">
                              <table class="table">
                                    <thead>
                                       <tr>
                                          <th class="product-thumbnail">Images</th>
                                          <th class="cart-product-name">Product</th>
                                          <th class="cart-product-name">Variant</th>
                                          <th class="product-price">Unit Price</th>
                                          <th class="product-quantity">Quantity</th>
                                          <th class="product-subtotal">Total</th>
                                          <th class="product-remove">Remove</th>
                                       </tr>
                                    </thead>
                                    <tbody>
                               
                                    {% for carts in cart %}
                                         
                                       <tr>
                                          <td class="product-thumbnail"><a href="shop-details.html"><img src="{{ carts.product.image.url }}" alt=""></a></td>
                                          <td class="product-name"><a href="shop-details.html">{{ carts.product.name|truncatewords:3 }}</a></td>
                                          <td class="product-name"><a href="shop-details.html">
                                          {% if carts.variant %} 
                                             {% if carts.variant.color and carts.variant.size %}
                                                color:{{ carts.variant.color }}
                                                size:{{ carts.variant.size }} 
                                                
                                             {% elif carts.variant.color %}
                                                color:{{ carts.variant.color }}
                                                
                                              {% else %}
                                                size:{{ carts.variant.size }}
                                              
                                             {% endif %}
                                          {% endif %}</a></td>
                                 
                                          <td class="product-price"><span class="amount">{% if carts.variant.price %} V{{ carts.variant.price }} {% elif carts.product.regular_discount_price %} ${{ carts.product.regular_discount_price }} {% else %} ${{ carts.product.price }} {% endif %}</span></td>
                                          
                                          <td class="product-quantity">
                                          <div class="cart-plus-minus"><input type="text" id="cart_qty" value="{{ carts.quantity }}" readonly ><div onclick="decrement({{ carts.id }})" class="dec qtybutton" >-</div><div onclick="increment({{ carts.id }})" id="increment" class="inc qtybutton" id="qtybuttons">+</div></div>
                                          </td>
                                          <td class="product-subtotal"><span class="amount">{% if carts.variant %} ${{ carts.variant_price_total }} {% else %} ${{ carts.get_total }}  {% endif %}</span></td>
                                          <td class="product-remove"><a href="javascript:void(0)" onclick="remove({{ carts.id }})"><i class="fa fa-times"></i></a></td>
                                     
                                         </tr>
                                         {% empty %}
                                         <h2 class="text-center p-5"> Not Found Product </h2>                                
                               
                                       
                                    {% endfor %}
                                    </tbody>
                              </table>
                           </div>
                           {% if not request.session.coupon_data %}
                           <div class="row">
                              <div class="col-12">
                                    <div class="coupon-all">
                                       <div class="coupon">
                                       <form action="">
                                        <input id="coupon_code" class="input-text" name="code" value="" placeholder="Coupon code" type="text">
                                          <button class="tp-btn-h1" type="submit">Apply
                                                coupon</button>
                                       </div>
                                       
                                       </form>
                                    </div>
                              </div>
                           </div>
                           {% endif %}
                           <div class="row justify-content-end">
                              <div class="col-md-5">
                                    <div class="cart-page-total">
                                       <h2>Cart totals</h2>
                                       <ul class="mb-20">
                                          <li>Subtotal <span>${{ totals }}</span></li>
                                          {% if request.session.coupon_data %}
                                          <li>discount <span>- ${{ discount }}</span><a href="javascript:void(0)" onclick="coupon_remove()" style="font-size:20px; color:red;"><i class="fa fa-times"></i></a></li>
                                          <li>Total <span>${{ subtotal }}</span></li>
                                          {% else %}
                                          <li>Total <span>${{ totals }}</span></li>
                                          {% endif %}
                                       </ul>
                                       <a class="tp-btn-h1" href="{% url 'checkout' %}">Proceed to checkout</a>
                                    </div>
                              </div>
                           </div>
                        </form>
                  </div>
               </div>
            </div>
         </section>
         <!-- cart-area-end -->

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

  {% endblock %}
