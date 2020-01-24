function initWebSocket() {
  ws = new WebSocket("ws://localhost:8000/websocket");

  ws.onopen = function() {
    console.log("Connected.")
  };

  ws.onmessage = function(e) {
    var output = document.getElementById("myOutput");
    output.innerText = e.data;
  };
}

window.onload = new function() {
  initWebSocket();
}

sendCommand = function() {
  var cmd = document.getElementById("myInput").value;
  ws.send(cmd);
}

// Press "Enter" call sendCommand() function.
var input = document.getElementById("myInput");
input.addEventListener("keyup", function(event) {
  if (event.keyCode === 13) {
	  event.preventDefault();
	  document.getElementById("myBtn").click();
  }
});