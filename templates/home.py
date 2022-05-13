{%extends 'layouts/base.py'%}

{%block content%}
    
  {% load static %}

   
   {% include 'slider.py' %}
        <!-- features__area-start -->
        <section class="features__area pt-20">
            <div class="container">
                <div class="row row-cols-xxl-4 row-cols-xl-4 row-cols-lg-4 row-cols-md-2 row-cols-sm-2 row-cols-1 gx-0">
                    <div class="col">
                        <div class="features__item d-flex white-bg">
                            <div class="features__icon mr-20">
                                <i class="fal fa-truck"></i>
                            </div>
                            <div class="features__content">
                                <h6>FREE DELIVERY</h6>
                                <p>For all orders over $120</p>
                            </div>
                        </div>
                    </div>
                    <div class="col">
                        <div class="features__item d-flex white-bg">
                            <div class="features__icon mr-20">
                                <i class="fal fa-money-check"></i>
                            </div>
                            <div class="features__content">
                                <h6>SAFE PAYMENT</h6>
                                <p>100% secure payment</p>
                            </div>
                        </div>
                    </div>
                    <div class="col">
                        <div class="features__item d-flex white-bg">
                            <div class="features__icon mr-20">
                                <i class="fal fa-comments-alt"></i>
                            </div>
                            <div class="features__content">
                                <h6>24/7 HELP CENTER</h6>
                                <p>Delicated 24/7 support</p>
                            </div>
                        </div>
                    </div>
                    <div class="col">
                        <div class="features__item features__item-last d-flex white-bg">
                            <div class="features__icon mr-20">
                                <i class="fad fa-user-headset"></i>
                            </div>
                            <div class="features__content">
                                <h6>FRIENDLY SERVICES</h6>
                                <p>30 day satisfaction guarantee</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <!-- features__area-end -->

        <!-- banner__area-start -->
        <section class="banner__area pt-20 pb-10">
            <div class="container">
                <div class="row">
                {% for sliders in slider%}
                    <div class="col-xl-4 col-lg-4 col-md-6">
                        <div class="banner__item p-relative w-img mb-30">
                            <div class="banner__img">
                                <a href="product-details.html"><img src="{{ sliders.image.url }}" alt=""></a>
                            </div>
                            <div class="banner__content">
                                <h6><a href="product-details.html">Intelligent <br> New Touch Control</a></h6>
                                <p>Discount  20% On Products</p>
                            </div>
                        </div>
                    </div>
                 {% endfor %}
                    
                </div>
            </div>
        </section>
        <!-- banner__area-end -->
      {% if flasProduct and flasSale %}
        <!-- topsell__area-start -->
        <section class="topsell__area-1 pt-15">
            <div class="container">
                <div class="row">
                    <div class="col-xl-12">
                        <div class="section__head d-flex justify-content-between mb-10">
                            <div class="section__title">
                                <h5 class="st-titile-d">Top Deals Of The Day</h5>
                            </div>
                            <div class="offer-time">
                                <span class="offer-title d-none d-sm-block">Hurry Up! Offer ends in:</span>
                                <div class="countdown">
                                    <div class="countdown-inner b-radius" data-countdown="" data-date="{{ flasSale.flash_date|date:'Y/m/d'}}">
                                        <ul class="text-center">
                                            <li><span data-days="">0</span> Days</li>
                                            <li><span data-hours="">0</span> Hours</li>
                                            <li><span data-minutes="">00</span> Mins</li>
                                            <li><span data-seconds="">00</span> Secs</li>
                                        </ul>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="row">
                    <div class="product-bs-slider">
                        <div class="product-slider swiper-container">
                            <div class="swiper-wrapper">
                            {% for flash_products in flasProduct %}
                                <div class="product__item swiper-slide">
                                    <div class="product__thumb fix">
                                        <div class="product-image w-img">
                                            <a href="product-details.html">
                                                <img src="{{ flash_products.image.url }}" alt="product">
                                            </a>
                                        </div>
                                        <div class="product__offer">
                                        <span class="discount">-15%</span>
                                        </div>
                                        <div class="product-action">
                                            <a href="#" class="icon-box icon-box-1" data-bs-toggle="modal" data-bs-target="#productModalId">
                                                <i class="fal fa-eye"></i>
                                                <i class="fal fa-eye"></i>
                                            </a>
                                            <a href="#" class="icon-box icon-box-1">
                                                <i class="fal fa-heart"></i>
                                                <i class="fal fa-heart"></i>
                                            </a>
                                            <a href="#" class="icon-box icon-box-1">
                                                <i class="fal fa-layer-group"></i>
                                                <i class="fal fa-layer-group"></i>
                                            </a>
                                        </div>
                                    </div>
                                    <div class="product__content">
                                        <h6><a href="product-details.html">{{ flash_products.name }}</a></h6>
                                        <div class="rating mb-5">
                                            <ul>
                                                <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                <li><a href="#"><i class="fal fa-star"></i></a></li>
                                            </ul>
                                            <span>(01 review)</span>
                                        </div>
                                        <div class="price mb-10">
                                            <span>$105-$110</span>
                                        </div>
                                        <div class="progress mb-5">
                                            <div class="progress-bar bg-danger" role="progressbar" style="width: 10%" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100"></div>
                                        </div>
                                        <div class="progress-rate">
                                            <span>Sold:312/{{ flash_products.quantity }}</span>
                                        </div>
                                    </div>
                                    <div class="product__add-cart text-center">
                                        <button type="button" class="cart-btn product-modal-sidebar-open-btn d-flex align-items-center justify-content-center w-100">
                                        Add to Cart
                                        </button>
                                    </div>
                                </div>
                              {% endfor %}
                            </div>
                        </div>
                        <!-- If we need navigation buttons -->
                        <div class="bs-button bs-button-prev"><i class="fal fa-chevron-left"></i></div>
                        <div class="bs-button bs-button-next"><i class="fal fa-chevron-right"></i></div>
                    </div>
                </div>
            </div>
        </section>
        <!-- topsell__area-end -->
      {% endif %}

        <!-- banner__area-start -->
      

        <!-- topsell__area-start -->
        <section class="topsell__area-2 pt-15">
            <div class="container">
                <div class="row">
                    <div class="col-xl-12">
                        <div class="section__head d-flex justify-content-between mb-10">
                            <div class="section__title">
                                <h5 class="st-titile">Top Selling Products</h5>
                            </div>
                            <div class="product__nav-tab"> 
                                <ul class="nav nav-tabs" id="flast-sell-tab" role="tablist">
                                    <li class="nav-item" role="presentation">
                                      <button class="nav-link active" id="computer-tab" data-bs-toggle="tab" data-bs-target="#computer" type="button" role="tab" aria-controls="computer" aria-selected="false">computer</button>
                                    </li>
                                    <li class="nav-item" role="presentation">
                                      <button class="nav-link" id="samsung-tab" data-bs-toggle="tab" data-bs-target="#samsung" type="button" role="tab" aria-selected="false">samsung</button>
                                    </li>
                                    <li class="nav-item" role="presentation">
                                      <button class="nav-link" id="htc-tab" data-bs-toggle="tab" data-bs-target="#htc" type="button" role="tab" aria-selected="false">HTC</button>
                                    </li>
                                    <li class="nav-item" role="presentation">
                                      <button class="nav-link" id="nokia-tab" data-bs-toggle="tab" data-bs-target="#nokia" type="button" role="tab" aria-selected="false">Nokia</button>
                                    </li>
                                    <li class="nav-item" role="presentation">
                                      <button class="nav-link" id="cell-tab" data-bs-toggle="tab" data-bs-target="#cell" type="button" role="tab" aria-selected="true">Cell Phones</button>
                                    </li>
                                  </ul>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="row">
                    <div class="col-xl-12">
                        <div class="tab-content" id="flast-sell-tabContent">
                            <div class="tab-pane fade active show" id="computer" role="tabpanel" aria-labelledby="computer-tab">
                                <div class="product-bs-slider-2">
                                    <div class="product-slider-2 swiper-container">
                                        <div class="swiper-wrapper">
                                            <div class="product__item swiper-slide">
                                                <div class="product__thumb fix">
                                                    <div class="product-image w-img">
                                                        <a href="product-details.html">
                                                            <img src="{% static ''%}assets/img/product/tp-1.jpg" alt="product">
                                                        </a>
                                                    </div>
                                                    <div class="product__offer">
                                                    <span class="discount">-15%</span>
                                                    </div>
                                                    <div class="product-action">
                                                        <a href="#" class="icon-box icon-box-1" data-bs-toggle="modal" data-bs-target="#productModalId">
                                                            <i class="fal fa-eye"></i>
                                                            <i class="fal fa-eye"></i>
                                                        </a>
                                                        <a href="#" class="icon-box icon-box-1">
                                                            <i class="fal fa-heart"></i>
                                                            <i class="fal fa-heart"></i>
                                                        </a>
                                                        <a href="#" class="icon-box icon-box-1">
                                                            <i class="fal fa-layer-group"></i>
                                                            <i class="fal fa-layer-group"></i>
                                                        </a>
                                                    </div>
                                                </div>
                                                <div class="product__content">
                                                    <h6><a href="product-details.html">Epple iPad Pro 10.5-inch Cellular 64G</a></h6>
                                                    <div class="rating mb-5">
                                                        <ul>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                        </ul>
                                                        <span>(01 review)</span>
                                                    </div>
                                                    <div class="price">
                                                        <span>$105-$110</span>
                                                    </div>
                                                </div>
                                                <div class="product__add-cart text-center">
                                                    <button type="button" class="cart-btn product-modal-sidebar-open-btn d-flex align-items-center justify-content-center w-100">
                                                    Add to Cart
                                                    </button>
                                                </div>
                                            </div>
                                            <div class="product__item swiper-slide">
                                                <div class="product__thumb fix">
                                                    <div class="product-image w-img">
                                                        <a href="product-details.html">
                                                            <img src="{% static ''%}assets/img/product/tp-2.jpg" alt="product">
                                                        </a>
                                                    </div>
                                                    <div class="product-action">
                                                        <a href="#" class="icon-box icon-box-1" data-bs-toggle="modal" data-bs-target="#productModalId">
                                                            <i class="fal fa-eye"></i>
                                                            <i class="fal fa-eye"></i>
                                                        </a>
                                                        <a href="#" class="icon-box icon-box-1">
                                                            <i class="fal fa-heart"></i>
                                                            <i class="fal fa-heart"></i>
                                                        </a>
                                                        <a href="#" class="icon-box icon-box-1">
                                                            <i class="fal fa-layer-group"></i>
                                                            <i class="fal fa-layer-group"></i>
                                                        </a>
                                                    </div>
                                                </div>
                                                <div class="product__content">
                                                    <h6><a href="product-details.html">Men Size Yellow Basketball Jerseys</a></h6>
                                                    <div class="rating mb-5">
                                                        <ul>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                        </ul>
                                                        <span>(01 review)</span>
                                                    </div>
                                                    <div class="price">
                                                        <span>$105-$150</span>
                                                    </div>
                                                </div>
                                                <div class="product__add-cart text-center">
                                                    <button type="button" class="cart-btn product-modal-sidebar-open-btn d-flex align-items-center justify-content-center w-100">
                                                    Add to Cart
                                                    </button>
                                                </div>
                                            </div>
                                            <div class="product__item swiper-slide">
                                                <div class="product__thumb fix">
                                                    <div class="product-image w-img">
                                                        <a href="product-details.html">
                                                            <img src="{% static ''%}assets/img/product/tp-3.jpg" alt="product">
                                                        </a>
                                                    </div>
                                                    <div class="product__offer">
                                                    <span class="discount">-9%</span>
                                                    </div>
                                                    <div class="product-action">
                                                        <a href="#" class="icon-box icon-box-1" data-bs-toggle="modal" data-bs-target="#productModalId">
                                                            <i class="fal fa-eye"></i>
                                                            <i class="fal fa-eye"></i>
                                                        </a>
                                                        <a href="#" class="icon-box icon-box-1">
                                                            <i class="fal fa-heart"></i>
                                                            <i class="fal fa-heart"></i>
                                                        </a>
                                                        <a href="#" class="icon-box icon-box-1">
                                                            <i class="fal fa-layer-group"></i>
                                                            <i class="fal fa-layer-group"></i>
                                                        </a>
                                                    </div>
                                                </div>
                                                <div class="product__content">
                                                    <h6><a href="product-details.html">Xbox Wireless Game Controller Pink</a></h6>
                                                    <div class="rating mb-5">
                                                        <ul>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                        </ul>
                                                        <span>(01 review)</span>
                                                    </div>
                                                    <div class="price">
                                                        <span>$200-$280</span>
                                                    </div>
                                                </div>
                                                <div class="product__add-cart text-center">
                                                    <button type="button" class="cart-btn product-modal-sidebar-open-btn d-flex align-items-center justify-content-center w-100">
                                                    Add to Cart
                                                    </button>
                                                </div>
                                            </div>
                                            <div class="product__item swiper-slide">
                                                <div class="product__thumb fix">
                                                    <div class="product-image w-img">
                                                        <a href="product-details.html">
                                                            <img src="{% static ''%}assets/img/product/tp-4.jpg" alt="product">
                                                        </a>
                                                    </div>
                                                    <div class="product-action">
                                                        <a href="#" class="icon-box icon-box-1" data-bs-toggle="modal" data-bs-target="#productModalId">
                                                            <i class="fal fa-eye"></i>
                                                            <i class="fal fa-eye"></i>
                                                        </a>
                                                        <a href="#" class="icon-box icon-box-1">
                                                            <i class="fal fa-heart"></i>
                                                            <i class="fal fa-heart"></i>
                                                        </a>
                                                        <a href="#" class="icon-box icon-box-1">
                                                            <i class="fal fa-layer-group"></i>
                                                            <i class="fal fa-layer-group"></i>
                                                        </a>
                                                    </div>
                                                </div>
                                                <div class="product__content">
                                                    <h6><a href="product-details.html">Wireless Bluetooth Over-Ear Headphones</a></h6>
                                                    <div class="rating mb-5">
                                                        <ul>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                        </ul>
                                                        <span>(01 review)</span>
                                                    </div>
                                                    <div class="price">
                                                        <span>$100-$180</span>
                                                    </div>
                                                </div>
                                                <div class="product__add-cart text-center">
                                                    <button type="button" class="cart-btn product-modal-sidebar-open-btn d-flex align-items-center justify-content-center w-100">
                                                    Add to Cart
                                                    </button>
                                                </div>
                                            </div>
                                            <div class="product__item swiper-slide">
                                                <div class="product__thumb fix">
                                                    <div class="product-image w-img">
                                                        <a href="product-details.html">
                                                            <img src="{% static ''%}assets/img/product/tp-5.jpg" alt="product">
                                                        </a>
                                                    </div>
                                                    <div class="product__offer">
                                                    <span class="discount">-10%</span>
                                                    </div>
                                                    <div class="product-action">
                                                        <a href="#" class="icon-box icon-box-1" data-bs-toggle="modal" data-bs-target="#productModalId">
                                                            <i class="fal fa-eye"></i>
                                                            <i class="fal fa-eye"></i>
                                                        </a>
                                                        <a href="#" class="icon-box icon-box-1">
                                                            <i class="fal fa-heart"></i>
                                                            <i class="fal fa-heart"></i>
                                                        </a>
                                                        <a href="#" class="icon-box icon-box-1">
                                                            <i class="fal fa-layer-group"></i>
                                                            <i class="fal fa-layer-group"></i>
                                                        </a>
                                                    </div>
                                                </div>
                                                <div class="product__content">
                                                    <h6><a href="product-details.html">Solo3 Wireless On-Ear Headphones</a></h6>
                                                    <div class="rating mb-5">
                                                        <ul>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                        </ul>
                                                        <span>(01 review)</span>
                                                    </div>
                                                    <div class="price">
                                                        <span><del>$270</del> $200</span>
                                                    </div>
                                                </div>
                                                <div class="product__add-cart text-center">
                                                    <button type="button" class="cart-btn product-modal-sidebar-open-btn d-flex align-items-center justify-content-center w-100">
                                                    Add to Cart
                                                    </button>
                                                </div>
                                            </div>
                                            <div class="product__item swiper-slide">
                                                <div class="product__thumb fix">
                                                    <div class="product-image w-img">
                                                        <a href="product-details.html">
                                                            <img src="{% static ''%}assets/img/product/tp-6.jpg" alt="product">
                                                        </a>
                                                    </div>
                                                    <div class="product-action">
                                                        <a href="#" class="icon-box icon-box-1" data-bs-toggle="modal" data-bs-target="#productModalId">
                                                            <i class="fal fa-eye"></i>
                                                            <i class="fal fa-eye"></i>
                                                        </a>
                                                        <a href="#" class="icon-box icon-box-1">
                                                            <i class="fal fa-heart"></i>
                                                            <i class="fal fa-heart"></i>
                                                        </a>
                                                        <a href="#" class="icon-box icon-box-1">
                                                            <i class="fal fa-layer-group"></i>
                                                            <i class="fal fa-layer-group"></i>
                                                        </a>
                                                    </div>
                                                </div>
                                                <div class="product__content">
                                                    <h6><a href="product-details.html">Vifa Bluetooth Portable Wireless Speaker</a></h6>
                                                    <div class="rating mb-5">
                                                        <ul>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                        </ul>
                                                        <span>(01 review)</span>
                                                    </div>
                                                    <div class="price">
                                                        <span>$150-$270</span>
                                                    </div>
                                                </div>
                                                <div class="product__add-cart text-center">
                                                    <button type="button" class="cart-btn product-modal-sidebar-open-btn d-flex align-items-center justify-content-center w-100">
                                                    Add to Cart
                                                    </button>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <!-- If we need navigation buttons -->
                                    <div class="bs-button bs2-button-prev"><i class="fal fa-chevron-left"></i></div>
                                    <div class="bs-button bs2-button-next"><i class="fal fa-chevron-right"></i></div>
                                </div>
                            </div>
                            <div class="tab-pane fade" id="samsung" role="tabpanel" aria-labelledby="samsung-tab">
                                <div class="product-bs-slider-2">
                                    <div class="product-slider-2 swiper-container">
                                        <div class="swiper-wrapper">
                                            <div class="product__item swiper-slide">
                                                <div class="product__thumb fix">
                                                    <div class="product-image w-img">
                                                        <a href="product-details.html">
                                                            <img src="{% static ''%}assets/img/product/tp-1.jpg" alt="product">
                                                        </a>
                                                    </div>
                                                    <div class="product__offer">
                                                    <span class="discount">-15%</span>
                                                    </div>
                                                    <div class="product-action">
                                                        <a href="#" class="icon-box icon-box-1" data-bs-toggle="modal" data-bs-target="#productModalId">
                                                            <i class="fal fa-eye"></i>
                                                            <i class="fal fa-eye"></i>
                                                        </a>
                                                        <a href="#" class="icon-box icon-box-1">
                                                            <i class="fal fa-heart"></i>
                                                            <i class="fal fa-heart"></i>
                                                        </a>
                                                        <a href="#" class="icon-box icon-box-1">
                                                            <i class="fal fa-layer-group"></i>
                                                            <i class="fal fa-layer-group"></i>
                                                        </a>
                                                    </div>
                                                </div>
                                                <div class="product__content">
                                                    <h6><a href="product-details.html">Epple iPad Pro 10.5-inch Cellular 64G</a></h6>
                                                    <div class="rating mb-5">
                                                        <ul>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                        </ul>
                                                        <span>(01 review)</span>
                                                    </div>
                                                    <div class="price">
                                                        <span>$105-$110</span>
                                                    </div>
                                                </div>
                                                <div class="product__add-cart text-center">
                                                    <button type="button" class="cart-btn product-modal-sidebar-open-btn d-flex align-items-center justify-content-center w-100">
                                                    Add to Cart
                                                    </button>
                                                </div>
                                            </div> 
                                            <div class="product__item swiper-slide">
                                                <div class="product__thumb fix">
                                                    <div class="product-image w-img">
                                                        <a href="product-details.html">
                                                            <img src="{% static ''%}assets/img/product/tp-4.jpg" alt="product">
                                                        </a>
                                                    </div>
                                                    <div class="product-action">
                                                        <a href="#" class="icon-box icon-box-1" data-bs-toggle="modal" data-bs-target="#productModalId">
                                                            <i class="fal fa-eye"></i>
                                                            <i class="fal fa-eye"></i>
                                                        </a>
                                                        <a href="#" class="icon-box icon-box-1">
                                                            <i class="fal fa-heart"></i>
                                                            <i class="fal fa-heart"></i>
                                                        </a>
                                                        <a href="#" class="icon-box icon-box-1">
                                                            <i class="fal fa-layer-group"></i>
                                                            <i class="fal fa-layer-group"></i>
                                                        </a>
                                                    </div>
                                                </div>
                                                <div class="product__content">
                                                    <h6><a href="product-details.html">Wireless Bluetooth Over-Ear Headphones</a></h6>
                                                    <div class="rating mb-5">
                                                        <ul>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                        </ul>
                                                        <span>(01 review)</span>
                                                    </div>
                                                    <div class="price">
                                                        <span>$100-$180</span>
                                                    </div>
                                                </div>
                                                <div class="product__add-cart text-center">
                                                    <button type="button" class="cart-btn product-modal-sidebar-open-btn d-flex align-items-center justify-content-center w-100">
                                                    Add to Cart
                                                    </button>
                                                </div>
                                            </div>
                                            <div class="product__item swiper-slide">
                                                <div class="product__thumb fix">
                                                    <div class="product-image w-img">
                                                        <a href="product-details.html">
                                                            <img src="{% static ''%}assets/img/product/tp-5.jpg" alt="product">
                                                        </a>
                                                    </div>
                                                    <div class="product__offer">
                                                    <span class="discount">-10%</span>
                                                    </div>
                                                    <div class="product-action">
                                                        <a href="#" class="icon-box icon-box-1" data-bs-toggle="modal" data-bs-target="#productModalId">
                                                            <i class="fal fa-eye"></i>
                                                            <i class="fal fa-eye"></i>
                                                        </a>
                                                        <a href="#" class="icon-box icon-box-1">
                                                            <i class="fal fa-heart"></i>
                                                            <i class="fal fa-heart"></i>
                                                        </a>
                                                        <a href="#" class="icon-box icon-box-1">
                                                            <i class="fal fa-layer-group"></i>
                                                            <i class="fal fa-layer-group"></i>
                                                        </a>
                                                    </div>
                                                </div>
                                                <div class="product__content">
                                                    <h6><a href="product-details.html">Solo3 Wireless On-Ear Headphones</a></h6>
                                                    <div class="rating mb-5">
                                                        <ul>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                        </ul>
                                                        <span>(01 review)</span>
                                                    </div>
                                                    <div class="price">
                                                        <span><del>$270</del> $200</span>
                                                    </div>
                                                </div>
                                                <div class="product__add-cart text-center">
                                                    <button type="button" class="cart-btn product-modal-sidebar-open-btn d-flex align-items-center justify-content-center w-100">
                                                    Add to Cart
                                                    </button>
                                                </div>
                                            </div>
                                            <div class="product__item swiper-slide">
                                                <div class="product__thumb fix">
                                                    <div class="product-image w-img">
                                                        <a href="product-details.html">
                                                            <img src="{% static ''%}assets/img/product/tp-6.jpg" alt="product">
                                                        </a>
                                                    </div>
                                                    <div class="product-action">
                                                        <a href="#" class="icon-box icon-box-1" data-bs-toggle="modal" data-bs-target="#productModalId">
                                                            <i class="fal fa-eye"></i>
                                                            <i class="fal fa-eye"></i>
                                                        </a>
                                                        <a href="#" class="icon-box icon-box-1">
                                                            <i class="fal fa-heart"></i>
                                                            <i class="fal fa-heart"></i>
                                                        </a>
                                                        <a href="#" class="icon-box icon-box-1">
                                                            <i class="fal fa-layer-group"></i>
                                                            <i class="fal fa-layer-group"></i>
                                                        </a>
                                                    </div>
                                                </div>
                                                <div class="product__content">
                                                    <h6><a href="product-details.html">Vifa Bluetooth Portable Wireless Speaker</a></h6>
                                                    <div class="rating mb-5">
                                                        <ul>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                        </ul>
                                                        <span>(01 review)</span>
                                                    </div>
                                                    <div class="price">
                                                        <span>$150-$270</span>
                                                    </div>
                                                </div>
                                                <div class="product__add-cart text-center">
                                                    <button type="button" class="cart-btn product-modal-sidebar-open-btn d-flex align-items-center justify-content-center w-100">
                                                    Add to Cart
                                                    </button>
                                                </div>
                                            </div>
                                            <div class="product__item swiper-slide">
                                                <div class="product__thumb fix">
                                                    <div class="product-image w-img">
                                                        <a href="product-details.html">
                                                            <img src="{% static ''%}assets/img/product/tp-2.jpg" alt="product">
                                                        </a>
                                                    </div>
                                                    <div class="product-action">
                                                        <a href="#" class="icon-box icon-box-1" data-bs-toggle="modal" data-bs-target="#productModalId">
                                                            <i class="fal fa-eye"></i>
                                                            <i class="fal fa-eye"></i>
                                                        </a>
                                                        <a href="#" class="icon-box icon-box-1">
                                                            <i class="fal fa-heart"></i>
                                                            <i class="fal fa-heart"></i>
                                                        </a>
                                                        <a href="#" class="icon-box icon-box-1">
                                                            <i class="fal fa-layer-group"></i>
                                                            <i class="fal fa-layer-group"></i>
                                                        </a>
                                                    </div>
                                                </div>
                                                <div class="product__content">
                                                    <h6><a href="product-details.html">Men Size Yellow Basketball Jerseys</a></h6>
                                                    <div class="rating mb-5">
                                                        <ul>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                        </ul>
                                                        <span>(01 review)</span>
                                                    </div>
                                                    <div class="price">
                                                        <span>$105-$150</span>
                                                    </div>
                                                </div>
                                                <div class="product__add-cart text-center">
                                                    <button type="button" class="cart-btn product-modal-sidebar-open-btn d-flex align-items-center justify-content-center w-100">
                                                    Add to Cart
                                                    </button>
                                                </div>
                                            </div>
                                            <div class="product__item swiper-slide">
                                                <div class="product__thumb fix">
                                                    <div class="product-image w-img">
                                                        <a href="product-details.html">
                                                            <img src="{% static ''%}assets/img/product/tp-3.jpg" alt="product">
                                                        </a>
                                                    </div>
                                                    <div class="product__offer">
                                                    <span class="discount">-9%</span>
                                                    </div>
                                                    <div class="product-action">
                                                        <a href="#" class="icon-box icon-box-1" data-bs-toggle="modal" data-bs-target="#productModalId">
                                                            <i class="fal fa-eye"></i>
                                                            <i class="fal fa-eye"></i>
                                                        </a>
                                                        <a href="#" class="icon-box icon-box-1">
                                                            <i class="fal fa-heart"></i>
                                                            <i class="fal fa-heart"></i>
                                                        </a>
                                                        <a href="#" class="icon-box icon-box-1">
                                                            <i class="fal fa-layer-group"></i>
                                                            <i class="fal fa-layer-group"></i>
                                                        </a>
                                                    </div>
                                                </div>
                                                <div class="product__content">
                                                    <h6><a href="product-details.html">Xbox Wireless Game Controller Pink</a></h6>
                                                    <div class="rating mb-5">
                                                        <ul>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                        </ul>
                                                        <span>(01 review)</span>
                                                    </div>
                                                    <div class="price">
                                                        <span>$200-$280</span>
                                                    </div>
                                                </div>
                                                <div class="product__add-cart text-center">
                                                    <button type="button" class="cart-btn product-modal-sidebar-open-btn d-flex align-items-center justify-content-center w-100">
                                                    Add to Cart
                                                    </button>
                                                </div>
                                            </div>
                                        </div>
                                        <!-- If we need navigation buttons -->
                                    </div>
                                    <div class="bs-button bs2-button-prev"><i class="fal fa-chevron-left"></i></div>
                                    <div class="bs-button bs2-button-next"><i class="fal fa-chevron-right"></i></div>
                                </div>
                            </div>
                            <div class="tab-pane fade" id="htc" role="tabpanel" aria-labelledby="htc-tab">
                                <div class="product-bs-slider-2">
                                    <div class="product-slider-2 swiper-container">
                                        <div class="swiper-wrapper">
                                            <div class="product__item swiper-slide">
                                                <div class="product__thumb fix">
                                                    <div class="product-image w-img">
                                                        <a href="product-details.html">
                                                            <img src="{% static ''%}assets/img/product/tp-4.jpg" alt="product">
                                                        </a>
                                                    </div>
                                                    <div class="product-action">
                                                        <a href="#" class="icon-box icon-box-1" data-bs-toggle="modal" data-bs-target="#productModalId">
                                                            <i class="fal fa-eye"></i>
                                                            <i class="fal fa-eye"></i>
                                                        </a>
                                                        <a href="#" class="icon-box icon-box-1">
                                                            <i class="fal fa-heart"></i>
                                                            <i class="fal fa-heart"></i>
                                                        </a>
                                                        <a href="#" class="icon-box icon-box-1">
                                                            <i class="fal fa-layer-group"></i>
                                                            <i class="fal fa-layer-group"></i>
                                                        </a>
                                                    </div>
                                                </div>
                                                <div class="product__content">
                                                    <h6><a href="product-details.html">Wireless Bluetooth Over-Ear Headphones</a></h6>
                                                    <div class="rating mb-5">
                                                        <ul>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                        </ul>
                                                        <span>(01 review)</span>
                                                    </div>
                                                    <div class="price">
                                                        <span>$100-$180</span>
                                                    </div>
                                                </div>
                                                <div class="product__add-cart text-center">
                                                    <button type="button" class="cart-btn product-modal-sidebar-open-btn d-flex align-items-center justify-content-center w-100">
                                                    Add to Cart
                                                    </button>
                                                </div>
                                            </div>
                                            <div class="product__item swiper-slide">
                                                <div class="product__thumb fix">
                                                    <div class="product-image w-img">
                                                        <a href="product-details.html">
                                                            <img src="{% static ''%}assets/img/product/tp-5.jpg" alt="product">
                                                        </a>
                                                    </div>
                                                    <div class="product__offer">
                                                    <span class="discount">-10%</span>
                                                    </div>
                                                    <div class="product-action">
                                                        <a href="#" class="icon-box icon-box-1" data-bs-toggle="modal" data-bs-target="#productModalId">
                                                            <i class="fal fa-eye"></i>
                                                            <i class="fal fa-eye"></i>
                                                        </a>
                                                        <a href="#" class="icon-box icon-box-1">
                                                            <i class="fal fa-heart"></i>
                                                            <i class="fal fa-heart"></i>
                                                        </a>
                                                        <a href="#" class="icon-box icon-box-1">
                                                            <i class="fal fa-layer-group"></i>
                                                            <i class="fal fa-layer-group"></i>
                                                        </a>
                                                    </div>
                                                </div>
                                                <div class="product__content">
                                                    <h6><a href="product-details.html">Solo3 Wireless On-Ear Headphones</a></h6>
                                                    <div class="rating mb-5">
                                                        <ul>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                        </ul>
                                                        <span>(01 review)</span>
                                                    </div>
                                                    <div class="price">
                                                        <span><del>$270</del> $200</span>
                                                    </div>
                                                </div>
                                                <div class="product__add-cart text-center">
                                                    <button type="button" class="cart-btn product-modal-sidebar-open-btn d-flex align-items-center justify-content-center w-100">
                                                    Add to Cart
                                                    </button>
                                                </div>
                                            </div>
                                            <div class="product__item swiper-slide">
                                                <div class="product__thumb fix">
                                                    <div class="product-image w-img">
                                                        <a href="product-details.html">
                                                            <img src="{% static ''%}assets/img/product/tp-6.jpg" alt="product">
                                                        </a>
                                                    </div>
                                                    <div class="product-action">
                                                        <a href="#" class="icon-box icon-box-1" data-bs-toggle="modal" data-bs-target="#productModalId">
                                                            <i class="fal fa-eye"></i>
                                                            <i class="fal fa-eye"></i>
                                                        </a>
                                                        <a href="#" class="icon-box icon-box-1">
                                                            <i class="fal fa-heart"></i>
                                                            <i class="fal fa-heart"></i>
                                                        </a>
                                                        <a href="#" class="icon-box icon-box-1">
                                                            <i class="fal fa-layer-group"></i>
                                                            <i class="fal fa-layer-group"></i>
                                                        </a>
                                                    </div>
                                                </div>
                                                <div class="product__content">
                                                    <h6><a href="product-details.html">Vifa Bluetooth Portable Wireless Speaker</a></h6>
                                                    <div class="rating mb-5">
                                                        <ul>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                        </ul>
                                                        <span>(01 review)</span>
                                                    </div>
                                                    <div class="price">
                                                        <span>$150-$270</span>
                                                    </div>
                                                </div>
                                                <div class="product__add-cart text-center">
                                                    <button type="button" class="cart-btn product-modal-sidebar-open-btn d-flex align-items-center justify-content-center w-100">
                                                    Add to Cart
                                                    </button>
                                                </div>
                                            </div>
                                            <div class="product__item swiper-slide">
                                                <div class="product__thumb fix">
                                                    <div class="product-image w-img">
                                                        <a href="product-details.html">
                                                            <img src="{% static ''%}assets/img/product/tp-1.jpg" alt="product">
                                                        </a>
                                                    </div>
                                                    <div class="product__offer">
                                                    <span class="discount">-15%</span>
                                                    </div>
                                                    <div class="product-action">
                                                        <a href="#" class="icon-box icon-box-1" data-bs-toggle="modal" data-bs-target="#productModalId">
                                                            <i class="fal fa-eye"></i>
                                                            <i class="fal fa-eye"></i>
                                                        </a>
                                                        <a href="#" class="icon-box icon-box-1">
                                                            <i class="fal fa-heart"></i>
                                                            <i class="fal fa-heart"></i>
                                                        </a>
                                                        <a href="#" class="icon-box icon-box-1">
                                                            <i class="fal fa-layer-group"></i>
                                                            <i class="fal fa-layer-group"></i>
                                                        </a>
                                                    </div>
                                                </div>
                                                <div class="product__content">
                                                    <h6><a href="product-details.html">Epple iPad Pro 10.5-inch Cellular 64G</a></h6>
                                                    <div class="rating mb-5">
                                                        <ul>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                        </ul>
                                                        <span>(01 review)</span>
                                                    </div>
                                                    <div class="price">
                                                        <span>$105-$110</span>
                                                    </div>
                                                </div>
                                                <div class="product__add-cart text-center">
                                                    <button type="button" class="cart-btn product-modal-sidebar-open-btn d-flex align-items-center justify-content-center w-100">
                                                    Add to Cart
                                                    </button>
                                                </div>
                                            </div>
                                            <div class="product__item swiper-slide">
                                                <div class="product__thumb fix">
                                                    <div class="product-image w-img">
                                                        <a href="product-details.html">
                                                            <img src="{% static ''%}assets/img/product/tp-2.jpg" alt="product">
                                                        </a>
                                                    </div>
                                                    <div class="product-action">
                                                        <a href="#" class="icon-box icon-box-1" data-bs-toggle="modal" data-bs-target="#productModalId">
                                                            <i class="fal fa-eye"></i>
                                                            <i class="fal fa-eye"></i>
                                                        </a>
                                                        <a href="#" class="icon-box icon-box-1">
                                                            <i class="fal fa-heart"></i>
                                                            <i class="fal fa-heart"></i>
                                                        </a>
                                                        <a href="#" class="icon-box icon-box-1">
                                                            <i class="fal fa-layer-group"></i>
                                                            <i class="fal fa-layer-group"></i>
                                                        </a>
                                                    </div>
                                                </div>
                                                <div class="product__content">
                                                    <h6><a href="product-details.html">Men Size Yellow Basketball Jerseys</a></h6>
                                                    <div class="rating mb-5">
                                                        <ul>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                        </ul>
                                                        <span>(01 review)</span>
                                                    </div>
                                                    <div class="price">
                                                        <span>$105-$150</span>
                                                    </div>
                                                </div>
                                                <div class="product__add-cart text-center">
                                                    <button type="button" class="cart-btn product-modal-sidebar-open-btn d-flex align-items-center justify-content-center w-100">
                                                    Add to Cart
                                                    </button>
                                                </div>
                                            </div>
                                            <div class="product__item swiper-slide">
                                                <div class="product__thumb fix">
                                                    <div class="product-image w-img">
                                                        <a href="product-details.html">
                                                            <img src="{% static ''%}assets/img/product/tp-3.jpg" alt="product">
                                                        </a>
                                                    </div>
                                                    <div class="product__offer">
                                                    <span class="discount">-9%</span>
                                                    </div>
                                                    <div class="product-action">
                                                        <a href="#" class="icon-box icon-box-1" data-bs-toggle="modal" data-bs-target="#productModalId">
                                                            <i class="fal fa-eye"></i>
                                                            <i class="fal fa-eye"></i>
                                                        </a>
                                                        <a href="#" class="icon-box icon-box-1">
                                                            <i class="fal fa-heart"></i>
                                                            <i class="fal fa-heart"></i>
                                                        </a>
                                                        <a href="#" class="icon-box icon-box-1">
                                                            <i class="fal fa-layer-group"></i>
                                                            <i class="fal fa-layer-group"></i>
                                                        </a>
                                                    </div>
                                                </div>
                                                <div class="product__content">
                                                    <h6><a href="product-details.html">Xbox Wireless Game Controller Pink</a></h6>
                                                    <div class="rating mb-5">
                                                        <ul>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                        </ul>
                                                        <span>(01 review)</span>
                                                    </div>
                                                    <div class="price">
                                                        <span>$200-$280</span>
                                                    </div>
                                                </div>
                                                <div class="product__add-cart text-center">
                                                    <button type="button" class="cart-btn product-modal-sidebar-open-btn d-flex align-items-center justify-content-center w-100">
                                                    Add to Cart
                                                    </button>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <!-- If we need navigation buttons -->
                                    <div class="bs-button bs2-button-prev"><i class="fal fa-chevron-left"></i></div>
                                    <div class="bs-button bs2-button-next"><i class="fal fa-chevron-right"></i></div>
                                </div>
                            </div>
                            <div class="tab-pane fade" id="nokia" role="tabpanel" aria-labelledby="nokia-tab">
                                <div class="product-bs-slider-2">
                                    <div class="product-slider-2 swiper-container">
                                        <div class="swiper-wrapper">
                                            <div class="product__item swiper-slide">
                                                <div class="product__thumb fix">
                                                    <div class="product-image w-img">
                                                        <a href="product-details.html">
                                                            <img src="{% static ''%}assets/img/product/tp-1.jpg" alt="product">
                                                        </a>
                                                    </div>
                                                    <div class="product__offer">
                                                    <span class="discount">-15%</span>
                                                    </div>
                                                    <div class="product-action">
                                                        <a href="#" class="icon-box icon-box-1" data-bs-toggle="modal" data-bs-target="#productModalId">
                                                            <i class="fal fa-eye"></i>
                                                            <i class="fal fa-eye"></i>
                                                        </a>
                                                        <a href="#" class="icon-box icon-box-1">
                                                            <i class="fal fa-heart"></i>
                                                            <i class="fal fa-heart"></i>
                                                        </a>
                                                        <a href="#" class="icon-box icon-box-1">
                                                            <i class="fal fa-layer-group"></i>
                                                            <i class="fal fa-layer-group"></i>
                                                        </a>
                                                    </div>
                                                </div>
                                                <div class="product__content">
                                                    <h6><a href="product-details.html">Epple iPad Pro 10.5-inch Cellular 64G</a></h6>
                                                    <div class="rating mb-5">
                                                        <ul>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                        </ul>
                                                        <span>(01 review)</span>
                                                    </div>
                                                    <div class="price">
                                                        <span>$105-$110</span>
                                                    </div>
                                                </div>
                                                <div class="product__add-cart text-center">
                                                    <button type="button" class="cart-btn product-modal-sidebar-open-btn d-flex align-items-center justify-content-center w-100">
                                                    Add to Cart
                                                    </button>
                                                </div>
                                            </div>
                                            <div class="product__item swiper-slide">
                                                <div class="product__thumb fix">
                                                    <div class="product-image w-img">
                                                        <a href="product-details.html">
                                                            <img src="{% static ''%}assets/img/product/tp-2.jpg" alt="product">
                                                        </a>
                                                    </div>
                                                    <div class="product-action">
                                                        <a href="#" class="icon-box icon-box-1" data-bs-toggle="modal" data-bs-target="#productModalId">
                                                            <i class="fal fa-eye"></i>
                                                            <i class="fal fa-eye"></i>
                                                        </a>
                                                        <a href="#" class="icon-box icon-box-1">
                                                            <i class="fal fa-heart"></i>
                                                            <i class="fal fa-heart"></i>
                                                        </a>
                                                        <a href="#" class="icon-box icon-box-1">
                                                            <i class="fal fa-layer-group"></i>
                                                            <i class="fal fa-layer-group"></i>
                                                        </a>
                                                    </div>
                                                </div>
                                                <div class="product__content">
                                                    <h6><a href="product-details.html">Men Size Yellow Basketball Jerseys</a></h6>
                                                    <div class="rating mb-5">
                                                        <ul>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                        </ul>
                                                        <span>(01 review)</span>
                                                    </div>
                                                    <div class="price">
                                                        <span>$105-$150</span>
                                                    </div>
                                                </div>
                                                <div class="product__add-cart text-center">
                                                    <button type="button" class="cart-btn product-modal-sidebar-open-btn d-flex align-items-center justify-content-center w-100">
                                                    Add to Cart
                                                    </button>
                                                </div>
                                            </div>
                                            <div class="product__item swiper-slide">
                                                <div class="product__thumb fix">
                                                    <div class="product-image w-img">
                                                        <a href="product-details.html">
                                                            <img src="{% static ''%}assets/img/product/tp-3.jpg" alt="product">
                                                        </a>
                                                    </div>
                                                    <div class="product__offer">
                                                    <span class="discount">-9%</span>
                                                    </div>
                                                    <div class="product-action">
                                                        <a href="#" class="icon-box icon-box-1" data-bs-toggle="modal" data-bs-target="#productModalId">
                                                            <i class="fal fa-eye"></i>
                                                            <i class="fal fa-eye"></i>
                                                        </a>
                                                        <a href="#" class="icon-box icon-box-1">
                                                            <i class="fal fa-heart"></i>
                                                            <i class="fal fa-heart"></i>
                                                        </a>
                                                        <a href="#" class="icon-box icon-box-1">
                                                            <i class="fal fa-layer-group"></i>
                                                            <i class="fal fa-layer-group"></i>
                                                        </a>
                                                    </div>
                                                </div>
                                                <div class="product__content">
                                                    <h6><a href="product-details.html">Xbox Wireless Game Controller Pink</a></h6>
                                                    <div class="rating mb-5">
                                                        <ul>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                        </ul>
                                                        <span>(01 review)</span>
                                                    </div>
                                                    <div class="price">
                                                        <span>$200-$280</span>
                                                    </div>
                                                </div>
                                                <div class="product__add-cart text-center">
                                                    <button type="button" class="cart-btn product-modal-sidebar-open-btn d-flex align-items-center justify-content-center w-100">
                                                    Add to Cart
                                                    </button>
                                                </div>
                                            </div>
                                            <div class="product__item swiper-slide">
                                                <div class="product__thumb fix">
                                                    <div class="product-image w-img">
                                                        <a href="product-details.html">
                                                            <img src="{% static ''%}assets/img/product/tp-4.jpg" alt="product">
                                                        </a>
                                                    </div>
                                                    <div class="product-action">
                                                        <a href="#" class="icon-box icon-box-1" data-bs-toggle="modal" data-bs-target="#productModalId">
                                                            <i class="fal fa-eye"></i>
                                                            <i class="fal fa-eye"></i>
                                                        </a>
                                                        <a href="#" class="icon-box icon-box-1">
                                                            <i class="fal fa-heart"></i>
                                                            <i class="fal fa-heart"></i>
                                                        </a>
                                                        <a href="#" class="icon-box icon-box-1">
                                                            <i class="fal fa-layer-group"></i>
                                                            <i class="fal fa-layer-group"></i>
                                                        </a>
                                                    </div>
                                                </div>
                                                <div class="product__content">
                                                    <h6><a href="product-details.html">Wireless Bluetooth Over-Ear Headphones</a></h6>
                                                    <div class="rating mb-5">
                                                        <ul>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                        </ul>
                                                        <span>(01 review)</span>
                                                    </div>
                                                    <div class="price">
                                                        <span>$100-$180</span>
                                                    </div>
                                                </div>
                                                <div class="product__add-cart text-center">
                                                    <button type="button" class="cart-btn product-modal-sidebar-open-btn d-flex align-items-center justify-content-center w-100">
                                                    Add to Cart
                                                    </button>
                                                </div>
                                            </div>
                                            <div class="product__item swiper-slide">
                                                <div class="product__thumb fix">
                                                    <div class="product-image w-img">
                                                        <a href="product-details.html">
                                                            <img src="{% static ''%}assets/img/product/tp-5.jpg" alt="product">
                                                        </a>
                                                    </div>
                                                    <div class="product__offer">
                                                    <span class="discount">-10%</span>
                                                    </div>
                                                    <div class="product-action">
                                                        <a href="#" class="icon-box icon-box-1" data-bs-toggle="modal" data-bs-target="#productModalId">
                                                            <i class="fal fa-eye"></i>
                                                            <i class="fal fa-eye"></i>
                                                        </a>
                                                        <a href="#" class="icon-box icon-box-1">
                                                            <i class="fal fa-heart"></i>
                                                            <i class="fal fa-heart"></i>
                                                        </a>
                                                        <a href="#" class="icon-box icon-box-1">
                                                            <i class="fal fa-layer-group"></i>
                                                            <i class="fal fa-layer-group"></i>
                                                        </a>
                                                    </div>
                                                </div>
                                                <div class="product__content">
                                                    <h6><a href="product-details.html">Solo3 Wireless On-Ear Headphones</a></h6>
                                                    <div class="rating mb-5">
                                                        <ul>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                        </ul>
                                                        <span>(01 review)</span>
                                                    </div>
                                                    <div class="price">
                                                        <span><del>$270</del> $200</span>
                                                    </div>
                                                </div>
                                                <div class="product__add-cart text-center">
                                                    <button type="button" class="cart-btn product-modal-sidebar-open-btn d-flex align-items-center justify-content-center w-100">
                                                    Add to Cart
                                                    </button>
                                                </div>
                                            </div>
                                            <div class="product__item swiper-slide">
                                                <div class="product__thumb fix">
                                                    <div class="product-image w-img">
                                                        <a href="product-details.html">
                                                            <img src="{% static ''%}assets/img/product/tp-6.jpg" alt="product">
                                                        </a>
                                                    </div>
                                                    <div class="product-action">
                                                        <a href="#" class="icon-box icon-box-1" data-bs-toggle="modal" data-bs-target="#productModalId">
                                                            <i class="fal fa-eye"></i>
                                                            <i class="fal fa-eye"></i>
                                                        </a>
                                                        <a href="#" class="icon-box icon-box-1">
                                                            <i class="fal fa-heart"></i>
                                                            <i class="fal fa-heart"></i>
                                                        </a>
                                                        <a href="#" class="icon-box icon-box-1">
                                                            <i class="fal fa-layer-group"></i>
                                                            <i class="fal fa-layer-group"></i>
                                                        </a>
                                                    </div>
                                                </div>
                                                <div class="product__content">
                                                    <h6><a href="product-details.html">Vifa Bluetooth Portable Wireless Speaker</a></h6>
                                                    <div class="rating mb-5">
                                                        <ul>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                        </ul>
                                                        <span>(01 review)</span>
                                                    </div>
                                                    <div class="price">
                                                        <span>$150-$270</span>
                                                    </div>
                                                </div>
                                                <div class="product__add-cart text-center">
                                                    <button type="button" class="cart-btn product-modal-sidebar-open-btn d-flex align-items-center justify-content-center w-100">
                                                    Add to Cart
                                                    </button>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <!-- If we need navigation buttons -->
                                    <div class="bs-button bs2-button-prev"><i class="fal fa-chevron-left"></i></div>
                                    <div class="bs-button bs2-button-next"><i class="fal fa-chevron-right"></i></div>
                                </div>
                            </div>
                            <div class="tab-pane fade" id="cell" role="tabpanel" aria-labelledby="cell-tab">
                                <div class="product-bs-slider-2">
                                    <div class="product-slider-2 swiper-container">
                                        <div class="swiper-wrapper">
                                            <div class="product__item swiper-slide">
                                                <div class="product__thumb fix">
                                                    <div class="product-image w-img">
                                                        <a href="product-details.html">
                                                            <img src="{% static ''%}assets/img/product/tp-1.jpg" alt="product">
                                                        </a>
                                                    </div>
                                                    <div class="product__offer">
                                                    <span class="discount">-15%</span>
                                                    </div>
                                                    <div class="product-action">
                                                        <a href="#" class="icon-box icon-box-1" data-bs-toggle="modal" data-bs-target="#productModalId">
                                                            <i class="fal fa-eye"></i>
                                                            <i class="fal fa-eye"></i>
                                                        </a>
                                                        <a href="#" class="icon-box icon-box-1">
                                                            <i class="fal fa-heart"></i>
                                                            <i class="fal fa-heart"></i>
                                                        </a>
                                                        <a href="#" class="icon-box icon-box-1">
                                                            <i class="fal fa-layer-group"></i>
                                                            <i class="fal fa-layer-group"></i>
                                                        </a>
                                                    </div>
                                                </div>
                                                <div class="product__content">
                                                    <h6><a href="product-details.html">Epple iPad Pro 10.5-inch Cellular 64G</a></h6>
                                                    <div class="rating mb-5">
                                                        <ul>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                        </ul>
                                                        <span>(01 review)</span>
                                                    </div>
                                                    <div class="price">
                                                        <span>$105-$110</span>
                                                    </div>
                                                </div>
                                                <div class="product__add-cart text-center">
                                                    <button type="button" class="cart-btn product-modal-sidebar-open-btn d-flex align-items-center justify-content-center w-100">
                                                    Add to Cart
                                                    </button>
                                                </div>
                                            </div>
                                            <div class="product__item swiper-slide">
                                                <div class="product__thumb fix">
                                                    <div class="product-image w-img">
                                                        <a href="product-details.html">
                                                            <img src="{% static ''%}assets/img/product/tp-2.jpg" alt="product">
                                                        </a>
                                                    </div>
                                                    <div class="product-action">
                                                        <a href="#" class="icon-box icon-box-1" data-bs-toggle="modal" data-bs-target="#productModalId">
                                                            <i class="fal fa-eye"></i>
                                                            <i class="fal fa-eye"></i>
                                                        </a>
                                                        <a href="#" class="icon-box icon-box-1">
                                                            <i class="fal fa-heart"></i>
                                                            <i class="fal fa-heart"></i>
                                                        </a>
                                                        <a href="#" class="icon-box icon-box-1">
                                                            <i class="fal fa-layer-group"></i>
                                                            <i class="fal fa-layer-group"></i>
                                                        </a>
                                                    </div>
                                                </div>
                                                <div class="product__content">
                                                    <h6><a href="product-details.html">Men Size Yellow Basketball Jerseys</a></h6>
                                                    <div class="rating mb-5">
                                                        <ul>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                        </ul>
                                                        <span>(01 review)</span>
                                                    </div>
                                                    <div class="price">
                                                        <span>$105-$150</span>
                                                    </div>
                                                </div>
                                                <div class="product__add-cart text-center">
                                                    <button type="button" class="cart-btn product-modal-sidebar-open-btn d-flex align-items-center justify-content-center w-100">
                                                    Add to Cart
                                                    </button>
                                                </div>
                                            </div>
                                            <div class="product__item swiper-slide">
                                                <div class="product__thumb fix">
                                                    <div class="product-image w-img">
                                                        <a href="product-details.html">
                                                            <img src="{% static ''%}assets/img/product/tp-3.jpg" alt="product">
                                                        </a>
                                                    </div>
                                                    <div class="product__offer">
                                                    <span class="discount">-9%</span>
                                                    </div>
                                                    <div class="product-action">
                                                        <a href="#" class="icon-box icon-box-1" data-bs-toggle="modal" data-bs-target="#productModalId">
                                                            <i class="fal fa-eye"></i>
                                                            <i class="fal fa-eye"></i>
                                                        </a>
                                                        <a href="#" class="icon-box icon-box-1">
                                                            <i class="fal fa-heart"></i>
                                                            <i class="fal fa-heart"></i>
                                                        </a>
                                                        <a href="#" class="icon-box icon-box-1">
                                                            <i class="fal fa-layer-group"></i>
                                                            <i class="fal fa-layer-group"></i>
                                                        </a>
                                                    </div>
                                                </div>
                                                <div class="product__content">
                                                    <h6><a href="product-details.html">Xbox Wireless Game Controller Pink</a></h6>
                                                    <div class="rating mb-5">
                                                        <ul>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                        </ul>
                                                        <span>(01 review)</span>
                                                    </div>
                                                    <div class="price">
                                                        <span>$200-$280</span>
                                                    </div>
                                                </div>
                                                <div class="product__add-cart text-center">
                                                    <button type="button" class="cart-btn product-modal-sidebar-open-btn d-flex align-items-center justify-content-center w-100">
                                                    Add to Cart
                                                    </button>
                                                </div>
                                            </div>
                                            <div class="product__item swiper-slide">
                                                <div class="product__thumb fix">
                                                    <div class="product-image w-img">
                                                        <a href="product-details.html">
                                                            <img src="{% static ''%}assets/img/product/tp-4.jpg" alt="product">
                                                        </a>
                                                    </div>
                                                    <div class="product-action">
                                                        <a href="#" class="icon-box icon-box-1" data-bs-toggle="modal" data-bs-target="#productModalId">
                                                            <i class="fal fa-eye"></i>
                                                            <i class="fal fa-eye"></i>
                                                        </a>
                                                        <a href="#" class="icon-box icon-box-1">
                                                            <i class="fal fa-heart"></i>
                                                            <i class="fal fa-heart"></i>
                                                        </a>
                                                        <a href="#" class="icon-box icon-box-1">
                                                            <i class="fal fa-layer-group"></i>
                                                            <i class="fal fa-layer-group"></i>
                                                        </a>
                                                    </div>
                                                </div>
                                                <div class="product__content">
                                                    <h6><a href="product-details.html">Wireless Bluetooth Over-Ear Headphones</a></h6>
                                                    <div class="rating mb-5">
                                                        <ul>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                        </ul>
                                                        <span>(01 review)</span>
                                                    </div>
                                                    <div class="price">
                                                        <span>$100-$180</span>
                                                    </div>
                                                </div>
                                                <div class="product__add-cart text-center">
                                                    <button type="button" class="cart-btn product-modal-sidebar-open-btn d-flex align-items-center justify-content-center w-100">
                                                    Add to Cart
                                                    </button>
                                                </div>
                                            </div>
                                            <div class="product__item swiper-slide">
                                                <div class="product__thumb fix">
                                                    <div class="product-image w-img">
                                                        <a href="product-details.html">
                                                            <img src="{% static ''%}assets/img/product/tp-5.jpg" alt="product">
                                                        </a>
                                                    </div>
                                                    <div class="product__offer">
                                                    <span class="discount">-10%</span>
                                                    </div>
                                                    <div class="product-action">
                                                        <a href="#" class="icon-box icon-box-1" data-bs-toggle="modal" data-bs-target="#productModalId">
                                                            <i class="fal fa-eye"></i>
                                                            <i class="fal fa-eye"></i>
                                                        </a>
                                                        <a href="#" class="icon-box icon-box-1">
                                                            <i class="fal fa-heart"></i>
                                                            <i class="fal fa-heart"></i>
                                                        </a>
                                                        <a href="#" class="icon-box icon-box-1">
                                                            <i class="fal fa-layer-group"></i>
                                                            <i class="fal fa-layer-group"></i>
                                                        </a>
                                                    </div>
                                                </div>
                                                <div class="product__content">
                                                    <h6><a href="product-details.html">Solo3 Wireless On-Ear Headphones</a></h6>
                                                    <div class="rating mb-5">
                                                        <ul>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                        </ul>
                                                        <span>(01 review)</span>
                                                    </div>
                                                    <div class="price">
                                                        <span><del>$270</del> $200</span>
                                                    </div>
                                                </div>
                                                <div class="product__add-cart text-center">
                                                    <button type="button" class="cart-btn product-modal-sidebar-open-btn d-flex align-items-center justify-content-center w-100">
                                                    Add to Cart
                                                    </button>
                                                </div>
                                            </div>
                                            <div class="product__item swiper-slide">
                                                <div class="product__thumb fix">
                                                    <div class="product-image w-img">
                                                        <a href="product-details.html">
                                                            <img src="{% static ''%}assets/img/product/tp-6.jpg" alt="product">
                                                        </a>
                                                    </div>
                                                    <div class="product-action">
                                                        <a href="#" class="icon-box icon-box-1" data-bs-toggle="modal" data-bs-target="#productModalId">
                                                            <i class="fal fa-eye"></i>
                                                            <i class="fal fa-eye"></i>
                                                        </a>
                                                        <a href="#" class="icon-box icon-box-1">
                                                            <i class="fal fa-heart"></i>
                                                            <i class="fal fa-heart"></i>
                                                        </a>
                                                        <a href="#" class="icon-box icon-box-1">
                                                            <i class="fal fa-layer-group"></i>
                                                            <i class="fal fa-layer-group"></i>
                                                        </a>
                                                    </div>
                                                </div>
                                                <div class="product__content">
                                                    <h6><a href="product-details.html">Vifa Bluetooth Portable Wireless Speaker</a></h6>
                                                    <div class="rating mb-5">
                                                        <ul>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                        </ul>
                                                        <span>(01 review)</span>
                                                    </div>
                                                    <div class="price">
                                                        <span>$150-$270</span>
                                                    </div>
                                                </div>
                                                <div class="product__add-cart text-center">
                                                    <button type="button" class="cart-btn product-modal-sidebar-open-btn d-flex align-items-center justify-content-center w-100">
                                                    Add to Cart
                                                    </button>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <!-- If we need navigation buttons -->
                                    <div class="bs-button bs2-button-prev"><i class="fal fa-chevron-left"></i></div>
                                    <div class="bs-button bs2-button-next"><i class="fal fa-chevron-right"></i></div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <!-- topsell__area-end -->

        <!-- featured-start -->
        <section class="featured light-bg pt-55 pb-40">
            <div class="container">
                <div class="row">
                    <div class="col-xl-12">
                        <div class="section__head d-flex justify-content-between mb-30">
                            <div class="section__title">
                                <h5 class="st-titile">Top Featured Products</h5>
                            </div>
                            <div class="button-wrap">
                                <a href="shop.html">See All Product <i class="fal fa-chevron-right"></i></a>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="row">
                    <div class="col-xl-6 col-lg-12">
                        <div class="single-features-item single-features-item-d b-radius mb-20">
                            <div class="row  g-0 align-items-center">
                            {% for i in product|slice:"1" %}
                                <div class="col-md-6">
                                    <div class="features-thum">
                                        <div class="features-product-image w-img">
                                            <a href="product-details.html"><img src="{{ i.image.url }}" alt=""></a>
                                        </div>
                                        <div class="product__offer">
                                            <span class="discount">-15%</span>
                                        </div>
                                        <div class="product-action">
                                            <a href="#" class="icon-box icon-box-1" data-bs-toggle="modal" data-bs-target="#productModalId">
                                                <i class="fal fa-eye"></i>
                                                <i class="fal fa-eye"></i>
                                            </a>
                                            <a href="#" class="icon-box icon-box-1">
                                                <i class="fal fa-heart"></i>
                                                <i class="fal fa-heart"></i>
                                            </a>
                                            <a href="#" class="icon-box icon-box-1">
                                                <i class="fal fa-layer-group"></i>
                                                <i class="fal fa-layer-group"></i>
                                            </a>
                                        </div>
                                    </div>
                                </div>
                                <div class="col-md-6">
                                    <div class="product__content product__content-d">
                                        <h6><a href="product-details.html">{{ i.name }}a></h6>
                                        <div class="rating mb-5">
                                            <ul class="rating-d">
                                                <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                <li><a href="#"><i class="fal fa-star"></i></a></li>
                                            </ul>
                                            <span>(01 review)</span>
                                        </div>
                                        <div class="price d-price mb-10">
                                            <span>$307.00 <del>$110</del></span>
                                        </div>
                                        <div class="features-des mb-25">
                                            <ul>
                                                <li><a href="product-details.html"><i class="fas fa-circle"></i> Bass and Stereo Sound.</a></li>
                                                <li><a href="product-details.html"><i class="fas fa-circle"></i> Display with 3088 x 1440 pixels resolution.</a></li>
                                                <li><a href="product-details.html"><i class="fas fa-circle"></i> Memory, Storage &amp; SIM: 12GB RAM, 256GB.</a></li>
                                                <li><a href="product-details.html"><i class="fas fa-circle"></i> Androi v10.0 Operating system.</a></li>
                                            </ul>
                                        </div>
                                        <div class="cart-option">
                                            <a href="cart.html" class="cart-btn-2 w-100 mr-10">Add to Cart</a>
                                            <a href="cart.html" class="transperant-btn"><i class="fal fa-heart"></i></a>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
           
                 {% endfor %}
                    <div class="col-xl-6 col-lg-12">
                        <div class="row">
                        {% for products in product %}
                            <div class="col-md-6">
                                <div class="single-features-item b-radius mb-20">
                                    <div class="row  g-0 align-items-center">
                                        <div class="col-6">
                                            <div class="features-thum">
                                                <div class="features-product-image w-img">
                                                    <a href="product-details.html"><img src="{{ products.image.url }}" alt=""></a>
                                                </div>
                                                <div class="product__offer">
                                                    <span class="discount">-15%</span>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="col-6">
                                            <div class="product__content product__content-d">
                                                <h6><a href="product-details.html">{{ products.name }}</a></h6>
                                                <div class="rating mb-5">
                                                    <ul>
                                                        <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                        <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                        <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                        <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                        <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                    </ul>
                                                    <span>(01 review)</span>
                                                </div>
                                                <div class="price d-price">
                                                    <span>$307.00 <del>$110</del></span>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                         
                         {% endfor %}
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <!-- featured-end -->

        <!-- moveing-text-area-start -->
        <section class="moveing-text-area">
            <div class="container">
                <div class="ovic-running">
                    <div class="wrap">
                        <div class="inner">
                            <p class="item">Free UK Delivery - Return Over $100.00 ( Excluding Homeware )   |   Free UK Collect From Store</p>
                            <p class="item">Design Week / 15% Off the website / Code: AYOSALE-2020</p>
                            <p class="item">Always iconic. Now organic. Introducing the $20 Organic Tee.</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <!-- moveing-text-area-end -->

        <!-- banner__area-start -->
        <section class="banner__area pt-60 pb-25">
            <div class="container">
                <div class="row">
                {% for footer_banners in footer_banner %}
                    <div class="col-xl-4 col-lg-6 col-md-12">
                        <div class="banner__item p-relative w-img mb-30">
                            <div class="banner__img">
                                <a href="product-details.html"><img src="{{ footer_banners.image.url }}" alt=""></a>
                            </div>
                            <div class="banner__content banner__content-sd text-center">
                                <div class="banner-button mb-20">
                                    <a href="product-details.html" class="st-btn">HOT DEALS</a>
                                </div>
                                <h6><a href="product-details.html">Sale 30% Off <br> Top Computer Case Gaming</a></h6>
                            </div>
                        </div>
                    </div>
                  {% endfor %}
                 
            
        </section>
        <!-- banner__area-end -->

        <!-- recomand-product-area-start -->
        <section class="recomand-product-area">
            <div class="container">
                <div class="row">
                    <div class="col-xl-12">
                        <div class="section__head d-flex justify-content-between mb-10">
                            <div class="section__title">
                                <h5 class="st-titile">Recommended For You</h5>
                            </div>
                            <div class="button-wrap">
                                <a href="shop.html">See All Product <i class="fal fa-chevron-right"></i></a>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="row g-0">
                    <div class="product-bs-slider-2">
                        <div class="product-slider-3 swiper-container">
                            <div class="swiper-wrapper">
                            {% for products in product %}
                                <div class="product__item mb-20 swiper-slide">
                                    <div class="product__thumb fix">
                                        <div class="product-image w-img">
                                            <a href="{% url 'product_detail' products.slug %}">
                                                <img src="{{ products.image.url }}" alt="product">
                                            </a>
                                        </div>
                                        <div class="product__offer">
                                        <span class="discount">-15%</span>
                                        </div>
                                        <div class="product-action">
                                            <a href="#" class="icon-box icon-box-1" data-bs-toggle="modal" data-bs-target="#productModalId">
                                                <i class="fal fa-eye"></i>
                                                <i class="fal fa-eye"></i>
                                            </a>
                                            <a href="#" class="icon-box icon-box-1">
                                                <i class="fal fa-heart"></i>
                                                <i class="fal fa-heart"></i>
                                            </a>
                                            <a href="#" class="icon-box icon-box-1">
                                                <i class="fal fa-layer-group"></i>
                                                <i class="fal fa-layer-group"></i>
                                            </a>
                                        </div>
                                    </div>
                                    <div class="product__content">
                                        <h6><a href="{% url 'product_detail' products.slug %}">{{ products.name }}</a></h6>
                                        <div class="rating mb-5">
                                            <ul>
                                                <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                <li><a href="#"><i class="fal fa-star"></i></a></li>
                                                <li><a href="#"><i class="fal fa-star"></i></a></li>
                                            </ul>
                                            <span>(01 review)</span>
                                        </div>
                                        <div class="price">
                                           {% if products.regular_discount_price %}
                                            <span>${{ products.regular_discount_price }}-<del>${{ products.price }}</del></span>
                                           {% else %}
                                             <span>${{ products.price }}</span>
                                           {% endif %}
                                        </div>
                                    </div>
                                    <div class="product__add-cart text-center">
                                        <a href="{% url 'addcart' products.id %}"  class="cart-btn product-modal-sidebar-open-btn d-flex align-items-center justify-content-center w-100">
                                        Add to Cart
                                        </a>
                                    </div>
                                </div>
                                {% endfor %}
                         
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <!-- recomand-product-area-end -->

        <!-- brand-area-start -->
        <section class="brand-area brand-area-d">
            <div class="container">
                <div class="brand-slider swiper-container pt-50 pb-45">
                    <div class="swiper-wrapper">
                        <div class="brand-item w-img swiper-slide">
                            <a href="#"><img src="{% static ''%}assets/img/brand/brand-1.jpg" alt="brand"></a>
                        </div>
                        <div class="brand-item w-img swiper-slide">
                            <a href="#"><img src="{% static ''%}assets/img/brand/brand-2.jpg" alt="brand"></a>
                        </div>
                        <div class="brand-item w-img swiper-slide">
                            <a href="#"><img src="{% static ''%}assets/img/brand/brand-3.jpg" alt="brand"></a>
                        </div>
                        <div class="brand-item w-img swiper-slide">
                            <a href="#"><img src="{% static ''%}assets/img/brand/brand-4.jpg" alt="brand"></a>
                        </div>
                        <div class="brand-item w-img swiper-slide">
                            <a href="#"><img src="{% static ''%}assets/img/brand/brand-5.jpg" alt="brand"></a>
                        </div>
                        <div class="brand-item w-img swiper-slide">
                            <a href="#"><img src="{% static ''%}assets/img/brand/brand-6.jpg" alt="brand"></a>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <!-- brand-area-end -->
        
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
                                    <a href="#"><img src="{% static ''%}assets/img/brand/app_ios.png" alt=""></a>
                                    <a href="#"><img src="{% static ''%}assets/img/brand/app_android.png" alt=""></a>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

        </section>
        <!-- cta-area-end -->
     {% for p in product %}
        <!-- shop modal start -->
        <div class="modal fade" id="productModalId" tabindex="-1" role="dialog" aria-hidden="true">
            <div class="modal-dialog modal-dialog-centered product__modal" role="document">
                <div class="modal-content">
                    <div class="product__modal-wrapper p-relative">
                        <div class="product__modal-close p-absolute">
                            <button data-bs-dismiss="modal"><i class="fal fa-times"></i></button>
                        </div>
                        <div class="product__modal-inner">
                            <div class="row">
                            <div class="col-xl-6 col-lg-6 col-md-6 col-sm-12 col-12">
                                <div class="product__modal-box">
                                    <div class="tab-content" id="modalTabContent">
                                        <div class="tab-pane fade show active" id="nav1" role="tabpanel" aria-labelledby="nav1-tab">
                                            <div class="product__modal-img w-img">
                                                <img src="{{ p.image.url }}" alt="">
                                            </div>
                                        </div>
                                        <div class="tab-pane fade" id="nav2" role="tabpanel" aria-labelledby="nav2-tab">
                                            <div class="product__modal-img w-img">
                                                <img src="{% static ''%}assets/img/quick-view/quick-view-2.jpg" alt="">
                                            </div>
                                        </div>
                                        <div class="tab-pane fade" id="nav3" role="tabpanel" aria-labelledby="nav3-tab">
                                            <div class="product__modal-img w-img">
                                                <img src="{% static ''%}assets/img/quick-view/quick-view-3.jpg" alt="">
                                            </div>
                                        </div>
                                        <div class="tab-pane fade" id="nav4" role="tabpanel" aria-labelledby="nav4-tab">
                                            <div class="product__modal-img w-img">
                                                <img src="{% static ''%}assets/img/quick-view/quick-view-4.jpg" alt="">
                                            </div>
                                        </div>
                                        </div>
                                    <ul class="nav nav-tabs" id="modalTab" role="tablist">
                                        <li class="nav-item" role="presentation">
                                            <button class="nav-link active" id="nav1-tab" data-bs-toggle="tab" data-bs-target="#nav1" type="button" role="tab" aria-controls="nav1" aria-selected="true">
                                                <img src="{% static ''%}assets/img/quick-view/quick-nav-1.jpg" alt="">
                                            </button>
                                        </li>
                                        <li class="nav-item" role="presentation">
                                            <button class="nav-link" id="nav2-tab" data-bs-toggle="tab" data-bs-target="#nav2" type="button" role="tab" aria-controls="nav2" aria-selected="false">
                                            <img src="{% static ''%}assets/img/quick-view/quick-nav-2.jpg" alt="">
                                            </button>
                                        </li>
                                        <li class="nav-item" role="presentation">
                                            <button class="nav-link" id="nav3-tab" data-bs-toggle="tab" data-bs-target="#nav3" type="button" role="tab" aria-controls="nav3" aria-selected="false">
                                            <img src="{% static ''%}assets/img/quick-view/quick-nav-3.jpg" alt="">
                                            </button>
                                        </li>
                                        <li class="nav-item" role="presentation">
                                            <button class="nav-link" id="nav4-tab" data-bs-toggle="tab" data-bs-target="#nav4" type="button" role="tab" aria-controls="nav4" aria-selected="false">
                                            <img src="{% static ''%}assets/img/quick-view/quick-nav-4.jpg" alt="">
                                            </button>
                                        </li>
                                        </ul>
                                </div>
                            </div>
                            <div class="col-xl-6 col-lg-6 col-md-6 col-sm-12 col-12">
                                <div class="product__modal-content">
                                    <h4><a href="product-details.html">{{ p.name }}</a></h4>
                                    <div class="product__review d-sm-flex">
                                        <div class="rating rating__shop mb-10 mr-30">
                                        <ul>
                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                            <li><a href="#"><i class="fal fa-star"></i></a></li>
                                        </ul>
                                        </div>
                                        <div class="product__add-review mb-15">
                                        <span>01 review</span>
                                        </div>
                                    </div>
                                    <div class="product__price">
                                        <span>$109.00 – $307.00</span>
                                    </div>
                                    <div class="product__modal-des mt-20 mb-15">
                                        <ul>
                                            <li><a href="#"><i class="fas fa-circle"></i> Bass and Stereo Sound.</a></li>
                                            <li><a href="#"><i class="fas fa-circle"></i> Display with 3088 x 1440 pixels resolution.</a></li>
                                            <li><a href="#"><i class="fas fa-circle"></i> Memory, Storage & SIM: 12GB RAM, 256GB.</a></li>
                                            <li><a href="#"><i class="fas fa-circle"></i> Androi v10.0 Operating system.</a></li>
                                        </ul>
                                    </div>
                                    <div class="product__stock mb-20">
                                        <span class="mr-10">Availability :</span>
                                        <span>1795 in stock</span>
                                    </div>
                                    <div class="product__modal-form">
                                        <form action="#">
                                        <div class="pro-quan-area d-lg-flex align-items-center">
                                            <div class="product-quantity mr-20 mb-25">
                                                <div class="cart-plus-minus p-relative"><input type="text" value="1" /></div>
                                            </div>
                                            <div class="pro-cart-btn mb-25">
                                                <button class="cart-btn" type="submit">Add to cart</button>
                                            </div>
                                        </div>
                                        </form>
                                    </div>
                                    <div class="product__stock mb-30">
                                        <ul>
                                            <li><a href="#">
                                                <span class="sku mr-10">SKU:</span>
                                                <span>Samsung C49J89: £875, Debenhams Plus</span></a>
                                            </li>
                                            <li><a href="#">
                                                <span class="cat mr-10">Categories:</span>
                                                <span>iPhone, Tablets</span></a>
                                            </li>
                                            <li><a href="#">
                                                <span class="tag mr-10">Tags:</span>
                                                <span>Smartphone, Tablets</span></a>
                                            </li>
                                        </ul>
                                    </div>
                                </div>
                            </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!-- shop modal end -->
        {% endfor %}

    </main>
   
{%endblock%}