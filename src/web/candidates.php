<?php
require(__DIR__ . DIRECTORY_SEPARATOR . 'classes' . DIRECTORY_SEPARATOR . 'loader.php');

SearcherHTML::setTitle('Candidatos a presidência');

SearcherHTML::addCSSFile('nv.d3.css');

SearcherHTML::addJSFile('popper.min.js');
SearcherHTML::addJSFile('d3.min.js');
SearcherHTML::addJSFile('nv.d3.min.js');
SearcherHTML::addJSFile('candidates.js');
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
						Candidatos
					</div>
				</div>
				<div class="container">
					<div class="row">
						<div class="col-lg-12">
							<h2 class="upper">Avaliação dos pré-cantidados com base nas notícias referentes a cada um.</h2>
							<h2 class="light">Foram avaliadas as notícias onde o cantidato aparece com relevância.</h2>
						</div>
					</div>
					<hr/>

					<div class="row">
						<div class="col-sm-4">
							<div class="img-intro">
								<img src="images/lula.jpg" alt="" />
								<h2>Lula</h2>
							</div>
							<p>Aparece em: <b>3320</b> notícias.<br/>
								A média de polaridade foi de: <b>-0.1199</b>.</p>
						</div>
						<div class="col-sm-8">
							<div class="chart1 chart">
								<svg></svg>
							</div>
						</div>
					</div>
					<hr/>

					<div class="row">
						<div class="col-sm-4">
							<div class="img-intro">
								<img src="images/haddad.jpg" alt="" />
								<h2>Haddad</h2>
							</div>
							<p>Aparece em: <b>84</b> notícias.<br/>
								A média de polaridade foi de: <b>-0.0362</b>.</p>
						</div>
						<div class="col-sm-8">
							<div class="chart2 chart">
								<svg></svg>
							</div>
						</div>
					</div>
					<hr/>

					<div class="row">
						<div class="col-sm-4">
							<div class="img-intro">
								<img src="images/ciro-gomes.jpg" alt="" />
								<h2>Ciro Gomes</h2>
							</div>
							<p>Aparece em: <b>86</b> notícias.<br/>
								A média de polaridade foi de: <b>-0.0206</b>.</p>
						</div>
						<div class="col-sm-8">
							<div class="chart3 chart">
								<svg></svg>
							</div>
						</div>
					</div>
					<hr/>

					<div class="row">
						<div class="col-sm-4">
							<div class="img-intro">
								<img src="images/marina.jpg" alt="" />
								<h2>Marina</h2>
							</div>
							<p>Aparece em: <b>189</b> notícias.<br/>
								A média de polaridade foi de: <b>-0.1152</b>.</p>
						</div>
						<div class="col-sm-8">
							<div class="chart4 chart">
								<svg></svg>
							</div>
						</div>
					</div>
					<hr/>

					<div class="row">
						<div class="col-sm-4">
							<div class="img-intro">
								<img src="images/joaquim-barbosa.jpg" alt="" />
								<h2>Joaquim Barbosa</h2>
							</div>
							<p>Aparece em: <b>173</b> notícias.<br/>
								A média de polaridade foi de: <b>-0.1528</b>.</p>
						</div>
						<div class="col-sm-8">
							<div class="chart5 chart">
								<svg></svg>
							</div>
						</div>
					</div>
					<hr/>

					<div class="row">
						<div class="col-sm-4">
							<div class="img-intro">
								<img src="images/doria.jpg" alt="" />
								<h2>Doria</h2>
							</div>
							<p>Aparece em: <b>446</b> notícias.<br/>
								A média de polaridade foi de: <b>-0.0437</b>.</p>
						</div>
						<div class="col-sm-8">
							<div class="chart6 chart">
								<svg></svg>
							</div>
						</div>
					</div>
					<hr/>

					<div class="row">
						<div class="col-sm-4">
							<div class="img-intro">
								<img src="images/bolsonaro.jpg" alt="" />
								<h2>Bolsonaro</h2>
							</div>
							<p>Aparece em: <b>239</b> notícias.<br/>
								A média de polaridade foi de: <b>-0.4032</b>.</p>
						</div>
						<div class="col-sm-8">
							<div class="chart7 chart">
								<svg></svg>
							</div>
						</div>
					</div>
					<hr/>

					<div class="row">
						<div class="col-sm">
							<h2 class="upper">Visão geral dos pré-candidatos.</h2>
							<h5 class="light">Comparação dos pré-candidatos por quantidade de notícias e média de polaridade</h5>
						</div>
					</div>
					<hr/>

					<div class="row">
						<div class="col-sm-5">
							<h4 class="text-center">Quantidade de notícias</h4>
							<div class="chart8 chart size2">
								<svg></svg>
							</div>
						</div>
						<div class="col-sm-7">
							<h4 class="text-center">Média de polaridade</h4>
							<div class="chart9 chart">
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
