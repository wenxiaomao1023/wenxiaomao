//coverSrc 120*120
//var audiopath="http://pan.baidu.com/disk/home#path=%252Fwenspace%252Faudio%252F";
//	/alidata/server/tomcat-7.0.54/webapps/wenspace/audio
var jsonObj = [ {
	songName : "In A World Like This",
	songTime : "03:41",
	songSrc : "static/audio/aud11.mp3",
	coverSrc : "static/img/audioplayer/cover/aud11.png",
	singer : "Backstreet Boys",
}, {
	songName : "All Of Me",
	songTime : "04:26",
	songSrc : "static/audio/aud10.mp3",
	coverSrc : "static/img/audioplayer/cover/aud10.png",
	singer : "John Legend",
}, {
	songName : "See You Again",
	songTime : "03:49",
	songSrc : "static/audio/aud.mp3",
	coverSrc : "static/img/audioplayer/cover/aud.png",
	singer : "Wiz Khalifa、Charlie Puth",
}, {
	songName : "If I Were A Boy",
	songTime : "04:10",
	songSrc : "static/audio/aud2.mp3",
	coverSrc : "static/img/audioplayer/cover/aud2.png",
	singer : "Beyonce",
}, {
	songName : "Love The Way You Lie",
	songTime : "04:56",
	songSrc : "static/audio/aud3.mp3",
	coverSrc : "static/img/audioplayer/cover/aud3.png",
	singer : "Eminem、Rihanna",
}, {
	songName : "可惜没如果",
	songTime : "04:58",
	songSrc : "static/audio/aud5.mp3",
	coverSrc : "static/img/audioplayer/cover/aud5.png",
	singer : "林俊杰",
}, {
	songName : "向往",
	songTime : "03:59",
	songSrc : "static/audio/aud6.mp3",
	coverSrc : "static/img/audioplayer/cover/aud6.png",
	singer : "李健",
}, {
	songName : "Girlfriend",
	songTime : "03:37",
	songSrc : "static/audio/aud7.mp3",
	coverSrc : "static/img/audioplayer/cover/aud7.png",
	singer : "Avril Lavigne",
}, ];

// 所有的歌曲
var audioList = new Array();
audioList = jsonObj;
var onClickPause = 0;// 防止用户点击开始或暂停按钮时 执行监听方法
var pauseState = 0;
var onclickPauseFromPlayList = 0;
var currentIndex = 0;
var currentModel = 0;// 0 列表循环 1 单曲循环
var currentAudio = audioList[currentIndex].songSrc;
/*
 * 传值的一种方法
function test(i){
	return function() {
		var index=i;
		var row = document.getElementsByName('listrow');
		row[currentIndex].style.backgroundColor = "#fff";
		if (index == currentIndex) {
			onclickPauseFromPlayList = 1;
		}
		this.style.backgroundColor = "#df8";
		playAudioFromList(index);
	};
}*/
function initPlayList() {
	var context = "";
	for (var i = 0; i < audioList.length; i++) {
		context += "<tr style='cursor:pointer' name=listrow index=" + i + ">"
		// +"<td><a
		// href=javascript:playAudioFromList("+i+")>"+audioList[i].songName+"</a></td>"
		+ "<td>" + audioList[i].songName + "</td>" + "<td>"
				+ audioList[i].singer + "</td>" + "</tr>"
	}
	document.getElementById('playlist').innerHTML = context;
	var row = document.getElementsByName('listrow');
	for (var i = 0; i < row.length; i++) {
		if (i == currentIndex) {
			row[i].style.backgroundColor = "#df8";
		}
		row[i].onclick = function() {
			var index = parseInt(this.getAttribute("index"));
			row[currentIndex].style.backgroundColor = "#fff";
			if (index == currentIndex) {
				onclickPauseFromPlayList = 1;
			}
			this.style.backgroundColor = "#df8";
			playAudioFromList(index);
		}
		/*
		 * 传值的一种方法
		row[i].onclick = test(i);
		*/
		row[i].onmouseout = function() {
			var index = parseInt(this.getAttribute("index"));
			if (index != currentIndex) {
				this.style.backgroundColor = "#fff";
			}
		}
		row[i].onmouseover = function() {
			var index = parseInt(this.getAttribute("index"));
			if (index != currentIndex) {
				this.style.background = "#6cf";
			}
		}
	}
}

function playAudioFromList(index) {
	if (index < 0 || index > audioList.length - 1)
		return;
	currentIndex = index;
	currentAudio = audioList[currentIndex].songSrc;
	updateAudioPlayerInfoPanel();
	playAudio();
}

