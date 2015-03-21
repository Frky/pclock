
var ws4redis;

var receiveData = function(data) {
    console.log("Received: " + data);
    data = JSON.parse(data)
    console.log("Let's change it");
    $("#" + data.type + "_lap").text(data.laps);
}


$(document).ready(function() {
    var ws4redis = WS4Redis({
        uri: ws_uri + "pclock?subscribe-broadcast",
        receive_message: receiveData,
        heartbeat_msg: ws_heartbeat,
    });
});
