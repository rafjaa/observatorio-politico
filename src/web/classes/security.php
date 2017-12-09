<?php
abstract class SearcherSecurity {
	static function validateFloat($input, $returnifwrong = null) {
		return preg_match('/^\\s*-?(\\d*\\.)?\\d+\\s*$/', $input) ? (float) $input : $returnifwrong;
	}
}
