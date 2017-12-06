<?php
abstract class SearcherMongo {
	const DB = 'tp_2_observatorio_politico';

	static function getConnection() {
		static $_connection;

		if (!$_connection)
			$_connection = new \MongoDB\Driver\Manager('mongodb://127.0.0.1:27017/');

		return $_connection;
	}

	static function query($collection, $query = array(), $options = array()) {
		$query = new \MongoDB\Driver\Query($query, $options);
		return self::getConnection()->executeQuery(self::DB . '.' . $collection, $query);
	}

	static function count($collection, $query = array()) {
		$command = new \MongoDB\Driver\Command(['count' => $collection, 'query' => $query]);
		$result = self::getConnection()->executeCommand(self::DB, $command)->toArray();
		return $result[0]->n;
	}
}
