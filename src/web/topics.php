<?php
require(__DIR__ . DIRECTORY_SEPARATOR . 'classes' . DIRECTORY_SEPARATOR . 'loader.php');

SearcherHTML::setTitle('Análise de tópicos');

SearcherHTML::addCSSFile('ion.rangeSlider.css');
SearcherHTML::addCSSFile('ion.rangeSlider.skinFlat.css');

SearcherHTML::addJSFile('ion.rangeSlider.min.js');
SearcherHTML::addJSFile('Chart.min.js');
SearcherHTML::addJSFile('script.js');
?>
<!DOCTYPE html>
<html lang="pt-BR">
	<head>
		<?php echo SearcherHTML::getHeadTags(); ?>
	</head>
	<body id="topics">
		<div id="parallax" data-parallax="scroll" data-image-src="template/images/newspapers.jpg">
			<?php require(__DIR__ . DIRECTORY_SEPARATOR . 'template' . DIRECTORY_SEPARATOR . 'header.php'); ?>
			<div id="topicscontainer">
				<div class="containertitle">
					<div class="container">
						Entidades
					</div>
				</div>
				<div class="container">
					<div class="row">
						<main>
						</main>
						<div class="clearfix"></div>
						<div class="footer">
							<div>
								<strong>Granularidade dos tópicos:</strong> <span id="span_n_topicos"></span>
							</div>
							<div id="range"></div>
						</div>
					</div>
				</div>
			</div>
			<?php require(__DIR__ . DIRECTORY_SEPARATOR . 'template' . DIRECTORY_SEPARATOR . 'footer.php'); ?>
		</div>
	</body>
</html>
