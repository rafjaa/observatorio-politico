<?php
require(__DIR__ . DIRECTORY_SEPARATOR . 'classes' . DIRECTORY_SEPARATOR . 'loader.php');

SearcherHTML::setTitle('Partidos');

SearcherHTML::addCSSFile('nv.d3.css');

SearcherHTML::addJSFile('popper.min.js');
SearcherHTML::addJSFile('d3.min.js');
SearcherHTML::addJSFile('nv.d3.min.js');
SearcherHTML::addJSFile('parties.js');
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
						Partidos
					</div>
				</div>
				<div class="container">
					<div class="row">
						<div class="col-lg-12">
							<h2 class="upper">Avaliação dos partidos com base nas notícias referentes a cada um.</h2>
							<h2 class="light">Foram avaliadas as notícias de cada site individualmente.</h2>
						</div>
					</div>
					<hr/>

					<div class="row">
						<div class="col-sm-6">
							<h2>Agência Brasil</h2>
							<h5>agenciabrasil.ebc.com.br</h5>
							<div class="chart1 chart">
								<svg></svg>
							</div>
						</div>
						<div class="col-sm-6">
							<h2>G1</h2>
							<h5>g1.globo.com</h5>
							<div class="chart2 chart">
								<svg></svg>
							</div>
						</div>
					</div>
					<hr/>

					<div class="row">
						<div class="col-sm-6">
							<h2>No Minuto</h2>
							<h5>nominuto.com</h5>
							<div class="chart3 chart">
								<svg></svg>
							</div>
						</div>
						<div class="col-sm-6">
							<h2>O Tempo</h2>
							<h5>otempo.com</h5>
							<div class="chart4 chart">
								<svg></svg>
							</div>
						</div>
					</div>
					<hr/>

					<div class="row">
						<div class="col-sm-6">
							<h2>Política Livre</h2>
							<h5>politicalivre.com.br</h5>
							<div class="chart5 chart">
								<svg></svg>
							</div>
						</div>
						<div class="col-sm-6">
							<h4 class="text-center">Partidos por número de notícias</h4>
							<div class="chart6 chart size2">
								<svg></svg>
							</div>
						</div>
					</div>
				</div>
			</div>
			<?php require(__DIR__ . DIRECTORY_SEPARATOR . 'template' . DIRECTORY_SEPARATOR . 'footer.php'); ?>
		</div>
	</body>
</html>
