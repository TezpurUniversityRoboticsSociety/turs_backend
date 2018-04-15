$(document).scroll(function() {

	var y=$(this).scrollTop();
	var x=$('.layer2text').position();
	// Navbar
		if(y > (x.top + 70)) {
			$('.navbar').addClass('shrink');
			$('.layer2text').removeClass('removed');
			$('.nav-link').removeClass('navlinkcol1')
			$('.nav-link').addClass('navlinkcol2');
		}
		else {

			$('.navbar').removeClass('shrink');
			$('.nav-link').addClass('navlinkcol1');
			$('.nav-link').removeClass('navlinkcol2');
		}
 });

//Scroll to desired sections on nav-bar clicks
$(document).ready(function(){
	// Add smooth scrolling to all links
	$(".slide-section").on('click', function(event) {
  
	  // Make sure this.hash has a value before overriding default behavior
	  if (this.hash !== "") {
		// Prevent default anchor click behavior
		event.preventDefault();
  
		// Store hash
		var hash = this.hash;
  
		// Using jQuery's animate() method to add smooth page scroll
		// The optional number (800) specifies the number of milliseconds it takes to scroll to the specified area
		$('html, body').animate({
		  scrollTop: $(hash).offset().top
		}, 'slow', function(){
	 
		  // Add hash (#) to URL when done scrolling (default click behavior)
		  window.location.hash = hash;
		});
	  } // End if
	});
  });


// For the first button to animate on hover
$(".btn-lg").hover(
	function() {
		$(this).addClass("bounce");
	},
	function() {
		$(this).removeClass("bounce");
	}
)

// Go to ABOUT US section on clicking EXPLORE button
  $(".btn-lg").click(function() {
    $('html,body').animate({
        scrollTop: $("#about").offset().top},
        'slow');
});



