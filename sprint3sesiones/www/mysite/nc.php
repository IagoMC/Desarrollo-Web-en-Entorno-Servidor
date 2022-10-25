<?php
$db = mysqli_connect('localhost', 'root', '1234', 'mysitedb') or die('Fail');

session_start();
$user = 'NULL';
if (!empty($_SESSION['user_id'])) {
$user = $_SESSION['user_id'];
}
$password_posted = $_POST['f_password2'];
$Nueva = $_POST['Nueva'];
$Nueva2 = $_POST['Nueva2'];
echo $user;
$query = "SELECT contraseña FROM tUsuarios WHERE id = ".$user;


$result = mysqli_query($db, $query) or die('Query error');

if (mysqli_num_rows($result) > 0) {
    $only_row = mysqli_fetch_array($result);
    if ($only_row[0] == $password_posted) {
        //session_start();
	
        //$_SESSION['user_id'] = $only_row[0];
	if ($Nueva2==$Nueva){	
	echo "$Nueva";
	echo "$Nueva2";
	
	$query2 = "UPDATE tUsuarios SET contraseña = '".$Nueva."' where id =".$user; 
	$result = mysqli_query($db, $query2) or die('Query error');

	//echo 'confirmado';
	echo '<p>Confirmado</p>';	
}else{

	//session_start();
	//$_SESSION['user_id'] = $Nueva;
        //header('Location: main.php');  
	echo '<p>NO</p>';  
}
} else {
        echo '<p>Contraseña incorrecta</p>';
    }
} else {
    echo '<p>Usuario no encontrado con ese email</p>';
}

?>
