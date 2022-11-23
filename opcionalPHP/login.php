<?php
$db = mysqli_connect('localhost', 'root', '1234', 'mysitedb') or die('Fail');

$usuario= $_POST['Usuario'];
$contrasena= $_POST['contraseña'];

$query = "SELECT id, contrasena FROM usuarios WHERE email = '" . $Usuario . "'";
$result = mysqli_query($db, $query) or die('Query error');


if (password_verify($contrasena, $only_row[1])) {
    session_start();
    $_SESSION['user_id'] = $only_row[0];
    header('Location: main.php');

}else{
    echo '<p>Contraseña no coincide</p>';
}
?>
