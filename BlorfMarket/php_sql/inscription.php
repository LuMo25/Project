<!-- Permet d'inscrire les nouveaux clients dans la baseclients grâce à un formulaire -->
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
                                $bdd = new PDO('mysql:host=localhost;dbname=inscription', 'root', '');

                                if(isset($_POST["inscription"]))
                                {
                                    $id = "";
                                    $email = htmlspecialchars($_POST['email']);
                                    $mdp = htmlspecialchars($_POST['mdp']);
                                    $verifmdp = htmlspecialchars($_POST['verifmdp']);
                                    $nomfacture = htmlspecialchars($_POST['nomfacture']);
                                    $adressefacture = htmlspecialchars($_POST['adressefacture']);
                                    $nomlivraison = htmlspecialchars($_POST['nomlivraison']);
                                    $adresselivraison = htmlspecialchars($_POST['adresselivraison']);
                                    $session = 'utilisateur'; /*La personne enregistré sera utilisateur par défaut */

                                    if(!empty($_POST['email']) AND !empty($_POST['mdp']) AND !empty($_POST['verifmdp']) AND !empty($_POST['nomfacture']) AND !empty($_POST['adressefacture']) AND !empty($_POST['nomlivraison']) AND !empty($_POST['adresselivraison']))
                                    {
                                        if($mdp == $verifmdp)
                                        {
                                            $insertclient = $bdd->prepare('INSERT INTO baseclient
						(id, email, mot_de_passe, nom_commande, adresse_commande, nom_livraison, adresse_livraison, session) 
						VALUES(?, ?, ?, ?, ?, ?, ?, ?)');
                                            $insertclient->execute(array(
                                                $id,
                                                $email,
                                                $mdp,
                                                $nomfacture,
                                                $adressefacture,
                                                $nomlivraison,
                                                $adresselivraison,
                                                $session,
                                            ));
                                            $id = $bdd -> lastInsertId();
                                            echo "Vous avez été ajouté dans notre base de données."."<br/>";

                                        }
                                        else
                                        {
                                            echo "vous n'avez pas tapé 2 fois le même mot de passe";
                                        }
                                    }
                                    else
                                    {
                                        echo "Complétez tous les champs";
                                    }
                                }
                                ?>
                                <legend>Formulaire</legend>
                                <form method="POST" action="">
                                    <table>
                                        <br>
                                        <tr>
                                            <td align="right">
                                                <label for="email"> Email:</label>
                                            </td>
                                            <td>
                                                <input type="email" maxlenght="50" value="<?php if(isset($email)) {echo $email;}?>"   placeholder="ex : blorf@blorf.blorf" id="email" name="email">
                                            </td>
                                        </tr>
                                        <tr>
                                            <td align="right">
                                                <label for="mdp"> Mot de Passe:</label>
                                            </td>
                                            <td>
                                                <input type="password" maxlenght="25" id="mdp" name="mdp">
                                            </td>
                                        </tr>
                                        <tr>
                                            <td align="right">
                                                <label for="verifmdp">Vérification Mot de Passe:</label>
                                            </td>
                                            <td>
                                                <input type="password" maxlenght="25" id="verifmdp" name="verifmdp">
                                            </td>
                                        </tr>
                                        <tr>
                                            <td align="right">
                                                <label for="adressedefacturation"> Adresse de Facturation</label>
                                            </td>
                                        <tr>
                                            <td align="right">
                                                <label for="nomfacture"> Nom de la personne qui commande:</label>
                                            </td>
                                            <td>                                          <!-- si la variable est créer cela va afficher la variable. Cela permet d'éviter que les données disparaissent si on submit. -->
                                                <input type="text" maxlenght="25" value="<?php if(isset($nomfacture)) {echo $nomfacture;}?>"   placeholder="ex: blorf" id="nomfacture" name="nomfacture">
                                            </td>
                                        </tr>
                                        <tr>
                                            <td align="right">
                                                <label for="adressefacture"> Adresse:</label>
                                            </td>
                                            <td>                                          <!-- si la variable est créer cela va afficher la variable. Cela permet d'éviter que les données disparaissent si on submit. -->
                                                <input type="text" maxlenght="100" value="<?php if(isset($adressefacture)) {echo $adressefacture;}?>"   placeholder="ex: Ton Ser du 65" id="addressefacture" name="adressefacture">
                                            </td>
                                        </tr>

                                        <tr>
                                            <td align="right">
                                                <label for="adressedelivraison"> Adresse de Livraison</label>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td align="right">
                                                <label for="nomlivraison"> Nom de la personne livrée:</label>
                                            </td>
                                            <td>
                                                <input type="text" maxlenght="25" value="<?php if(isset($nomlivraison)) {echo $nomlivraison;}?>"   placeholder="ex : Poulpe" id="nomlivraison" name="nomlivraison">
                                            </td>
                                        </tr>
                                        <tr>
                                            <td align="right">
                                                <label for="adresselivraison"> Adresse:</label>
                                            </td>
                                            <td>
                                                <input type="text" maxlenght="100" value="<?php if(isset($adresselivraison)) {echo $adresselivraison;}?>"   placeholder="ex : 5Y jambon du 82" id="adresselivraison" name="adresselivraison">
                                            </td>
                                        </tr>
                                    </table>
                                    <div align="center">
                                        <input type="submit" value="Ajouter" name="inscription"/>
                                    </div>
                                </form>
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