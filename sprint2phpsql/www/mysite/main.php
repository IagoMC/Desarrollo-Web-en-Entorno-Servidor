<?php
  $db = mysqli_connect('localhost', 'root', '1234', 'mysitedb') or die('Fail');
?>
<html>
<body>
<h1>Conexion establecida</h1>
<table>

  <?php
  // Lanzar una query
  $query = 'SELECT * FROM tLibros';
  $result = mysqli_query($db, $query) or die('Query error');
  // Recorrer el resultado
  while ($row = mysqli_fetch_array($result)) {
  	echo '<tr>';
  	echo '<td>'.$row[0];
  	echo '</td>';
  	echo '<br>';	

  	echo '<td>'.$row[1];
    echo '</td>';
	  echo '<br>';

	  echo '<td>'<a href="detail.php?libro_id='$row[0];
	  echo '"><img src="'.row[2];
	  echo '</td>';
	  echo '<br>';

	  echo '<td>'.$row[3];
	  echo '</td>';
	  echo '<br>';
	
  	echo '<td>'.$row[4];
	  echo '</td>';
  	echo '<br>';
  	echo '</tr>';

  }
mysqli_close($db);
?>
</table>
</body>
</html>
