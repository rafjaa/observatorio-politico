<?php
require(__DIR__ . DIRECTORY_SEPARATOR . 'classes' . DIRECTORY_SEPARATOR . 'loader.php');

SearcherHTML::setTitle('Entidades');

$total = SearcherMongo::count('tags');

$total = ceil($total / 10);
$page = max(min(isset($_REQUEST['p']) ? (int) $_REQUEST['p'] : 1, $total), 1);

$cursor = SearcherMongo::query('tags', [], ['sort' => ['freq' => -1], 'limit' => 18, 'skip' => ($page - 1) * 18, 'projection' => ['_id' => 0]]);
$results = $cursor->toArray();
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
						Entidades
					</div>
				</div>
				<div class="container">
					<div class="row">
<?php
		$pos = 0;
		foreach ($results as &$result) :
?>
						<a class="col-lg-4 col-md-6 col-sm-6 col-xs-12 tagitem" href="searchtags.php?q=<?php echo SearcherHTML::escape(rawurlencode($result->tag)); ?>">
							<div class="block">
								<div><?php echo 'Mencionada ' . number_format($result->freq, 0, ',', '.') . ' vez' . ($result->freq > 1 ? 'es' : ''); ?></div>
								<h4><?php echo SearcherHTML::escape($result->tag); ?></h4>
							</div>
						</a>
<?php
		endforeach;
?>
					</div>
					<div class="paginatorcontainer">
						<?php SearcherHTML::pagination($page, $total, 'tags.php', array(), 'p'); ?>
					</div>
				</div>
			</div>
			<?php require(__DIR__ . DIRECTORY_SEPARATOR . 'template' . DIRECTORY_SEPARATOR . 'footer.php'); ?>
		</div>
	</body>
</html>
