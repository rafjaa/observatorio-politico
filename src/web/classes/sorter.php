<?php
abstract class SearcherSorter {
	static function tags($a, $b) {
		if (!($pos = $b->freq - $a->freq))
			return strcmp($a->tag, $b->tag);
		return $pos;
	}
}
