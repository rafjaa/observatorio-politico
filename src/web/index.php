<?php
require(__DIR__ . DIRECTORY_SEPARATOR . 'classes' . DIRECTORY_SEPARATOR . 'loader.php');

SearcherHTML::setTitle('Boas-vindas');

SearcherHTML::addCSSFile('jquery-ui.min.css');
SearcherHTML::addCSSFile('jquery-ui.theme.min.css');
SearcherHTML::addCSSFile('jqcloud.min.css');

SearcherHTML::addJSFile('parallax.min.js');
SearcherHTML::addJSFile('jquery-ui.min.js');
SearcherHTML::addJSFile('jqcloud.min.js');

$cursor = SearcherMongo::query('tags', [], ['sort' => ['freq' => -1], 'limit' => 100, 'projection' => ['_id' => 0]]);
$result = array();

foreach ($cursor as $document) {
	$object = (object) ['text' => $document->tag, 'weight' => $document->freq, 'link' => 'searchtags.php?q=' . rawurlencode($document->tag)];
	if (rand(1,3) == 1)
		$object->html = (object) ['class' => 'vertical'];
	$result[] = $object;
}

SearcherHTML::addJSDeclarationFile('var words = ' . json_encode($result));
?>
<!DOCTYPE html>
<html lang="pt-BR">
	<head>
		<?php echo SearcherHTML::getHeadTags(); ?>
	</head>
	<body id="main">
		<div id="parallax" data-parallax="scroll" data-image-src="template/images/newspapers.jpg">
			<?php require(__DIR__ . DIRECTORY_SEPARATOR . 'template' . DIRECTORY_SEPARATOR . 'header.php'); ?>
			<div id="mainsearcher">
				<div class="container">
					<div id="searchform">
						<form method="GET" action="searchtags.php">
							<div id="searchfield">
								<i class="glyphicon glyphicon-search"></i>
								<div class="set">
									<input name="q" type="text" autocomplete="off">
								</div>
							</div>
							<button class="btn btn-primary btn-block">Pesquisar</button>
						</form>
					</div>
				</div>
			</div>
			<div id="tagcloudcontainer">
				<div class="containertitle">
					<div class="container">
						<a href="tags.php">Palavras mais frequentes</a>
					</div>
				</div>
				<div class="container-fluid">
					<div id="tagcloud"></div>
				</div>
			</div>
			<?php require(__DIR__ . DIRECTORY_SEPARATOR . 'template' . DIRECTORY_SEPARATOR . 'footer.php'); ?>
		</div>
	</body>
</html>
