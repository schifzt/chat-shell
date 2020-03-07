const myInput = document.getElementById("myInput");
const myOutput = document.getElementById("myOutput");

function initWebSocket() {
  ws = new WebSocket("ws://localhost:8000/websocket");

  ws.onopen = function() {
    console.log("Connected.")
  };

  ws.onmessage = function(e) {
    var message = e.data;

    if(message.slice(0,3) === "___"){
      // message is a completion list
      completions = message.slice(3, ).split("\n");
      myOutput.innerHTML = completions;
      // setAutocomplete(completions);
    }else{
      // message is a result of input command
      console.log(countLinebreak(message));
      myOutput.innerHTML = col_b(message);
    }
  };
}

window.onload = new function() {
  initWebSocket();
}

sendCommand = function() {
  var cmd = myInput.value;
  ws.send(cmd);
}

sendIncompleteWord = function() {
  var incomplete_word = myInput.value.split(" ").pop();
  console.log(incomplete_word);
  ws.send("___" + incomplete_word);
}

const ENTER = 13;
myInput.addEventListener("keyup", function(event) {
  event.preventDefault();
  if (event.keyCode === ENTER) {
    sendCommand();
  }
  else{
    sendIncompleteWord();
  }
});

