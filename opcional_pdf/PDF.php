<?php
$nombre = $_POST['nombre'];
$apellido = $_POST['apellido'];

require('fpdf.php');

class PDF extends FPDF{
    function Header(){
        $this->Image('xunta.png',10,50,300);
        $this->SetFont('Arial','B',15);
        $this->cell(80);
        $this->cell(30,10,'DIPLOMA',1,0,'c')

    }
    function Footer()
{
    // Posición: a 1,5 cm del final
    $this->SetY(-15);
    // Arial italic 8
    $this->SetFont('Arial','I',8);
    // Número de página
    $this->Cell(0,10,'Page '.$this->PageNo().'/{nb}',0,0,'C');
}
}
    $pdf = new PDF();
    $pdf->AliasNbPages();
    $pdf->AddPage();
    $pdf->SetFont('Times','',12);
   
    $pdf->Output();

?>