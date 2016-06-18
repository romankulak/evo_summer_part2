
$(function() {

var textarray = [
 "пресвятейший",
 "суперсвятейший",
    "жгучий",
 "могучий",
 "дремучий"    // No comma after last entry
];

function RndText() {
  var rannum= Math.floor(Math.random()*textarray.length);
  document.getElementById('ShowText').innerHTML=textarray[rannum];
}




    // Submit post on submit
    $('#post-form').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!")  // sanity check

        create_post();
        //RndText();
    });

    // AJAX for posting
function create_post() {
    console.log("create post is working!") // sanity check
    $.ajax({
        url : "create_post/", // the endpoint
        type : "POST", // http method
        data : { the_post : $('#post-text').val() }, // data sent with the post request

        // handle a successful response
            success : function(json) {
                $('#post-text').val(''); // remove the value from the input
                console.log(json); // log the returned json to the console
                $("#talk").prepend("<li><strong>Рад тебя видеть снова,</strong> <strong id='ShowText'> </strong> <strong>" +json.text+"</strong></li>");
                console.log("success"); // another sanity check
                RndText();
            },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
};

});
