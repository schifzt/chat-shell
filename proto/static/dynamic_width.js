function resizable (elm, factor) {
    // var int = Number(factor) || 7.7;
    function resize(){
        elm.style.width = ((elm.value.length + 1) * factor) + 'px'
    }
    elm.addEventListener("keypress", resize, false);
    resize();
}

resizable(document.getElementById('myInput'), 10);