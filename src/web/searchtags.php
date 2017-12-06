<?php
require(__DIR__ . DIRECTORY_SEPARATOR . 'classes' . DIRECTORY_SEPARATOR . 'loader.php');

SearcherHTML::setTitle('Resultados');

SearcherHTML::addCSSFile('jquery-ui.min.css');
SearcherHTML::addCSSFile('jquery-ui.theme.min.css');

SearcherHTML::addJSFile('parallax.min.js');
SearcherHTML::addJSFile('jquery-ui.min.js');

$tags = preg_split('/\\s*,\\s*/', $_REQUEST['q']);
if (end($tags) === '')
	array_pop($tags);

$search = array();
foreach ($tags as &$tag)
	$search[] = ['tag' => new MongoDB\BSON\Regex('^' . preg_quote($tag) . '$', 'i')];

$query = ['entidades' => ['$elemMatch' => ['$or' => &$search]]];
$total = SearcherMongo::count('noticias', $query);

$total = ceil($total / 10);
$page = max(min(isset($_REQUEST['p']) ? (int) $_REQUEST['p'] : 1, $total), 1);

$cursor = SearcherMongo::query('noticias', $query, ['limit' => 10, 'skip' => ($page - 1) * 10, 'projection' => ['_id' => 0]]);
$results = $cursor->toArray();
?>
<!DOCTYPE html>
<html lang="pt-BR">
	<head>
		<?php echo SearcherHTML::getHeadTags(); ?>
	</head>
	<body id="results">
		<div id="parallax" data-parallax="scroll" data-image-src="template/images/newspapers.jpg">
			<div id="tagcloudcontainer">
				<div class="containertitle">
					<div class="container">
						Resultados
					</div>
				</div>
				<div class="container">
<?php	foreach ($results as &$result) : ?>
					<div class="result">
						<div class="header">
							<div class="title"><a href="<?php echo SearcherHTML::escape($result->url); ?>" target="_blank"><?php echo $result->titulo; ?></a></div>
							<div class="link"><a href="<?php echo SearcherHTML::escape($result->url); ?>" target="_blank"><?php echo SearcherHTML::escape($result->url); ?></a></div>
						</div>
						<div class="tags">
<?php
		usort($result->entidades, array('SearcherSorter', 'tags'));
		for ($i = 0; $i < 10 && isset($result->entidades[$i]); ++$i)
			echo '<a href="searchtags.php?q=' . rawurlencode($result->entidades[$i]->tag) . '" class="tag' . ($i > 4 ? ' hidden-xs' : '') . '">' . SearcherHTML::escape($result->entidades[$i]->tag) . ' - ' . $result->entidades[$i]->freq . '</a>';
?>
						</div>
					</div>
<?php	endforeach; ?>
					<div class="paginatorcontainer">
						<?php SearcherHTML::pagination($page, $total, 'searchtags.php', array('q' => &$_REQUEST['q']), 'p'); ?>
					</div>
				</div>
			</div>
			<?php require(__DIR__ . DIRECTORY_SEPARATOR . 'template' . DIRECTORY_SEPARATOR . 'footer.php'); ?>
		</div>
	</body>
</html>
