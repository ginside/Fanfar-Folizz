$( document ).ready(function() {
	$('.image a').click(function (e) {
		$('#imageModal .modal-dialog').removeClass('modal-lg');
		$('#imageModal img').attr('src', $(this).attr('data-img-url'));
		$('#modalTitle').html($(this).attr('data-img-title'));
		
		var img = new Image();
		img.onload = function() {
			if(img.width > 900) {
				$('#imageModal .modal-dialog').addClass('modal-lg');
			}
		}
		img.src=$(this).attr('data-img-url');
	});
});