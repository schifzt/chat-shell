const TAB = 9;
// const ENTER = 13;
setAutocomplete = (function (tags) {
	var availableTags = tags;
	$("input#myInput").autocomplete({
		source: availableTags,
		autoFocus: true,
		// focus : function(e, ui) {
		// 	if(e.keyCode === ENTER) return false;
		// }
	});
});

// $("#menu").menu();

// // Hover states on the static widgets
// $("#dialog-link, #icons li").hover(
// 	function () {
// 		$(this).addClass("ui-state-hover");
// 	},
// 	function () {
// 		$(this).removeClass("ui-state-hover");
// 	}
// );