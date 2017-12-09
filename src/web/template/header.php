<?php
defined('_SEARCHER') or die;

$requestedfilename = basename($_SERVER['SCRIPT_NAME']);
?>
<div id="menuheader">
	<nav class="navbar">
		<div class="container">
			<div class="navbar-header">
				<button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar-collapse" aria-expanded="false">
					<span class="sr-only">Trocar navegação</span>
					<span class="icon-bar"></span>
					<span class="icon-bar"></span>
					<span class="icon-bar"></span>
				</button>
				<a class="navbar-brand" href="index.php"><i class="glyphicon glyphicon-search"></i></a>
			</div>

			<div class="collapse navbar-collapse" id="navbar-collapse">
				<ul class="nav navbar-nav navbar-left">
					<li<?php if ($requestedfilename == 'searchtags.php') echo ' class="active"'; ?>><a href="searchtags.php">Notícias</a></li>
					<li<?php if ($requestedfilename == 'tags.php') echo ' class="active"'; ?>><a href="tags.php">Entidades</a></li>
				</ul>
				<form class="navbar-form navbar-right" action="searchtags.php">
					<div class="form-group">
						<input type="text" class="form-control" placeholder="Entidades" name="q" value="<?php echo SearcherHTML::escape(@$_REQUEST['q']); ?>" id="headersearch">
					</div>
					<button type="submit" class="btn btn-default">Pesquisar</button>
				</form>
			</div>
		</div>
	</nav>
</div>
