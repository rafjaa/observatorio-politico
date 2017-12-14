$(function(){
	function split(v) {
		return v.split(/,\s*/)
	}

	function extractLast(term) {
		return split(term).pop()
	}

	function setsearch(si) {
		si.keydown(function(e){
			if (e.keyCode === $.ui.keyCode.TAB && $(this).autocomplete('instance').menu.active)
				e.preventDefault()
		}).autocomplete({
			source: function(request, response){
				$.ajax('ajaxtag.php', {
					method: 'POST',
					data: {
						tag: extractLast(request.term)
					},
					success: response
				})
			},
			search: function(){
				var term = extractLast(this.value);
				if (term.length < 2) return false
			},
			focus: function(){
				return false
			},
			select: function(event, ui){
				var terms = split(this.value);
				terms.pop();
				terms.push(ui.item.value);
				terms.push('');
				this.value = terms.join(', ');
				return false
			}
		})
	}

	if ($('body#main')[0]) {
		var ms = $('#mainsearcher'), tc = $('#tagcloud').addClass('format'), ctc = 1, sf = $('#searchform'), si = $('#searchfield input');

		function scroll(t){
			t = document.documentElement.scrollTop || document.body.scrollTop;
			if (ctc && t + document.documentElement.clientHeight > tc.offset().top + tc.height() / 2) {
				ctc = 0;
				tc.jQCloud(words, {autoResize: true, delay: 4, encodeURI: false})
			}
			sf.css('opacity', Math.max(Math.min(1 + (sf.offset().top - t) / sf.height() * 3 / 2, 1), 0))
		}

		function resize(m){
			m = Math.max(parseInt(((document.documentElement.clientHeight - $('#menuheader').height()) * .92 - sf.height()) / 2), 20);
			sf.css({marginTop: m, marginBottom: m});
			$('#parallax').trigger('resize.px.parallax');
			scroll()
		}

		$('#searchfield').click(function(e){
			if (e.target != si[0]) si.focus()
		});

		setsearch(si);

		$(window).resize(resize).scroll(scroll);
		resize()
	} else if ($('body#results')[0]) {
		$('#entitiesrange').ionRangeSlider({
			hide_min_max: true,
			keyboard: true,
			min: -1,
			max: 1,
			from: _np,
			to: _xp,
			type: 'double',
			step: .05,
			grid: true
		}).change(function(){
			var s = this.value.split(';');
			$('#np').val(s[0]);
			$('#xp').val(s[1])
		});

		$('.gauge').each(function(){
			var g = new Gauge($(this).find('canvas')[0]).setOptions({
				lines: 12,
				angle: 0,
				lineWidth: 0.4,
				pointer: {
					length: 0.75,
					strokeWidth: 0.042,
					color: '#1D212A'
				},
				colorStart: '#1ABC9C',
				colorStop: '#1ABC9C',
				strokeColor: '#F0F3F3',
				generateGradient: true,
				staticZones: [
					{strokeStyle: "rgb(255,0,0)", min: -1, max: -.6},
					{strokeStyle: "rgb(200,100,0)", min: -.6, max: -.2},
					{strokeStyle: "rgb(150,150,0)", min: -.2, max: .2},
					{strokeStyle: "rgb(100,200,0)", min: .2, max: .6},
					{strokeStyle: "rgb(0,255,0)", min: .6, max: 1}
				],
				highDpiSupport: true
			});
			g.minValue = -1;
			g.maxValue = 1;
			g.animationSpeed = 32;
			g.set($(this).data('compound'))
		});

		setsearch($('#entitiesfilter'));

		function setcontent(b) {
			$('#newscontentdata').html(b.data('content') || 'Falha ao buscar notícia.')
		}

		$('.viewnews').click(function(){
			var b = $(this);
			if (b.data('content') != undefined)
				setcontent(b);
			else {
				$('#newscontentdata').html('<i class="glyphicon glyphicon-hourglass"></i> Buscando notícia... Por favor, aguarde...');
				$.ajax('ajaxnews.php', {
					method: 'POST',
					data: {
						id: b.closest('.result').data('id')
					},
					success: function(r){
						b.data('content', r);
						setcontent(b)
					}
				})
			}
			$('#newscontent').modal()
		})
	} else
		// Workaround para o bug do tooltip do NV.
		// Faz que o height da página fique maior quando
		// sai de uma tela muito pequena para uma maior
		// e deixa um espaço enorme vazio na parte inferior
		// da página.
		$(window).resize(function(){
			$('.nvtooltip').css('transform', '')
		});

	setsearch($('#headersearch'))
})
