<?php
header('Content-Type: application/json');

$servername = "localhost";
$username = "tu_usuario";
$password = "tu_contraseña";
$dbname = "guli_sundae";

// Crear conexión
$conn = new mysqli($servername, $username, $password, $dbname);

// Verificar conexión
if ($conn->connect_error) {
    die("Conexión fallida: " . $conn->connect_error);
}

// Consulta para obtener los sabores
$sql = "SELECT id, nombre, descripcion FROM sabores WHERE disponible = TRUE";
$result = $conn->query($sql);

$sabores = array();

if ($result->num_rows > 0) {
    while($row = $result->fetch_assoc()) {
        $sabores[] = $row;
    }
}

echo json_encode($sabores);

$conn->close();
?>

