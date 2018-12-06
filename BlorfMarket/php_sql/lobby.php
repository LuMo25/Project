<html>
<head>
    <title>Bienvenue</title>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />

</head>
<body>
<?php
session_start();
if(!$_SESSION['inscription'])
{
    echo "Vous êtes connecté";
    header('location:connexion.php');
}
?>
<fieldset>
    <div align="center">
        <input type="button" value="S'Inscrire" onclick="javascript:location.href='inscription.php'">
        <input type="button" value="Se Connecter" onclick="javascript:location.href='connexion.php'">
    </div>
</fieldset>
</body>