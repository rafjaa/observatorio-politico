<?php
abstract class SearcherHTML {
	static private $_cssfiles = array();
	static private $_jsfiles = array();
	static private $_jsdeclarations = array();
	static private $_title = '';

	static function addCSSFile($fileurl) {
		self::$_cssfiles[] = str_replace(realpath($_SERVER['DOCUMENT_ROOT']), '', realpath(__DIR__ . DIRECTORY_SEPARATOR . '..')) . ($fileurl[0] == '/' ? $fileurl : '/template/css/' . $fileurl);
	}

	static function addJSFile($fileurl) {
		self::$_jsfiles[] = str_replace(realpath($_SERVER['DOCUMENT_ROOT']), '', realpath(__DIR__ . DIRECTORY_SEPARATOR . '..')) . ($fileurl[0] == '/' ? $fileurl : '/template/js/' . $fileurl);
	}

	static function addJSDeclarationFile($declaration) {
		self::$_jsdeclarations[] =& $declaration;
	}

	static function &getCSSTags() {
		$cssfiletags = array();
		foreach (self::$_cssfiles as &$cssfile)
			$cssfiletags[] = '<link type="text/css" rel="stylesheet" href="' . $cssfile . '">';
		return implode("\n", $cssfiletags);
	}

	static function &getJSTags() {
		$jsfiletags = array();

		foreach (self::$_jsfiles as &$jsfile)
			$jsfiletags[] = '<script type="text/javascript" src="' . $jsfile . '"></script>';

		if (!empty(self::$_jsdeclarations))
			$jsfiletags[] = '<script type="text/javascript">' . implode(';', self::$_jsdeclarations) . '</script>';

		return implode("\n", $jsfiletags);
	}

	static function getHeadTags() {
		$tags = array();
		$tags[] = '<meta http-equiv="Content-Type" content="text/html;charset=UTF-8">';
		$tags[] = '<title>' . self::escape(self::$_title) . '</title>';
		$tags[] = '<meta name="viewport" content="initial-scale=1,maximum-scale=1">';
		$tags[] = &self::getCSSTags();
		$tags[] = &self::getJSTags();
		return implode("\n", $tags);
	}

	static function setTitle($title) {
		self::$_title =& $title;
	}

	static function escape($text) {
		return htmlspecialchars($text, ENT_COMPAT, 'UTF-8');
	}

	static private function _urlpagination(&$url, &$query, &$parameter, $value) {
		$query[$parameter] = $value;
		return self::escape($url . '?' . http_build_query($query));
	}

	static function pagination($page, $total, $url, $query, $parameter) {
		$num = 5;
		$pos = max(($until = min($num - 1 + max(($page = min(max($page, 1), $total)) - ($num - 1) / 2, 1), $total)) - $num + 1, 1);
?>
		<ul class="pagination">
			<li<?php if ($page == 1) echo ' class="disabled"'; ?>><a href="<?php echo $page != 1 ? self::_urlpagination($url, $query, $parameter, $page - 1) : '#'; ?>"<?php if ($page == 1) echo ' onclick="return false"'; ?>>&laquo;</a></li>
<?php	do { ?>
			<li<?php if ($page == $pos) echo ' class="active"'; ?>><a href="<?php echo $page != $pos ? self::_urlpagination($url, $query, $parameter, $pos) : '#'; ?>"<?php if ($page == $pos) echo ' onclick="return false"'; ?>><?php echo $pos; ?></a></li>
<?php	} while (++$pos <= $until); ?>
			<li<?php if ($page == $total) echo ' class="disabled"'; ?>><a href="<?php echo $page != $total ? self::_urlpagination($url, $query, $parameter, $page + 1) : '#'; ?>"<?php if ($page == $total) echo ' onclick="return false"'; ?>>&raquo;</a></li>
		</ul>
<?php
	}
}
