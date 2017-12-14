<?php
require(__DIR__ . DIRECTORY_SEPARATOR . 'classes' . DIRECTORY_SEPARATOR . 'loader.php');

SearcherHTML::setTitle('Resultados');

SearcherHTML::addCSSFile('ion.rangeSlider.css');
SearcherHTML::addCSSFile('ion.rangeSlider.skinModern.css');

SearcherHTML::addJSFile('ion.rangeSlider.min.js');
SearcherHTML::addJSFile('gauge.min.js');

$tags = preg_split('/\\s*,\\s*/', @$_REQUEST['q']);
if (end($tags) === '')
	array_pop($tags);

$mincompound = max(SearcherSecurity::validateFloat(@$_REQUEST['np'], -1), -1);
$maxcompound = min(SearcherSecurity::validateFloat(@$_REQUEST['xp'], 1), 1);

$and = [];
if (!empty($tags)) {
	$search = array();
	foreach ($tags as &$tag)
		$search[] = ['tag' => new MongoDB\BSON\Regex('^' . preg_quote($tag) . '$', 'i')];

	$and[] = ['entidades' => ['$elemMatch' => ['$and' => &$search]]];
}
$params = array('q' => &$_REQUEST['q']);

if ($mincompound > -1) {
	$and[] = ['polaridade.compound' => ['$gte' => $mincompound]];
	$params['np'] = $mincompound;
}

if ($maxcompound < 1) {
	$and[] = ['polaridade.compound' => ['$lte' => $maxcompound]];
	$params['xp'] = $maxcompound;
}

$query = empty($and) ? [] : ['$and' => &$and];

$total = SearcherMongo::count('noticias', $query);

$total = ceil($total / 10);
$page = max(min(isset($_REQUEST['p']) ? (int) $_REQUEST['p'] : 1, $total), 1);

$cursor = SearcherMongo::query('noticias', $query, ['limit' => 10, 'skip' => ($page - 1) * 10]);
$results = $cursor->toArray();

SearcherHTML::addJSDeclarationFile("var _np=$mincompound,_xp=$maxcompound");
?>
<!DOCTYPE html>
<html lang="pt-BR">
	<head>
		<?php echo SearcherHTML::getHeadTags(); ?>
	</head>
	<body id="results">
		<div id="parallax" data-parallax="scroll" data-image-src="template/images/newspapers.jpg">
			<?php require(__DIR__ . DIRECTORY_SEPARATOR . 'template' . DIRECTORY_SEPARATOR . 'header.php'); ?>
			<div id="tagcloudcontainer">
				<div class="containertitle">
					<div class="container">
						Resultados
					</div>
				</div>
				<div class="container">
<?php	foreach ($results as &$result) : ?>
					<div class="result" data-id="<?php echo SearcherHTML::escape($result->_id); ?>">
						<div class="header">
							<div class="title"><a href="<?php echo SearcherHTML::escape($result->url); ?>" target="_blank"><?php echo $result->titulo; ?></a></div>
							<div class="link"><a href="<?php echo SearcherHTML::escape($result->url); ?>" target="_blank"><?php echo SearcherHTML::escape($result->url); ?></a></div>
							<div class="btn btn-default viewnews">Visualizar notícia processada</div>
						</div>
						<div class="gauge" data-compound="<?php echo sprintf('%.4f', $result->polaridade->compound); ?>">
							<canvas></canvas>
							<div>
								<span class="pull-left">-1</span>
								<span class="pull-right">1</span>
							</div>
							<div class="clearfix"></div>
						</div>
<?php		if (is_array($result->entidades)) : ?>
						<div class="tags">
<?php
			usort($result->entidades, array('SearcherSorter', 'tags'));
			for ($i = 0; $i < 10 && isset($result->entidades[$i]); ++$i)
				echo '<a href="searchtags.php?q=' . rawurlencode($result->entidades[$i]->tag) . '" class="tag' . ($i > 4 ? ' hidden-xs' : '') . '">' . SearcherHTML::escape($result->entidades[$i]->tag) . ' - ' . $result->entidades[$i]->freq . '</a>';
?>
						</div>
<?php		endif; ?>
					</div>
<?php	endforeach; ?>
					<div class="paginatorcontainer">
						<?php SearcherHTML::pagination($page, $total, 'searchtags.php', $params, 'p'); ?>
					</div>
				</div>
				<div id="containerfilter">
					<div class="container">
						<div class="row">
							<div class="col-md-12">
								<form method="GET">
									<h3>Entidades</h3>
									<input type="text" name="q" value="<?php echo SearcherHTML::escape(@$_REQUEST['q']); ?>" class="btn-block" id="entitiesfilter">
									<h3>Polaridade composta</h3>
									<div id="entitiesrange"></div>
									<input type="hidden" id="np" name="np" value="<?php echo $mincompound; ?>">
									<input type="hidden" id="xp" name="xp" value="<?php echo $maxcompound; ?>">
									<button class="btn btn-primary btn-lg">Filtrar</button>
								</form>
							</div>
						</div>
					</div>
				</div>
			</div>
			<?php require(__DIR__ . DIRECTORY_SEPARATOR . 'template' . DIRECTORY_SEPARATOR . 'footer.php'); ?>
		</div>
		<div class="modal fade" id="newscontent" tabindex="-1" role="dialog" aria-labelledby="newscontentlabel">
			<div class="modal-dialog modal-lg" role="document">
				<div class="modal-content">
					<div class="modal-header">
						<button type="button" class="close" data-dismiss="modal" aria-label="Fechar"><span aria-hidden="true">&times;</span></button>
						<h4 class="modal-title" id="newscontentlabel">Notícia processada</h4>
					</div>
					<div class="modal-body" id="newscontentdata"></div>
					<div class="modal-footer">
						<button type="button" class="btn btn-default" data-dismiss="modal">Fechar</button>
					</div>
				</div>
			</div>
		</div>
	</body>
</html>