function secondToTime(value) {
	var s = parseInt(value);// 秒
	var m = 0;// 分
	// var h = 0;// 小时
	if (s >= 60) {
		m = parseInt(s / 60);
		s = parseInt(s % 60);
		/*
		 * if (m > 60) { h = parseInt(m / 60); m = parseInt(m % 60); }
		 */
	}
	if (s < 10)
		s = "0" + s;
	var result = s;

	if (m < 10)
		m = "0" + m;

	result = m + ":" + result;

	return result;
}
// display and update progress bar
function progressBar() {
	var oAudio = document.getElementById('myaudio');
	// get current time in seconds
	var elapsedTime = Math.round(oAudio.currentTime);
	document.getElementById('songtime').textContent = secondToTime(elapsedTime)
			+ "/" + audioList[currentIndex].songTime;
	// update the progress bar
	if (canvas.getContext) {
		var ctx = canvas.getContext("2d");
		// clear canvas before painting
		// ctx.clearRect(0, 0, canvas.clientWidth, canvas.clientHeight);
		ctx.fillStyle = "rgb(230,230,230)";
		ctx.fillRect(0, 0, canvas.clientWidth, canvas.clientHeight);
		ctx.fillStyle = "rgb(250,0,0)";
		var fWidth = (elapsedTime / oAudio.duration) * (canvas.clientWidth);
		if (fWidth > 0) {
			ctx.fillRect(0, 0, fWidth, canvas.clientHeight);
		}
	}
}

function updateAudioPlayerInfoPanel() {
	if (onclickPauseFromPlayList == 1) {
		onclickPauseFromPlayList = 0;
		return;
	}
	document.getElementById('myaudio').currentTime = 0;
	progressBar();
	document.getElementById('songname').textContent = audioList[currentIndex].songName;
	document.getElementById('songtime').textContent = "00:00/"
			+ audioList[currentIndex].songTime;
	document.getElementById('singer').textContent = audioList[currentIndex].singer;
	if (audioList[currentIndex].coverSrc != "")
		document.getElementById("cover").src = audioList[currentIndex].coverSrc;
	else
		document.getElementById("cover").src = "static/img/audioplayer/cover/default.png";
	var row = document.getElementsByName('listrow');
	row[currentIndex].style.backgroundColor = "#df8";
}

// Play and pause function
function playAudio() {
	try {
		// return objects we need to work with
		var oAudio = document.getElementById('myaudio');
		// var btn = document.getElementById('play');
		// var audioURL = document.getElementById('audiofile');

		// Skip loading if current file hasn't changed.
		if (currentAudio !== tmpAudio) {
			oAudio.src = currentAudio;
			// currentAudio = tmpAudio;
			tmpAudio = currentAudio;

		}

		// Tests the paused attribute and set state.
		if (oAudio.paused) {
			oAudio.play();
			// btn.textContent = "Pause";
			document.getElementById("btn_start").src = "static/img/audioplayer/btn_pause.png";
		} else {
			onClickPause = 1;
			oAudio.pause();
			// btn.textContent = "Play";
			document.getElementById("btn_start").src = "static/img/audioplayer/btn_start.png";
		}
	} catch (e) {
		// Fail silently but show in F12 developer tools console
		if (window.console && console.error("Error:" + e))
			;
	}
}

function preAudio() {
	if (currentIndex - 1 < 0)
		return;
	var row = document.getElementsByName('listrow');
	row[currentIndex].style.backgroundColor = "#fff";
	currentAudio = audioList[--currentIndex].songSrc;
	updateAudioPlayerInfoPanel();
	if (pauseState == 0) {
		playAudio();
	}
}

function nextAudio() {
	if (currentIndex + 1 > audioList.length - 1)
		return;
	var row = document.getElementsByName('listrow');
	row[currentIndex].style.backgroundColor = "#fff";
	currentAudio = audioList[++currentIndex].songSrc;
	updateAudioPlayerInfoPanel();
	if (pauseState == 0) {
		playAudio();
	}
}

function continueAudio() {
	var row = document.getElementsByName('listrow');
	row[currentIndex].style.backgroundColor = "#fff";
	currentIndex++;
	if (currentIndex > audioList.length - 1)
		currentIndex = 0;
	currentAudio = audioList[currentIndex].songSrc;
	updateAudioPlayerInfoPanel();
	playAudio();
}

