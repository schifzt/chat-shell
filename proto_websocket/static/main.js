function initWebSocket() {
  ws = new WebSocket("ws://localhost:8000/websocket");

  ws.onopen = function() {
    console.log("Connected.")
  };

  ws.onmessage = function(e) {
    var elm = document.getElementById("myOutput");
    console.log(countLinebreak(e.data));
    elm.innerHTML = col_b(e.data);
  };
}

window.onload = new function() {
  initWebSocket();
}

sendCommand = function() {
  var cmd = document.getElementById("myInput").value;
  ws.send(cmd);
}

sendIncompleteWord = function() {
  var chr = document.getElementById("myInput").value;
  ws.send("___"+chr);
}

/* "Enter" calls sendCommand() function. */
var input = document.getElementById("myInput");
input.addEventListener("keyup", function(event) {
  event.preventDefault();
  if (event.keyCode === 13) {
    sendCommand();
  }
  else{
    sendIncompleteWord();
  }
});