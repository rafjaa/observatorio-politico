$(function(){
	if ($('#main')[0]) {
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
			m = Math.max(parseInt((document.documentElement.clientHeight * .92 - sf.height()) / 2), 20);
			sf.css({marginTop: m, marginBottom: m});
			$('#parallax').trigger('resize.px.parallax');
			scroll()
		}

		function split(v) {
			return v.split(/,\s*/)
		}

		function extractLast(term) {
			return split(term).pop()
		}

		$('#searchfield').click(function(e){
			if (e.target != si[0]) si.focus()
		});

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
		});

		$(window).resize(resize).scroll(scroll);
		resize()
	}
})
