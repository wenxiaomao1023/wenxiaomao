//var STATIC="http://127.0.0.1:8000/static/";

//获取参数
function getParameter(name) {
	var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)");
	var r = window.location.search.substr(1).match(reg);
	if (r != null)
		return unescape(r[2]);
	return null;
}

// 验证邮箱格式
function isEmail(str) {
	var reg = /^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+(.[a-zA-Z0-9_-])+/;
	return reg.test(str);
}

//验证空格
function existBlank(elementId) {
	var obj = document.getElementById(elementId);
	var str = obj.value;
	if (str.indexOf(" ") >= 0){
		//alert("输入有空格！");
		return true;
	}else{
		return false;
	}
	//obj.value = str.replace(/\s/g, ""); // 这句话可以强制删除所有空格
}