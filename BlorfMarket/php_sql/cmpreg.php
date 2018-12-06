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
    <title>Mise a jour</title>
</head>

<body>
<ul class="cb-slideshow">
    <li><span>01</span><div></div></li>
    <li><span>02</span><div></div></li>
    <li><span>03</span><div></div></li>
    <li><span>04</span><div></div></li>
    <li><span>05</span><div></div></li>
    <li><span>06</span><div></div></li>
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
                                $error = 0;
                                $errorCo = 0;
                                if( isset( $_POST['ba'] ) ) {
                                    if( $_POST['ba'] == NULL ) {
                                        $error = $error + 1;
                                    }
                                } else {
                                    $error = $error + 1;
                                }
                                if( isset( $_POST['da'] ) ) {
                                    if( $_POST['da'] == NULL ) {
                                        $error = $error + 1;
                                    }
                                } else {
                                    $error = $error + 1;
                                }

                                if( isset( $_SESSION['isCo'] ) ) {
                                    if( $_SESSION['isCo'] != true) {
                                        $errorCo = $errorCo + 1;
                                    }
                                }

                                if( $error < 1 && $errorCo < 1) {

                                    $ba = $_POST['ba'];
                                    $da = $_POST['da'];

                                    $conn = new mysqli('localhost', 'root', '', 'aze');
                                    if ($conn->connect_error) {
                                        die("Connection failed: " . $conn->connect_error);
                                    }

                                    $sql = "
            UPDATE users
            SET billing_address='" . $ba . "', delivery_address='" . $da . "'
            WHERE id='" . $_SESSION['id'] . "' 
            ";

                                    if ($conn->query($sql) === TRUE) {
                                        echo 'Informations mises a jour';
                                    } else {

                                        echo "Error: " . $sql . "<br>" . $conn->error;
                                    }

                                    $conn->close();

                                } else {
                                    echo 'Erreur de formulaire<br><a href="index.php">.</a>.';
                                }
                                ?><div class="special-space"></div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="clearing"></div>
        </div>
        <!--- panel wrapper div end -->
    </div>
</div>
</body>
</html>
