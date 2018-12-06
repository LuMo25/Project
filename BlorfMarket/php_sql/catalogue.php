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
    <title>BlorfMarket</title>
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

                                $erri = 0;
                                if (isset($_SESSION['isCo'])) {
                                    if ($_SESSION['isCo'] == 0) {
                                        echo "<a> Vous devez etre connecte pour avoir acces au catalogue!</a>";
                                        echo "<input type=\"button\" value=\"Se Connecter\" onclick=\"javascript:location.href='connexion.php'\">
";
                                    } else {
                                        $erri = $erri + 1;
                                    }
                                } else {
                                    $erri = $erri + 1;
                                    echo "Vous devez être connecté pour accéder au catalogue!<br>";
                                    echo "<input type=\"button\" value=\"Se connecter\" onclick=\"javascript:location.href='connexion.php'\">
";
                                }


                                if ($erri > 1) {
                                    include "intro.php";
                                }
                                ?>





                                <?php

                                $erri = 0;
                                if (isset($_SESSION['isCo'])) {
                                    if ($_SESSION['isCo'] == 1) {
                                        echo '            
                    <h1>catalogue:</h1>
                    <hr>
                    <p>Rechercher</p>
                    <form action="catalogue.php" method="get">
                        <label>Sexe: </label><select name="gender"><option value="all">Tous</option><option value="female">Femme</option><option value="male">Homme</option></select>
                        <br>
                        
                        <input type="submit" value="Rechercher">
                    </form>
                    <br><hr>             
                    ';


                                        $url = 'https://api.zalando.com/articles?fullText=shoes&pageSize=48';

                                        if (isset($_GET['gender'])) {
                                            if ($_GET['gender'] != NULL) {
                                                if ($_GET['gender'] != "all") {
                                                    $url = $url . "gender=" . $_GET['gender'] . "&";
                                                }
                                            }
                                        }

                                        $content = @file_get_contents($url);

                                        $error = 0;
                                        if ($content === FALSE) {
                                            $error = $error + 1;
                                            echo 'nothing found! :(';
                                        }

                                        if ($error < 1) {
                                            $json = json_decode($content, true);
                                            foreach ($json['content'] as $value) {


                                                $item = '
                    <form method="get" action="article.php">
                    <button type="submit">
                    <input type="hidden" name="id" value="' . $value['id'] . '">             
                        <div class="thumbnail">
                        <img src="' . $value['media']['images'][0]['smallUrl'] . '" />
                        </button></form>';
                                                echo $item;
                                                echo '<p></p>';



                                            }
                                        }


                                    }
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
        <!--- panel wrapper div end -->
    </div>
</div>
</body>

</html>
