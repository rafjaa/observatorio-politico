<?php
abstract class SearcherLoader {
	static function load($class) {
		$filename = strtolower(substr($class, 8));

		if ($filename !== '') {
			$filename = __DIR__ . DIRECTORY_SEPARATOR . $filename . '.php';

			if (@is_file($filename))
				@include_once($filename);
		}

		return class_exists($class);
	}
}

spl_autoload_register(array('SearcherLoader', 'load'));

define('_SEARCHER', true);

SearcherHTML::addCSSFile('bootstrap.min.css');
SearcherHTML::addCSSFile('jquery-ui.min.css');
SearcherHTML::addCSSFile('jquery-ui.theme.min.css');
SearcherHTML::addCSSFile('template.css');

SearcherHTML::addJSFile('jquery.min.js');
SearcherHTML::addJSFile('bootstrap.min.js');
SearcherHTML::addJSFile('parallax.min.js');
SearcherHTML::addJSFile('jquery-ui.min.js');
SearcherHTML::addJSFile('site.js');
