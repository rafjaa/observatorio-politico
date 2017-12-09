<?php
require(__DIR__ . DIRECTORY_SEPARATOR . 'classes' . DIRECTORY_SEPARATOR . 'loader.php');

header('Content-Type: application/json');

$result = false;
$cursor = SearcherMongo::query('noticias', ['_id' => new \MongoDB\BSON\ObjectId((string) @$_POST['id'])], ['projection' => ['conteudo' => 1, '_id' => 0]]);

foreach ($cursor as $document)
	$result = preg_replace('/\\n/', '<br><br>', $document->conteudo);

echo json_encode($result);
