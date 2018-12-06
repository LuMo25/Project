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
    <title>Accueil</title>

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
                                <h1>catalogue:</h1>
                                <hr>
                                <p>Rechercher</p>
                                <form action="catalogue.php" method="get">
                                    <label>Sexe: </label><select name="gender"><option value="all">Tous</option><option value="female">Femme</option><option value="male">Homme</option></select>
                                    <br>
                                    <label>Saison: </label><select name="season"><option value="all">Toutes</option><option value="winter">Hiver</option><option value="fall">Automne</option><option value="summer">Ete</option><option value="spring">Printemps</option></select>
                                    <br>
                                    <input type="submit" value="Rechercher">
                                </form>
                                <hr>
                                <?php
                                $url = 'https://api.zalando.com/articles?';
                                if(isset($_GET['gender'])) {
                                    if($_GET['gender'] != NULL) {
                                        if($_GET['gender'] != "all") {
                                            $url = $url . "gender=" . $_GET['gender'] . "&";
                                        }
                                    }
                                }
                                if(isset($_GET['season'])) {
                                    if($_GET['season'] != NULL) {
                                        if($_GET['season'] != "all") {
                                            $url = $url . "season=" . $_GET['season'] . "&";
                                        }
                                    }
                                }
                                $content = @file_get_contents($url);

                                $error = 0;
                                if($content === FALSE){
                                    $error = $error + 1;
                                    echo 'nothing found! :(';
                                }
                                if($error < 1) {
                                    $json = json_decode($content, true);
                                    foreach ($json['content'] as $value) {
                                        $item = '
                                <a>' . $value['name'] . '</a><br>
                                <li href=article?id=' . $value['id'] . '><img src="' . $value['media']['images'][0]['smallUrl'] . '" alt="item"></li>';
                                        echo $item;
                                        echo '<br><br>';

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