function listLoopModel() {
	// 开启列表循环
	if (currentModel != 0) {
		currentModel = 0;
		document.getElementById("btn_singleloop").src = "static/img/audioplayer/btn_singleloop_unselect.png";
		document.getElementById("btn_listloop").src = "static/img/audioplayer/btn_listloop_select.png";
		$("#myaudio").removeAttr('loop');
	}
}

function singleLoopModel() {
	// 开启单曲循环
	if (currentModel != 1) {
		currentModel = 1;
		document.getElementById("btn_singleloop").src = "static/img/audioplayer/btn_singleloop_select.png";
		document.getElementById("btn_listloop").src = "static/img/audioplayer/btn_listloop_unselect.png";
		$("#myaudio").attr('loop', 'loop');
	}
}

function downloadAudio(){
	//location.href="download.action?file="+audioList[currentIndex].songSrc;
	var url="download.action?file="+audioList[currentIndex].songSrc;
	window.open(url,"_blank");
}
/*
 * //Rewinds the audio file by 30 seconds. function rewindAudio() { try { var
 * oAudio = document.getElementById('myaudio'); oAudio.currentTime -= 5.0; }
 * catch (e) { // Fail silently but show in F12 developer tools console if
 * (window.console && console.error("Error:" + e)) ; } }
 * 
 * //Fast forwards the audio file by 30 seconds. function forwardAudio() { try {
 * var oAudio = document.getElementById('myaudio'); oAudio.currentTime += 5.0; }
 * catch (e) { // Fail silently but show in F12 developer tools console if
 * (window.console && console.error("Error:" + e)) ; } }
 * 
 * //Restart the audio file to the beginning. function restartAudio() { try {
 * var oAudio = document.getElementById('myaudio'); oAudio.currentTime = 0; }
 * catch (e) { // Fail silently but show in F12 developer tools console if
 * (window.console && console.error("Error:" + e)) ; } }
 */
// added events
function initEvents() {
	var canvas = document.getElementById('canvas');
	var oAudio = document.getElementById('myaudio');
	// 初始化
	oAudio.src = currentAudio;
	tmpAudio = currentAudio;
	// updateAudioPlayerInfoPanel();
	document.getElementById('songname').textContent = audioList[currentIndex].songName;
	document.getElementById('songtime').textContent = "00:00/"
			+ audioList[currentIndex].songTime;
	document.getElementById('singer').textContent = audioList[currentIndex].singer;
	if (audioList[currentIndex].coverSrc != "")
		document.getElementById("cover").src = audioList[currentIndex].coverSrc;
	else
		document.getElementById("cover").src = "static/img/audioplayer/cover/default.png";

	document.getElementById("btn_singleloop").src = "static/img/audioplayer/btn_singleloop_unselect.png";
	document.getElementById("btn_listloop").src = "static/img/audioplayer/btn_listloop_select.png";
	initPlayList();

	// set up event to toggle play button to pause when playing
	oAudio
			.addEventListener(
					"playing",
					function() {
						// document.getElementById("play").textContent =
						// "Pause";
						pauseState = 0;
						document.getElementById("btn_start").src = "static/img/audioplayer/btn_pause.png";
					}, true);

	// set up event to toggle play button to play when paused
	oAudio
			.addEventListener(
					"pause",
					function() {
						// document.getElementById("play").textContent = "Play";
						pauseState = 1;
						document.getElementById("btn_start").src = "static/img/audioplayer/btn_start.png";
						if (onClickPause == 1) {
							onClickPause = 0;
							return;
						}
						// alert("over");
						if (currentModel == 0) {
							continueAudio();
						}
					}, true);
	// set up event to update the progress bar
	oAudio.addEventListener("timeupdate", progressBar, true);
	// set up mouse click to control position of audio
	canvas.addEventListener("click", function(e) {
		// this might seem redundant, but this these are needed later - make
		// global to remove these
		var oAudio = document.getElementById('myaudio');
		var canvas = document.getElementById('canvas');

		if (!e) {
			e = window.event;
		} // get the latest windows event if it isn't set
		try {
			// calculate the current time based on position of mouse cursor in
			// canvas box
			oAudio.currentTime = oAudio.duration
					* (e.offsetX / canvas.clientWidth);
		} catch (err) {
			// Fail silently but show in F12 developer tools console
			if (window.console && console.error("Error:" + err))
				;
		}
	}, true);
}
// this event gets fired when a page has loaded
window.addEventListener("DOMContentLoaded", initEvents, false);