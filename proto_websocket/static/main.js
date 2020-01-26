function initWebSocket() {
  ws = new WebSocket("ws://localhost:8000/websocket");

  ws.onopen = function() {
    console.log("Connected.")
  };

  ws.onmessage = function(e) {
    message = e.data;
    console.log(countLinebreak(message));

    if(message.slice(0,3) === "___"){
      // message is a completion list
      console.log(message);
    }else{
      // message is a result of input command
      var elm = document.getElementById("myOutput");
      elm.innerHTML = col_b(message);
    }
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
  var incomplete_word = document.getElementById("myInput").value;
  ws.send("___" + incomplete_word);
}

const ENTER = 13;
input.addEventListener("keyup", function(event) {
  event.preventDefault();
  if (event.keyCode === ENTER) {
    sendCommand();
  }
  else{
    sendIncompleteWord();
  }
});