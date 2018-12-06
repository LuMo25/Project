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
    <title>Acheter</title>
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

                                $coo = 0;
                                if (isset($_SESSION['isCo'])) {
                                    if ($_SESSION['isCo'] == 1) {
                                        $coo = 1;
                                    }
                                }

                                if ($coo == 1) {

                                    $dsn = "mysql:host=localhost;port=3306;dbname=supmarket";


                                    try {
                                        $pdo = new PDO($dsn, "root", "");
                                    } catch (PDOException $e) {
                                        die("Error ! : " . $e->getMessage());
                                    }

                                    $sql = "";
                                    if ($_SESSION['role'] == "admin") {
                                        $sql = 'SELECT * FROM recepices WHERE status="pending"';
                                    } else if ($_SESSION['role'] == "guest") {
                                        $sql = 'SELECT * FROM recepices WHERE customer="' . $_SESSION['id'] . '"';
                                    }


                                    $sth = $pdo->query($sql);

                                    $res = $sth->fetchAll();


                                    if ($res == false) {
                                        echo '<p>Aucun objet trouvé</p>';
                                    } else {


                                        $val = "";
                                        foreach ($res as $item) {

                                            $article = $item['articles'];
                                            $cln = "[CustomerLName]";
                                            $cfn = "[CustomerFName]";
                                            $cu = $item['customer'];
                                            $ba = $item['billing_address'];
                                            $da = $item['delivery_address'];
                                            $cb = "CustomerNumber";
                                            $cc = "CustomerCity";
                                            $money = $item['price'];
                                            $cury = $item['currency'];


                                            $val = '
                
                    <div id="item" style="auto;border-style:solid">     
                        <div id="tet" style="background-color:aliceblue">
                            <h1>-- Pending --</h1>
                            <p class="p">SOCIETE</p>
                            <p class="p">BLORFMλRKET(c)</p>  
                            <p class="p">3 rue des tonserensarwel 75000</p>  
                            <p class="p">+455 58 74 15</p>  
                            <p class="p">PORT D\'ALEXENDRE I ET D\'ALEXENDRE A</p>  
                        </div>
                        <div id="tet" style="background-color:aliceblue">
                            <p class="p">CLIENT</p>
                            <p class="p">' . $cln . " " . $cfn . '</p>
                            <p class="p">Customer ID: ' . $cu . '</p> 
                            <p class="p">Delivery address:' . $ba . '</p>  
                            <p class="p">Delivery address:' . $da . '</p>  
                            <p class="p">Phone number: ' . $cb . '</p>  
                            <p class="p">Customer city: ' . $cc . '</p>  
                        </div>
                        <div id="mil" style="background-color:white">
                            <p class="p" >ARTICLES</p>
                            <p> ' . $article . '</p>
                        </div>
                        <div id="milp" style="background-color:beige">
                            <p class="p">PRIX</p>
                            <p class="p">Valeur: ' . $money . '</p>
                            <p class="p">Currency: ' . $cury . '</p>
                        </div>
                        <div id="bas" style="background-color:aliceblue">
                            <p >BLORFMλRKET(c) - Pour être en forme défonce Jean Claude avec un pied de biche</p>
  
                        </div>
                    </div><br>
                    <form action="valrep.php" method="post">
                        <input type="hidden" name="id" value="' . $item['id'] . '">
                        <input type="submit" value="Valider cette commande">
                    </form>
                    <br><br><br><hr><br>
                ';


                                            echo $val;

                                        }
                                    }
                                } else {
                                    echo 'Vous devez être connecté pour acceder à cette page';
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
