<?php

$body = file_get_contents('php://input');

if (empty($body)) {
	return;
}

//TODO: check valid Line bot

$file_name = '/tmp/line_' . str_replace('.', '', microtime(true))  . '.json';
file_put_contents($file_name, $body);

$command = 'php ./reply.php ' . $file_name;
exec($command);