$(document).ready(function(){
    function getCookie(c_name) {
        if(document.cookie.length > 0) {
            c_start = document.cookie.indexOf(c_name + "=");
            if(c_start != -1) {
                c_start = c_start + c_name.length + 1;
                c_end = document.cookie.indexOf(";", c_start);
                if(c_end == -1) c_end = document.cookie.length;
                return unescape(document.cookie.substring(c_start,c_end));
            }
        }
        return "";
    }
    $(function () {
        $.ajaxSetup({
            headers: {
                "X-CSRFToken": getCookie("csrftoken")
            }
        });
    });
});

function post_new(user_id){
    var text = newtext.value;
    var currentUser = user_id;
    var json = JSON.stringify({"text":text, "user":currentUser});
    // alert(json)
    var url = window.location.href;

    function get_hostname(url) {
            var m = url.match(/^http:\/\/[^/]+/);
            return m ? m[0] : null;
        }

    var posUrl = get_hostname(url) + '/api/data/'
    // alert(posUrl)

    $.ajax({
        type: "POST",
        url: posUrl,
        data: json,
        success: function(){},
        dataType: "json",
        contentType : "application/json"
        });

    $('#newtext').each(
        function () {
            $(this).val($(this).data('defvalue'));
        });
};