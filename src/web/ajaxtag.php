<?php
require(__DIR__ . DIRECTORY_SEPARATOR . 'classes' . DIRECTORY_SEPARATOR . 'loader.php');

header('Content-Type: application/json');

$result = array();
$cursor = SearcherMongo::query('tags', ['tag' => new MongoDB\BSON\Regex('^' . preg_quote($_POST['tag']), 'i')], ['sort' => ['freq' => -1], 'limit' => 10, 'projection' => ['tag' => 1, '_id' => 0]]);

foreach ($cursor as $document)
	$result[] = $document->tag;

echo json_encode($result);
