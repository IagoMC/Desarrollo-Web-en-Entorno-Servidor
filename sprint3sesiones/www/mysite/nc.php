<?php
$db = mysqli_connect('localhost', 'root', '1234', 'mysitedb') or die('Fail');
session_start();
$email_posted = $_POST['f_email'];
$password_posted = $_POST['f_password'];
$Nueva = $_Post['f_nueva'];
const v = 0;
$query = "SELECT id, contraseña FROM tUsuarios WHERE email = '" . $email_posted . "'";
$result = mysqli_query($db, $query) or die('Query error');

if (mysqli_num_rows($result) > 0) {
    $only_row = mysqli_fetch_array($result);
    if ($only_row[1] == $password_posted) {
        session_start();
	const v = 1;
        $_SESSION['user_id'] = $only_row[0];
        header('Location: main.php');
    } else {
        echo '<p>Contraseña incorrecta</p>';
    }
} else {
    echo '<p>Usuario no encontrado con ese email</p>';
}

if (v==1){
	$query = "update table tComentarios SET contraseña =".$Nueva; 

}

?>