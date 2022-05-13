  {% load static %}
  <!-- slider-area-start -->
        <div class="slider-area">
        {% for sliders in slider %}
            <div class="swiper-container slider__active">
                <div class="slider-wrapper swiper-wrapper">
                    <div class="single-slider swiper-slide slider-height d-flex align-items-center" data-background="{{ sliders.image.url }}">
                        <div class="container">
                            <div class="row">
                                <div class="col-xl-5">
                                    <div class="slider-content">
                                        <div class="slider-top-btn" data-animation="fadeInLeft" data-delay="1.5s">
                                            <a href="product-details.html" class="st-btn b-radius">{{ sliders.types }}</a>
                                        </div>
                                        <h2 data-animation="fadeInLeft" data-delay="1.7s" class="pt-15 slider-title pb-5">{{ sliders.first_caption }}</h2>
                                        <p class="pr-20 slider_text" data-animation="fadeInLeft" data-delay="1.9s">{{ sliders.last_captiop }}</p>
                                        <div class="slider-bottom-btn mt-75">
                                            <a data-animation="fadeInUp" data-delay="1.15s" href="shop.html" class="st-btn-b b-radius">{{ sliders.action_text }}</a>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div><!-- /single-slider -->
                   
                    {% endfor %}
                 
                    <div class="main-slider-paginations"></div>
                </div>
            </div>
        </div>