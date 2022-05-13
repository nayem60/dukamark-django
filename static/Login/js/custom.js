// -------------------------------  -(Start) -----------------------------------//

const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('container');

signUpButton.addEventListener('click', () => {
	container.classList.add("right-panel-active");
});

signInButton.addEventListener('click', () => {
	container.classList.remove("right-panel-active");
});

// -------------------------------  -(END) ------------------------------------//


// -------------------------------- WOW -(Start) ----------------------------------------- //
new WOW().init();
// -------------------------------- WOW -(END) ----------------------------------------- //

// ------------------------------ Back TO TOP (Start) ----------------------------------- //
(function (a) {
	a.fn.tottTop = function (f) {
		var b = a.extend({
			scrollTop: 800,
			duration: 1E3,
			scrtollTopBtnDuration: 1000
		}, f);
		return this.each(function () {
			var c = a(this),
				d = a(window);
			d.scroll(function () {
				d.scrollTop() > b.scrollTop ? c.fadeIn(b.scrtollTopBtnDuration) : c.fadeOut(b.scrtollTopBtnDuration)
			});
			c.click(e)
		})
	}
})(jQuery);
$('.totop').tottTop();
// ----------------------------- Back TO TOP (End) ------------------------------------ //
