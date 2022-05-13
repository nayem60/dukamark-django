{%load static%}

 <!doctype html>

 <html lang="en">



 <head>

 	<meta charset="utf-8">

 	<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

 	<meta name="keywords" content="MJ Maraz, Web Design, Web Development, Responsive web Design, IT, Freelancing">

 	<meta name="author" content="MJ Maraz">

 	<title>login/singup</title>

 	<link rel="shortcut icon" type="image" href="image/pab-icon.png">

 	<link rel="stylesheet" href="{%static 'Login'%}/css/bootstrap.min.css">

 	<link rel="stylesheet" href="{%static 'Login'%}/css/fontawesome.css">
 		<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta2/css/all.min.css">

 	<link rel="stylesheet" href="{%static 'Login'%}/css/style.css">

 	<link rel="stylesheet" href="{%static 'Login'%}/css/responsive.css">

 </head>

 <!-- ====================== Design by - "mjmarazbd.com"  =================================== -->



 <body >



 	<!-- ---------------------------------------------------------------------------------------------- -->

 	<!-- >>>>>>>>>> LOGIN = (START) >>>>>>>> -->

 	<section id="" class="login_part ptb">



 		<div class="container" id="container">



 			

 			<div class="form-container sign-up-container">

 				<form action="{% url 'registration' %}"method="post">
 						{%csrf_token%}

 					<h1>Create Account</h1>

 					<div class="social-container">

 						<a href="#" class="social1"><i class="fab fa-facebook-f"></i></a>

 						<a href="#" class="social2"><i class="fab fa-google-plus-g"></i></a>

 						<a href="#" class="social3"><i class="fab fa-linkedin-in"></i></a>

 					</div>

 					<div class="input"><i class="far fa-user"></i> <input type="text" name="username"placeholder="Username" /></div>
 					<div class="input"><i class="far fa-envelope"></i> <input type="email" name="email"placeholder="Email" /></div>

 					<div class="input"><i class="fas fa-unlock-alt"></i> <input type="password" name="password1"placeholder="Password" /></div>
 					<div class="input"><i class="fas fa-unlock-alt"></i> <input type="password" name="password2"placeholder="Confirm Password" /></div>

 					<button>Sign Up</button>

 				</form>

 			</div>

 			<div class="form-container sign-in-container">

 				<form action=""method="post">
 				
 				{% csrf_token %}

 					<h1>Login</h1>

 					<div class="social-container">

 						<a href="#" class="social"><i class="fab fa-facebook-f"></i></a>

 						<a href="#" class="social"><i class="fab fa-google-plus-g"></i></a>

 						<a href="#" class="social"><i class="fab fa-linkedin-in"></i></a>

 					</div>

 					<span>or use your account</span>

 					<div class="input"><i class="far fa-envelope"></i> <input type="text" name="username" placeholder="Username" /></div>

 					<div class="input"><i class="fas fa-unlock-alt"></i> <input type="password" name="password"placeholder="Password" /></div>

 					<a href="#">Forgot your password?</a>

 					<button>logIn</button>

 				</form>

 			</div>

 			<div class="overlay-container">

 				<div class="overlay">

 					<div class="overlay-panel overlay-left">

 						<h1>Welcome Back!</h1>

 						<p>To keep connected with us please login with your personal info</p>

 						<button class="ghost" id="signIn">Login</button>

 					</div>

 					<div class="overlay-panel overlay-right">

 						<h1>Hello, Friend!</h1>

 						<p>Enter your personal details and start journey with us</p>

 						<button class="ghost" id="signUp">Sign Up</button>

 					</div>

 				</div>

 			</div>

 		</div>





 	</section>

 	<!-- <<<<<<<<< LOGIN = (ENDS) <<<<<<<<< -->

 	<!-- ---------------------------------------------------------------------------------------------- -->



 	<!-- ============================================================================================ -->

 	<script src="{%static 'Login'%}/js/jquery-3.5.1.min.js"></script>

 	<script src="{%static 'Login'%}/js/bootstrap.bundle.min.js"></script>

 	<script src="{%static 'Login'%}/js/custom.js"></script>
 	<script src="https://unpkg.com/sweetalert/dist/sweetalert.min.js"></script>
 

 	<!-- ============================================================================================= -->

 </body>



 </html>

