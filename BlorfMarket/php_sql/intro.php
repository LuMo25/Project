
<div class="banner-wrapper">
    <div class="banner-container">
        <div class="banner">
            <div class="banner-content">
                <h1>BLORFMλRKET</h1>
                <h2>
                    Черная меза</h2>
            </div>
        </div>
    </div>
</div>
<nav class="navbar navbar-default">

    <div class="container-fluid">
        <div class="menu-wrapper">
            <div id="menu">
                <ul>
                    <li><a href='index.php'>accueil</a></li>
                    <li><a href='catalogue.php'>catalogue</a></li>
                    <?php
                    if (isset($_SESSION['isCo'])) {
                        if ($_SESSION['isCo'] == false) {

                            echo '<li><a href=\'connexion.php\' class="active">connexion</a></li>
                              <li><a href=\'register.php\' class="active">inscription</a></li>';
                        }
                        else {
                            echo '<li><a href=\'cart.php\'">Panier</a></li>
                              <li><a href=\'manage.php\'">géstion</a></li>
                              <li><a href=\'deconnexion.php\' class="active">déconnexion</a></li>';
                        }
                    }
                    else {
                        echo '<li><a href=\'connexion.php\' class="active">connexion</a></li>
                          <li><a href=\'register.php\' class="active">inscription</a></li>';
                    }

                    ?>
                </ul>
            </div>
        </div>
    </div>
</nav>