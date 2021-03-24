function WebSocketConnect(url, message = null) {
    var websocket_connect = new WebSocket(url);
    
    websocket_connect.onopen = function(e) {
        console.log(`Sending to ${url}`);
        websocket_connect.send(message);
    };

    websocket_connect.onmessage = function(event) {
        console.log('[message] Data received from server: ${event.data}');
    };

    websocket_connect.onclose = function(event) {
        if (event.wasClean) {
            console.log(`[close] Connection closed cleanly, code=${event.code} reason=${event.reason}`);
        } else { console.log('[close] Connection died'); }
    };

    websocket_connect.onerror = function(error) { console.log(`[error] ${error.message}`) };
}

window.addEventListener("load", function(){
    // Logic for connect websocket
    function sendConnect() {
        const channel_id = (new FormData(connect_form)).get("channelId");
        const websocket = `ws://${window.location.host}/ws/connect/${channel_id}`;
        WebSocketConnect(websocket);
    }

    // Logic for say websocket
    function sendSay() {
        const phrase = (new FormData(say_form)).get("phrase");
        const websocket = `ws://${window.location.host}/ws/say`;
        WebSocketConnect(websocket, phrase);
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

    // Update h1 to match deployed app name
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200){
            let response = JSON.parse(xhr.responseText);
            document.getElementById("appname").innerHTML = response.appname;
        }  
    }
    xhr.open('GET', `http://${window.location.host}/appname`, true);
    xhr.send();
});
