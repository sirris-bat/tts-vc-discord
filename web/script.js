function WebSocketConnect(url) {
    // Connect to websocket
    var websocket_connect = new WebSocket(url);
    
    websocket_connect.onopen = function(e) {
        alert('[open] Connection established');
        alert(`Sending to ${url}`);
        websocket_connect.send();
    };

    websocket_connect.onmessage = function(event) {
        alert('[message] Data received from server: ${event.data}');
    };

    websocket_connect.onclose = function(event) {
        if (event.wasClean) {
            alert(`[close] Connection closed cleanly, code=${event.code} reason=${event.reason}`);
        } else {
            // e.g. server process killed or network down
            // event.code is usually 1006 in this case
            alert('[close] Connection died');
        }
    };

    websocket_connect.onerror = function(error) {
        alert(`[error] ${error.message}`)
    };
}

window.addEventListener("load", function(){
    // Logic for connect websocket
    function sendConnect() {
        const channel_id = (new FormData(connect_form)).get("channelId");
        const websocket = `ws://${window.location.host}/connect/${channel_id}`;
        WebSocketConnect(websocket);
    }

    // Logic for say websocket
    function sendSay() {
        alert("Not yet implemented")
    }


    // Setup event listener for connect websocket
    const connect_form = document.getElementById("connectForm");
    connect_form.addEventListener("submit", function(event) {
        event.preventDefault();
        sendConnect();
    });

    // Setup event listener for say websocket
    const say_form = document.getElementById("sayForm");
    say_form.addEventListener("submit", function(event) {
        event.preventDefault();
        sendSay();
    });
});
