<?php
$db = mysqli_connect('localhost', 'root', '1234', 'mysitedb') or die('Fail');

$usuario= $_POST['Usuario'];
$contraseña= $_POST['contraseña'];

$query = "SELECT id, contraseña FROM usuarios WHERE email = '" . $Usuario . "'";
$result = mysqli_query($db, $query) or die('Query error');
$contraseñaHash=password_hash($contraseña,PASSWORD_DEFAULT);

if ($only_row[1] == $contraseñaHash) {
    session_start();
    $_SESSION['user_id'] = $only_row[0];
    header('Location: main.php');

}else{
    echo '<p>Contraseña no coincide</p>';
}
?>