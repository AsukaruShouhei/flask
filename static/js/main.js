
$(function(){
// 設定
    var $width =1280; // 横幅
    var $height =528; // 高さ
    var $interval = 8000; // 切り替わりの間隔（ミリ秒）
    var $fade_speed = 1200; // フェード処理の早さ（ミリ秒）
    $("#slide ul li").css({"position":"relative","overflow":"hidden","width":$width,"height":$height});
    $("#slide ul li").hide().css({"position":"absolute"});
    $("#slide ul li:first").addClass("active").show();

    setInterval(function(){
        var $active = $("#slide ul li.active");
        var $next = $active.next("li").length?$active.next("li"):$("#slide ul li:first");
        $active.fadeOut($fade_speed).removeClass("active");
        $next.fadeIn($fade_speed).addClass("active");
    },
    $interval);
});