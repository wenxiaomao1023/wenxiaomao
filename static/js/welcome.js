$(function showWelcomeText() {
	tx = $(window).width() - $(".welcomeText").width();
	ty = $(window).height() / 2 - $(".welcomeText").height() * 2;
	tx2 = $(window).width() - $(".welcomeText2").width();
	ty2 = $(window).height() / 2 - $(".welcomeText2").height();
	tx3 = $(window).width() - $(".welcomeText3").width();
	ty3 = $(window).height() / 2;
	cx = ($(window).width() - $(".welcomeText").width()) / 2 - 198;
	cy = $(window).height() - $(".car").height();
	$(".welcomeText").css("display", "block");
	showWelcomeTextTimer();
})

function showWelcomeTextTimer() {
	if (tx <= ($(window).width() - $(".welcomeText").width()) / 2) {
		if (tx != ($(window).width() - $(".welcomeText").width()) / 2) {
			tx = ($(window).width() - $(".welcomeText").width()) / 2;
			$(".welcomeText").css({
				"left" : tx,
				"top" : ty
			});
		}
		$(".welcomeText2").css("display", "block");
		showWelcomeText2Timer();
		return;
	}
	$(".welcomeText").css({
		"left" : tx,
		"top" : ty
	});
	tx -= 5;
	setTimeout(showWelcomeTextTimer, 1);
}

function showWelcomeText2Timer() {
	if (tx2 <= ($(window).width() - $(".welcomeText2").width()) / 2) {
		if (tx2 != ($(window).width() - $(".welcomeText2").width()) / 2) {
			tx2 = ($(window).width() - $(".welcomeText2").width()) / 2;
			$(".welcomeText2").css({
				"left" : tx2,
				"top" : ty2
			});
		}
		$(".welcomeText3").css("display", "block");
		showWelcomeText3Timer();
		return;
	}
	$(".welcomeText2").css({
		"left" : tx2,
		"top" : ty2
	});
	tx2 -= 5;
	setTimeout(showWelcomeText2Timer, 1);
}

function showWelcomeText3Timer() {
	if (tx3 <= ($(window).width() - $(".welcomeText3").width()) / 2) {
		if (tx3 != ($(window).width() - $(".welcomeText3").width()) / 2) {
			tx3 = ($(window).width() - $(".welcomeText3").width()) / 2;
			$(".welcomeText3").css({
				"left" : tx3,
				"top" : ty3
			});
		}

		setTimeout(function() {
			$(".car").css("display", "block");
			showCarTimer();
		}, 2000);
		// showCarTimer();
		return;
	}
	$(".welcomeText3").css({
		"left" : tx3,
		"top" : ty3
	});
	tx3 -= 5;
	setTimeout(showWelcomeText3Timer, 1);
}

function showCarTimer() {
	if (cy <= ty - 15) {
		if (cy != ty - 15) {
			cy = ty - 15;
			$(".car").css({
				"left" : cx,// tx-195
				"top" : cy
			// ty-15
			});
		}
		// cx = tx-196;
		showCarDrivingTimer();
		return;
	}
	$(".car").css({
		"left" : cx,// tx-195
		"top" : cy
	// ty-15
	});
	cy -= 2;
	setTimeout(showCarTimer, 2);
}

function showCarDrivingTimer() {
	if (cx < 0 - $(".car").width()) {
		location.href = "/index";
		return;
	}
	$(".welcomeText").css({
		"left" : tx,
		"top" : ty
	});
	$(".welcomeText2").css({
		"left" : tx2,
		"top" : ty2
	});
	$(".welcomeText3").css({
		"left" : tx3,
		"top" : ty3
	});
	$(".car").css({
		"left" : cx,
		"top" : cy
	});
	tx -= 2;
	tx2 -= 2;
	tx3 -= 2;
	cx -= 2;
	setTimeout(showCarDrivingTimer, 1);
}