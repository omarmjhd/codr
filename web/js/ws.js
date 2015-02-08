var ws = new WebSocket("ws://codr.cloudapp.net:8888/api/notifications");

ws.onopen = function() {
    // do something
};

ws.onmessage = function (evt) {
    alert('You matched with ' + evt.data);
};

