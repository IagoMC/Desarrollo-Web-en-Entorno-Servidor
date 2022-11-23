<?php
  $db = mysqli_connect('localhost', 'root', '1234', 'mysitedb') or die('Fail');
$usuario= $_POST['Usuario'];
$email=$_POST['Email'];
$contrasena=$_POST['contraseña'];
$con_contrasena=$_POST['con_contraseña'];

if ($con_contrasena!=$contrasena) {
    echo '<p>Contraseña no valida</p>';
} else {
    $contrasenaHash=password_hash($contrasena,PASSWORD_DEFAULT);
    $query = $db->prepare ("insert into usuarios (nombre, email, contrasena) values (?,?,?)");
	
    $query->bind_param("sss",$usuario,$email,$contrasenaHash); 
    $query->execute();
    $query->close();
    header('Location: login.html');

}


?>
