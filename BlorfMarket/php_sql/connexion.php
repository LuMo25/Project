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
    <title>Se connecter</title>
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
                                <div class="content">
                                    <?php

                                    // on teste le formulaire et si l'utilisateur est connecté
                                    $error = 0;
                                    $errorCo = 0;
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
                                    if( isset( $_SESSION['isCo'] ) ) {
                                        if( $_SESSION['isCo'] == true) {
                                            $errorCo = $errorCo + 1;
                                        }
                                    }
                                    if( $error > 1 ) {

                                        if( $errorCo == 0) {
                                            echo
                                            '<form action="connexion.php" method="post">   
  <div class="coo1">
                    <li>
                    <a>Login</a><input type="text" placeholder="mon pseudo" name="login">
                    </li>
                    
                    <li>
                    <a>Password</a><input type="password" placeholder="mon mot de passe" name="password">
                    </li>
                    <li>
                    <input type="submit">
                    </li></div>
                    
                </form>';
                                        } else {
                                            echo 'Vous etes deja connecte!';

                                        }

                                    } else {

                                        $login = $_POST['login'];
                                        $password = $_POST['password'];


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



                                        if($res == false) {
                                            echo 'Mauvais credentials!';
                                            $_SESSION['isCo'] = false;
                                        } else {
                                            $_SESSION['id'] = $res->id;
                                            $_SESSION['isCo'] = true;
                                            $_SESSION['role'] = $res->role;
                                            echo 'connected with ID: ' . $_SESSION['id'] . ' as: ' . $_SESSION['role'] ;
                                            echo "<input type=\"button\" value=\"Se Connecter\" onclick=\"javascript:location.href='index.php'\">";
                                        }
                                    }
                                    ?>
                                </div>
                                <div class="special-space"></div>
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
