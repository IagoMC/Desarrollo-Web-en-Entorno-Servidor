?php
	$db = mysqli_connect('localhost', 'root', '1234', 'mysitedb') or die ('Fail');
?>
<html>
	<body>
	<?php
	 $libro_id = $_POST['libro_id'];
	 $comentario = $_POST['new_comment'];

	$query = "INSERT INTO tComentarios (comentario, usuario_id, libro_id) values ('".$comentario."',".$cancion_id.",null)";
	mysqli_query($db, $query) or die ('Error');
	
	echo "<p>Nuevo comentario ";
	echo mysqli_insert_id($db);
	echo " añadido</p>";

	echo "<a href='/detail.php?cancion_id=".$libro_id."'>volver</a>";
	mysqli_close($db);
	?>
	</body>
</html>
