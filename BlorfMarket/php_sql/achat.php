<?php
session_start();
?>

<!DOCTYPE html>

<html>

<head>

    <link rel="stylesheet" type="text/css" href="../css/demo.css" />
    <link rel="stylesheet" type="text/css" href="../css/style1.css" />
    <link href="../css/styles.css" rel="stylesheet" type="text/css" />
    <script type="text/javascript" src="../js/modernizr.custom.86080.js"></script>
    <script type="text/javascript" src="../js/scroll.js."></script>
    <script type="text/javascript" src="../js/jquery.min.js"></script>
    <script type="text/javascript" src="../js/jquery.sticky.js"></script>
    <script>
        $(window).load(function(){
            $("#menu").sticky({ topSpacing: 0 });
        });
    </script>
    <title>Formulaire d'inscription</title>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title>Acheter</title>
</head>

<body>
<ul class="cb-slideshow">
    <li><span>Image 01</span><div></div></li>
    <li><span>Image 02</span><div></div></li>
    <li><span>Image 03</span><div></div></li>
    <li><span>Image 04</span><div></div></li>
    <li><span>Image 05</span><div></div></li>
    <li><span>Image 06</span><div></div></li>
</ul>
<div class="container">

    <?php include "intro.php"; ?>
    <div class="clearing"></div>
    <div class="border-bottom"></div>

    <div class="clearing"></div>
    <div class="container2">
        <div class="panel-wrapper">
            <div class="right-colum">
                <div class="mid-panel-content">
                    <div class="border"></div>
                    <div class="clearing"></div>
                    <div class="address">
                        <div class="panel">
                            <div class="desmarches">
                                <div class="special-space"></div>

    <?php

$co = 0;
if (isset($_SESSION['isCo'])) {
    if ($_SESSION['isCo'] == 1) {
        $co = 1;
    }
}

if ($co == 1) {


    $dsn = "mysql:host=localhost;port=3306;dbname=supmarket";


    try {
        $pdo = new PDO($dsn, "root", "");
    } catch (PDOException $e) {
        die("Error ! : " . $e->getMessage());
    }


    $sql = 'SELECT billing_address, delivery_address FROM users
                    WHERE id="' . $_SESSION['id'] . '"';

    $sth = $pdo->query($sql);

    $res = $sth->fetch(PDO::FETCH_OBJ);

    if ($res->billing_address == NULL || $res->delivery_address == NULL) {
        echo '<p>Vous n\'avez pas d\'addresse de livraison et d\'adresse de facturation! Veuillez les remplir ci dessous</p>';

        echo '
                
                    <form action="cmpreg.php" method="post">
                        <label>Addresse de facturation: </label><input type="text" name="ba"><br>
                        <label>Addresse de livraison: </label><input type="text" name="da"><br>
                        <input type="submit"><br>
                    </form>
                
                ';


        // pop form
    } else {
        //do


        $dsn = "mysql:host=localhost;port=3306;dbname=supmarket";


        try {
            $pdo = new PDO($dsn, "root", "");
        } catch (PDOException $e) {
            die("Error ! : " . $e->getMessage());
        }

        $sql = 'SELECT id, billing_address, delivery_address FROM users
                    WHERE id="' . $_SESSION['id'] . '"';

        $sth = $pdo->query($sql);

        $res = $sth->fetch(PDO::FETCH_OBJ);

        $ba = $res->billing_address;
        $da = $res->delivery_address;
        $cu = $res->id;

        //var_dump($_SESSION['cart']);
        //print_r($_SESSION['cart']);

        $ar = "";
        $pr = 0.00;
        foreach ($_SESSION['cart'] as $item) {
            $ar = $ar . "||" . $item['productId'];
            $pr = $pr + (double)$item['productPrice'];
        }

        $cy = $_SESSION['cart'][0]['productCurrency'];


        $conn = new mysqli('localhost', 'root', '', 'supmarket');
        if ($conn->connect_error) {
            die("Connection failed: " . $conn->connect_error);
        }

        $sql = "INSERT INTO recepices (billing_address, delivery_address, articles, price, customer, currency, status)
                VALUES ('$ba', '$da', '$ar', '$pr', '$cu', '$cy', 'pending')";

        if ($conn->query($sql) === TRUE) {
            echo '<p>Le recepice a ete envoye aux administrateur qui s\'en occupera des que possible.</p>';
        } else {
            echo "Error: " . $sql . "<br>" . $conn->error;
        }

        $conn->close();


    }


} else {
    echo 'Vous devez etre connecte pour acceder a cette page';
}


?>

                                <div class="special-space"></div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="clearing"></div>
        </div>
    </div>
</div>
</body>

</html>
