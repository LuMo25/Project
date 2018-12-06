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
    <title>Panier</title>
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


if (!isset($_SESSION['cart'])) {
    $_SESSION['cart'] = array();
}


$error = 0;
$errorCo = 0;
if (isset($_POST['productId'])) {
    if ($_POST['productId'] == NULL) {
        $error = $error + 1;
    }
} else {
    $error = $error + 1;
}
if (isset($_POST['productName'])) {
    if ($_POST['productName'] == NULL) {
        $error = $error + 1;
    }
} else {
    $error = $error + 1;
}
if (isset($_POST['productCurrency'])) {
    if ($_POST['productCurrency'] == NULL) {
        $error = $error + 1;
    }
} else {
    $error = $error + 1;
}
if (isset($_POST['productPrice'])) {
    if ($_POST['productPrice'] == NULL) {
        $error = $error + 1;
    }
} else {
    $error = $error + 1;
}
if (isset($_POST['productPage'])) {
    if ($_POST['productPage'] == NULL) {
        $error = $error + 1;
    }
} else {
    $error = $error + 1;
}

if (isset($_SESSION['isCo'])) {
    if ($_SESSION['isCo'] == true) {
        $errorCo = $errorCo + 1;
    }
} else {
    $errorCo = $errorCo + 1;
}


//var_dump($_SESSION);

$ez = 0;
if ($error < 1) {

    if ($errorCo > 0) {


        $ez = 1;

        array_push($_SESSION['cart'], array());
        $len = sizeof($_SESSION['cart']);
        $_SESSION['cart'][$len - 1]["productId"] = $_POST['productId'];
        $_SESSION['cart'][$len - 1]["productName"] = $_POST['productName'];
        $_SESSION['cart'][$len - 1]["productCurrency"] = $_POST['productCurrency'];
        $_SESSION['cart'][$len - 1]["productPrice"] = $_POST['productPrice'];
        $_SESSION['cart'][$len - 1]["productPage"] = $_POST['productPage'];


    } else {
        echo 'Vous devez etre connecte pour acceder au panier';
    }

}

if ($ez = 1) {


    foreach ($_SESSION['cart'] as $value) {


        $pi = $value['productId'];
        $pn = $value['productName'];
        $pc = $value['productCurrency'];
        $ppr = $value['productPrice'];
        $ppa = $value['productPage'];


        echo
            '
                    <div style="border-style:solid;width:400px;">
                        <a href="' . $ppa . '">' . $pn . '</a>
                        <p>Prix: ' . $ppr . $pc . '</p>
                        <a style="font-style:italic;" href="' . $ppa . '">Voir le produit</a>       
                    </div>
                    <br>
                    
                    ';

    }


    echo '
                    <form action="achat.php" method="post">
                        <input type="submit" value="Acheter">
                    
                    </form>
                    ';

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
</div>
</body>

</html>
