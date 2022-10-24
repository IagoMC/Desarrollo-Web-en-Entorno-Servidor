<?php
$db = mysqli_connect('localhost', 'root', '1234', 'mysitedb') or die('Fail');

$email_posted = $_POST['f_email2'];
$password_posted = $_POST['f_password2'];
$Nueva = $_Post['Nueva'];

$query = "SELECT id, contraseña FROM tUsuarios WHERE email = '" . $email_posted2 . "'";
$result = mysqli_query($db, $query) or die('Query error');

if (mysqli_num_rows($result) > 0) {
    $only_row = mysqli_fetch_array($result);
    if ($only_row[1] == $password_posted2) {
        //session_start();
	
        //$_SESSION['user_id'] = $only_row[0];
	$query = "UPDATE tUsuarios SET contraseña = '.$Nueva.' where email = '.$email_posted2.'"; 
	//echo 'confirmado';


	//session_start();
	//$_SESSION['user_id'] = $Nueva;
        //header('Location: main.php');  
	echo '<p>Confirmado</p>';  

} else {
        echo '<p>Contraseña incorrecta</p>';
    }
} else {
    echo '<p>Usuario no encontrado con ese email</p>';
}

?>
