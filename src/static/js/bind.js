var data=[];

function addBr(text){
    return text.replace(/\n/g, "<br />");

}
var Message;
Message = function (arg) {
    this.text = arg.text, this.message_side = arg.message_side;
    this.draw = function (_this) {
        return function () {
            var $message;
            $message = $($('.message_template').clone().html());
            $message.addClass(_this.message_side).find('.text').html(addBr(_this.text));
            $('.messages').append($message);
            return setTimeout(function () {
                return $message.addClass('appeared');
            }, 0);
        };
    }(this);
    return this;
};


function showBotMessage(msg){
        message = new Message({
             text: msg,
             message_side: 'left'
        });
        message.draw();
        $messages.animate({ scrollTop: $messages.prop('scrollHeight') }, 300);
}
function showUserMessage(msg){
        $messages = $('.messages');
        message = new Message({
            text: msg,
            message_side: 'right'
        });
        message.draw();
        $messages.animate({ scrollTop: $messages.prop('scrollHeight') }, 300);
        $('#msg_input').val('');
}
function thumb(){
    // function thumbsup(){
    var button= document.createElement("div");
    // button.innerText= String.fromCodePoint(0x1F44D, 0x1F44E);
    button.innerHTML= '<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6"><path stroke-linecap="round" stroke-linejoin="round" d="M7.498 14.25H4.372c-1.026 0-1.945-.694-2.054-1.715a12.137 12.137 0 01-.068-1.285c0-2.848.992-5.464 2.649-7.521C5.287 3.247 5.886 3 6.504 3h4.016a4.5 4.5 0 011.423.23l3.114 1.04a4.5 4.5 0 001.423.23h1.294M7.498 14.25c.618 0 .991.724.725 1.282A7.471 7.471 0 007.5 18.75 2.25 2.25 0 009.75 21a.75.75 0 00.75-.75v-.633c0-.573.11-1.14.322-1.672.304-.76.93-1.33 1.653-1.715a9.04 9.04 0 002.86-2.4c.498-.634 1.226-1.08 2.032-1.08h.384m-10.253 1.5H9.7m8.075-9.75c.01.05.027.1.05.148.593 1.2.925 2.55.925 3.977 0 1.487-.36 2.89-.999 4.125m.023-8.25c-.076-.365.183-.75.575-.75h.908c.889 0 1.713.518 1.972 1.368.339 1.11.521 2.287.521 3.507 0 1.553-.295 3.036-.831 4.398-.306.774-1.086 1.227-1.918 1.227h-1.053c-.472 0-.745-.556-.5-.96a8.95 8.95 0 00.303-.54" /></svg>'
    button.style.float= "right";
    button.style.cursor = "pointer";
    var text = document.getElementsByClassName("messages")[0];
    text.appendChild(button);
    button.addEventListener("click",function(){
<<<<<<< HEAD
        alert("Your response has been stored");
=======
        alert("Your response has been registered!");
>>>>>>> main
    })
 }
// function thumb(){
//     var button= document.createElement("div");
//     // button.innerText= String.fromCodePoint(0x1F44D, 0x1F44E);
//     button.innerHTML= '<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6"><path stroke-linecap="round" stroke-linejoin="round" d="M7.498 14.25H4.372c-1.026 0-1.945-.694-2.054-1.715a12.137 12.137 0 01-.068-1.285c0-2.848.992-5.464 2.649-7.521C5.287 3.247 5.886 3 6.504 3h4.016a4.5 4.5 0 011.423.23l3.114 1.04a4.5 4.5 0 001.423.23h1.294M7.498 14.25c.618 0 .991.724.725 1.282A7.471 7.471 0 007.5 18.75 2.25 2.25 0 009.75 21a.75.75 0 00.75-.75v-.633c0-.573.11-1.14.322-1.672.304-.76.93-1.33 1.653-1.715a9.04 9.04 0 002.86-2.4c.498-.634 1.226-1.08 2.032-1.08h.384m-10.253 1.5H9.7m8.075-9.75c.01.05.027.1.05.148.593 1.2.925 2.55.925 3.977 0 1.487-.36 2.89-.999 4.125m.023-8.25c-.076-.365.183-.75.575-.75h.908c.889 0 1.713.518 1.972 1.368.339 1.11.521 2.287.521 3.507 0 1.553-.295 3.036-.831 4.398-.306.774-1.086 1.227-1.918 1.227h-1.053c-.472 0-.745-.556-.5-.96a8.95 8.95 0 00.303-.54" /></svg>'
//    button.style.float= "right";
//     button.style.cursor = "pointer";
//     var text = document.getElementsByClassName("messages")[0];
//     var btn= text.appendChild(button);
    
// }
function sayToBot(text){
    document.getElementById("msg_input").placeholder = "Type your messages here..."
    $.post("/chat",
            {
                //csrfmiddlewaretoken:csrf,
                text:text,
            },
            function(jsondata, status){
                if(jsondata["status"]=="success"){
                    response=jsondata["response"];

                    if(response){showBotMessage(response);
                    thumb();}
                }
            });

}

getMessageText = function () {
            var $message_input;
            $message_input = $('.message_input');
            return $message_input.val();
        };

$("#say").keypress(function(e) {
    if(e.which == 13) {
        $("#saybtn").click();
    }
});

$('.send_message').click(function (e) {
        msg = getMessageText();
        if(msg){
        showUserMessage(msg);
        sayToBot(msg);
    $('.message_input').val('');}
});

$('.message_input').keyup(function (e) {
    if (e.which === 13) {
        msg = getMessageText();
        if(msg){
        showUserMessage(msg);
        sayToBot(msg);
    $('.message_input').val('') ;}
    }
});


// Pop up

function openForm() {
    document.getElementById("display").style.display = "block";
  }
  
  function closeForm() {
    document.getElementById("display").style.display = "none";
  }
  