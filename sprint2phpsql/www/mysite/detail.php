<?php
$db = mysqli_connect('localhost', 'root', '1234', 'mysitedb') or die('Fail');
?>
<html>
  <body>
  <?php
    if (!isset($_GET['libro_id'])) {
      die('No se ha especificado una canción');
    }
    $libro_id = $_GET['libro_id'];
    $query = 'SELECT * FROM tLibros WHERE id='.$libro_id;
    $result = mysqli_query($db, $query) or die('Query error1');
    $only_row = mysqli_fetch_array($result);
    echo '<h1>'.$only_row['id'].'</h1>';
    echo '<h2>'.$only_row['nombre'].'</h2>';
    echo '<img src='.$only_row['url_imagen'].'>';
    echo '<h2>'.$only_row['genero'].'</h2>';

    echo '<h2>'.$only_row['autor'].'</h2>';
    ?>
    <h3>Comentarios:</h3>
    <ul>
    <?php
    $query2 = 'SELECT * FROM tComentarios WHERE libro_id='.$libro_id;
    $result2 = mysqli_query($db, $query2) or die('Query error2');
    while ($row = mysqli_fetch_array($result2)) {
      echo '<li>'.$row['comentario'].'</li>';
    }

mysqli_close($db);
	?>
    
	<p>Deja un nuevo comentario:</p>
	<form action="/comment.php" method="post">
		<textarea rows="4" cols="50" name="mew_comment"></textarea><br>
		<input type="hidden" name="libro_id" value="<?php echo $libro_id; ?>">
		<input type="submit" value="comentar">
	</form>


  
  </ul>
  </body>
</html>
