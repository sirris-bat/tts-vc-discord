function WebSocketConnect(channel_id) {
    if ('WebSocket in Window'){
        alert('WebSocket support detected, proceeding...');

        // Connect to websocket
        var websocket_connect = new('ws://localhost:4000/connect/'.concat(channel_id));
        
        websocket_connect.onopen = function(e) {
            alert('[open] Connection established');
            alert('Sending to server');
            websocket_connect.send();
        };

        websocket_connect.onmessage = function(event) {
            alert('[message] Data received from server: ${event.data}');
        };

        websocket_connect.onclose = function(event) {
            if (event.wasClean) {
                alert('[close] Connection closed cleanly, code=${event.code} reason=${event.reason}');
            } else {
                // e.g. server process killed or network down
                // event.code is usually 1006 in this case
                alert('[close] Connection died');
            }
        };

        websocket_connect.onerror = function(error) {
            alert('[error] ${error.message}')
        };

    } else {
        alert('WebSockets are NOT supported by your browser!');
    }
}
