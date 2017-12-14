<?php
require(__DIR__ . DIRECTORY_SEPARATOR . 'classes' . DIRECTORY_SEPARATOR . 'loader.php');

SearcherHTML::setTitle('Lava Jato');

SearcherHTML::addCSSFile('nv.d3.css');

SearcherHTML::addJSFile('popper.min.js');
SearcherHTML::addJSFile('d3.min.js');
SearcherHTML::addJSFile('nv.d3.min.js');
SearcherHTML::addJSFile('lavajato.js');
?>
<!DOCTYPE html>
<html lang="pt-BR">
	<head>
		<?php echo SearcherHTML::getHeadTags(); ?>
	</head>
	<body id="candidates">
		<div id="parallax" data-parallax="scroll" data-image-src="template/images/newspapers.jpg">
			<?php require(__DIR__ . DIRECTORY_SEPARATOR . 'template' . DIRECTORY_SEPARATOR . 'header.php'); ?>
			<div id="candidatescontainer">
				<div class="containertitle">
					<div class="container">
						Lava Jato
					</div>
				</div>
				<div class="container">
					<div class="row">
						<div class="col-sm-12">
							<br/>
							<h1 class="text-uppercase">Operação Lava Jato</h1>
							<h3>Os políticos que mais aparecem nas notícias de investição da Lava Jato. </h3>
						</div>
					</div>
					<hr/>

					<div class="row">
						<div class="col">
							<div class="chart1 chart">
								<svg></svg>
							</div>
						</div>
					</div>
					<hr/>

					<div class="row">
						<div class="col-sm-5">
							<div class="img-intro">
								<img src="images/lula.jpg" alt="" />
								<h2>Lula</h2>
							</div>
							<h2 class="text-uppercase">O nome mais citado!</h2>
							<h2 class="light">Das <b>3320</b> notícias em que aparece, <b>1041</b> citam a Lava Jato.</h2>
						</div>
						<div class="col-sm-7">
							<br/>
							<h5 class="text-center">Quantidade de notícias sobre a Lava Jato por site.</h5>
							<br/>
							<div class="chart8 size2 chart box">
								<svg></svg>
							</div>
						</div>
					</div>
					<hr/>
				</div>
			</div>
			<?php require(__DIR__ . DIRECTORY_SEPARATOR . 'template' . DIRECTORY_SEPARATOR . 'footer.php'); ?>
		</div>
	</body>
</html>
