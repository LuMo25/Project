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
    <title>Créer un compte</title>
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
                                $error = 0;
                                $Ecoo = 0;
                                if( isset( $_POST['email'] ) ) {
                                    if( $_POST['email'] == NULL ) {
                                        $error = $error + 1;
                                    }
                                } else {
                                    $error = $error + 1;
                                }
                                if( isset( $_POST['login'] ) ) {
                                    if( $_POST['login'] == NULL ) {
                                        $error = $error + 1;
                                    }
                                } else {
                                    $error = $error + 1;
                                }
                                if( isset( $_POST['password'] ) ) {
                                    if( $_POST['password'] == NULL ) {
                                        $error = $error + 1;
                                    }
                                } else {
                                    $error = $error + 1;
                                }
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
                                    if( $_SESSION['isCo'] == true) {
                                        $Ecoo = $Ecoo + 1;
                                    }
                                }
                                if( $error > 1 ) {

                                    if( $Ecoo == 0) {
                                        echo
                                        '<form action="register.php" method="post">     
    <div class="coo2">
    <li>
                    <a>eMail</a><input type="email" placeholder="mon adresse mail" name="email" autocomplete="off">
                    </li><li>
                    <a>Login</a><input type="text" placeholder="mon pseudo" name="login" autocomplete="off">
                    </li><li>
                    <a>Addresse de facturation</a><input type="mon adresse de facturation" name="ba" autocomplete="off">
                    </li><li>
                    <a>Addresse de livraison</a><input type="mon adresse de livraison" name="da" autocomplete="off">
                    </li><li>
                    <a>Password</a><input type="password" placeholder="mon mot de passe" name="password">
                    </li><li>
                    <input type="submit"> 
                    </li></div>
                </form>';
                                    }

                                } else {

                                    $login = $_POST['login'];
                                    $password = $_POST['password'];
                                    $email = $_POST['email'];
                                    $ba = $_POST['ba'];
                                    $da = $_POST['da'];

                                    $conn = new mysqli('localhost', 'root', '', 'supmarket');
                                    if ($conn->connect_error) {
                                        die("Connection failed: " . $conn->connect_error);
                                    }

                                    $sql = "INSERT INTO users (login, password, email, billing_address, delivery_address, role)
            VALUES ('$login', '$password', '$email', '$ba', '$da', 'guest')";

                                    if ($conn->query($sql) === TRUE) {
                                        echo 'Vous est inscrit';
                                    } else {
                                        echo "Error: " . $sql . "<br>" . $conn->error;
                                    }

                                    $conn->close();

                                    $_SESSION['isCo'] = true;



                                    $dsn = "mysql:host=localhost;port=3306;dbname=supmarket";


                                    try {
                                        $pdo = new PDO($dsn, "root", "");
                                    } catch (PDOException $e) {
                                        die("Error ! : " . $e->getMessage());
                                    }


                                    $sql = 'SELECT id, role FROM users
                    WHERE login="'.$login.'"
                    AND password="'.$password.'"';

                                    $sth = $pdo->query($sql);

                                    $res = $sth->fetch(PDO::FETCH_OBJ);

                                    $_SESSION['id'] = $res->id;
                                    $_SESSION['role'] = $res->role;

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
