$(function(){
/* IE6 FIx
 -------------------------------------------------------- */
if(/msie/i.test(navigator.userAgent)){
	window.PNGImage=0;

	$('#contents img[src*=\'.png\']').each(function(){
		$(this).after('<span></span>');

		$(this).next()
			.attr({
				'id':$(this).attr('id'),
				'class':$(this).attr('class'),
				'title':$(this).attr('alt')
			})
			.css({
				'display':'inline-block',
				'width':$(this).width()+'px',
				'height':$(this).height()+'px',
				'filter':'progid:DXImageTransform.Microsoft.AlphaImageLoader(src='+$(this).attr('src')+')',
				'zoom':1
			});

		$(this).remove();

		window.PNGImage++;
	});

	$('#contents a span').css('cursor','pointer');
}




/* init
 -------------------------------------------------------- */
	$('#contents .visualArea h1').css({
		'opacity':0
	});

	$('#contents .visualArea ol li.scene2 dl dt').css({'opacity':0});
	$('#contents .visualArea ol li.scene2 dl dd').css({
		'opacity':0,
		'left':'-532px'
	});

	$('#contents .visualArea ol li.scene3 dl dt').css({'opacity':0});
	$('#contents .visualArea ol li.scene3 dl dd').css({
		'opacity':0,
		'right':'-581px'
	});




/* animation
 -------------------------------------------------------- */
	var animation=function(){
		$('#contents .visualArea h1')
			.animate({
				'opacity':1,
				'top':'-148px'
			},1000,function(){
				//scene1
				$('#contents .visualArea ol li.scene1').fadeIn(2000,function(){
					setTimeout(function(){
						//scene2
						$('#contents .visualArea ol li.scene2').fadeIn(1000,function(){
							$('#contents .visualArea ol li.scene2 dl dd').animate({
								'opacity':1,
								'left':'0px'
							},3000,function(){
								$('#contents .visualArea ol li.scene2 dl dt').animate({
									'opacity':1
								},3000,function(){
									setTimeout(function(){
										//scene3
										$('#contents .visualArea ol li.scene3').fadeIn(1000,function(){
											$('#contents .visualArea ol li.scene3 dl dd').animate({
												'opacity':1,
												'right':'0px'
											},3000,function(){
												$('#contents .visualArea ol li.scene3 dl dt').animate({
													'opacity':1
												},3000,function(){
													setTimeout(function(){
														//scene4
														$('#contents .visualArea ol li.scene4').fadeIn(3000);
													},3000);
												});
											});
										});
									},3000);
								});
							});
						});
					},2000);
				});
			});
	}

	if(!/msie\s6./i.test(navigator.userAgent))animation();
	else{
		(function(){
			if(window.PNGImage==17)animation();
			else setTimeout(arguments.callee,0);return;
		})();
	}
});