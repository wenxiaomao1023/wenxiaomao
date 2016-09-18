var sizeChangeFlag = 0;

$(document).ready(function() {
	/*换肤*/
	setBackgroundSkin();
	//监听滚动条的变化
	/*
	$(window).scroll(function() {
		windowsSizeChange();
	});
	 */
	//监听浏览器大小变化
	$(window).bind("resize", windowsSizeChange);
	
	document.getElementsByTagName("body")[0].onclick = function(e) {
		//获取事件对象 
		e = e || window.event;//IE和Chrome下是window.event FF下是e 
		//获取事件源 
		var target = e.target || e.srcElement;//IE和Chrome下是srcElement FF下是target 
		//alert(target.tagName);
		var op = $(".setup-wallpaper-pop").css("opacity");
		if (op == 1 && !(target.tagName == "A")) {
			$(".setup-wallpaper-pop").css("z-index", "-1");
			$("#setup-wall-pop").removeClass("setup-wallpaper-pop-show");
		}
	}
});

function windowsSizeChange() {
	sizeChangeFlag = 1;
	setupWallpaperPop();
}
function setupWallpaperPop() {
	var posLeft = $(".header").css("margin-left")
			+ $(".header").css("width");
	var op = $(".setup-wallpaper-pop").css("opacity");
	$(".setup-wallpaper-pop").css("top", 75);
	$(".setup-wallpaper-pop").css("right", parseInt(posLeft) + 5);
	if (sizeChangeFlag != 1) {
		if (op == 0) {
			$(".setup-wallpaper-pop").css("z-index", "100");
			$("#setup-wall-pop").addClass("setup-wallpaper-pop-show");
		} else {
			$(".setup-wallpaper-pop").css("z-index", "-1");
			$("#setup-wall-pop")
					.removeClass("setup-wallpaper-pop-show");
		}
	}
	sizeChangeFlag = 0;
}
function setWallpaper(i) {
	window.sessionStorage.skin = i;
	setBackgroundSkin();
}
//设置网页背景
function setBackgroundSkin() {
	// document.getElementsByTagName("body").css
	if ("undefined" == typeof (window.sessionStorage.skin))
		window.sessionStorage.skin = 1;
	var skin = "bg_skin_" + window.sessionStorage.skin;
	$("body").removeClass();
	$("body").addClass(skin);
}