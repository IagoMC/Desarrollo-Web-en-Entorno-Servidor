<?php
  $db = mysqli_connect('172.16.0.2', 'root', '1234', 'mysitedb') or die('Fail');
$usuario= $_POST['Usuario'];
$email=$_POST['Email'];
$contraseña=$_POST['contraseña'];
$con_contraseña=$_POST['con_contraseña'];

if ($con_contraseña!=$contraseña) {
    echo '<p>Contraseña no valida</p>';
} else {
    $contraseñaHash=password_hash($contraseña,PASSWORD_DEFAULT);
    $query = $mysqli->prepare ("insert into usuarios values (?,?,?)");
    $query->bind_param("sss",$usuario,$email,$contraseñaHash); 
    $query->execute();
    $query->close();
    header('Location: login.php');

}


?>