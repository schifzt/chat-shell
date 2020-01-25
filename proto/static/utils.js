function col_b(str){
    return(
        str.replace(/\n/g, "<br>")
        .replace(/ /g, "<span class=\"space\">s</span>")
        .replace(/\t/g, "<span class=\"tab\">4tab</span>")
        .replace(/(.)[\b]\1/g, "<span class=\"highlight\">$1</span>")
        .replace(/_[\b](.)/g, "<span class=\"underline\">$1</span>")
    );
}