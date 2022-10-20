<?php
  $db = mysqli_connect('localhost', 'root', '1234', 'mysitedb') or die('Fail');
?>
<html>
<head>
	<style>
	img{
		width: 200px;
		height: 300px;
	}
	td{
		padding:15px;
		text-align:center;
	}
	.color{
		background-color:red;
	}
	
	h1{
	/*
		width: 100px;
   		height: 200px;
    		
    		transition: width 2s, height 2s, margin 2s;
    		margin: 50px auto 0;
	*/
	}
	
	h1:hover{
   	 width: 100%;
   	 height: 50px;
   	 margin: 0 auto;
	text-align: center;
	background: red;
}	

	.tr1:hover{
	background: green;
	}
		
	
	
	</style>

</head>
<body>
<h1>Conexion establecida</h1>
<a href="/logout.php">Logout</a>
<table border="1" >

	<tr>
	 <td class="color">ID</td>
	 <td class="color">Titulo</td>
	 <td class="color">Foto</td>
	 <td class="color">Genero</td>
	 <td class="color">Autor</td>
	</tr>

  <?php
  // Lanzar una query
  $query = 'SELECT * FROM tLibros';
  $result = mysqli_query($db, $query) or die('Query error');
  // Recorrer el resultado
  while ($row = mysqli_fetch_array($result)) {
  	


	echo '<tr class="tr1">';
  	echo '<td class="pa">'.$row[0];
  	echo '</td>';
  	echo '<br>';	

  	echo '<td>'.$row[1];
    echo '</td>';
	  echo '<br>';

	  echo '<td><a href="/detail.php?libro_id='.$row[0];
	  echo '"><img src="'.$row[2];
	  echo '"></a></td>';
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
