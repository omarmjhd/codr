var notes_ws = new WebSocket("ws://codr.cloudapp.net:8888/api/notifications");
var chat_ws = new WebSocket("ws://codr.cloudapp.net:8888/api/chat");


// notifications
notes_ws.onmessage = function (evt) {
    alert('You matched with ' + evt.data);
};

