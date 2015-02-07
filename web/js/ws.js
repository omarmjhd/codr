var ws = new WebSocket("ws://codr.cloudapp.net/api/notifications");

ws.onopen = function() {
    alert('opened');
};

ws.onmessage = function (evt) {
   alert(evt.data);
};

