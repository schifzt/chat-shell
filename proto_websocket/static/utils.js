function countLinebreak(text){
    return(text.match(/\n/g).length);
}

function foldLine(n_foldstart){
    // var elm = document.getElementById("myOutput");
    // var style = window.getComputedStyle(elm);
    return(style);
}

function col_b(text){
    return(
        text.replace(/\n/g, "<br>")
        .replace(/ /g, "<span class=\"space\">s</span>")
        .replace(/\t/g, "<span class=\"tab\">ssss</span>")
        .replace(/(.)[\b]\1/g, "<span class=\"highlight\">$1</span>")
        .replace(/_[\b](.)/g, "<span class=\"underline\">$1</span>")
    );
}