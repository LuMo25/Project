<?php session_start(); ?>

<?php
    
    $error = 0;
    if (isset($_POST['id'])) {
        if ($_POST['id'] == NULL) {
            $error = $error + 1;
        }
    } else {
        $error = $error + 1;
    }
    
    if ($error == 0) {


        $id = $_POST['id'];
        $conn = new mysqli('localhost', 'root', '', 'supmarket');
        if ($conn->connect_error) {
            die("Connection failed: " . $conn->connect_error);
        }
        $sql = 'UPDATE recepice
            SET status="done"
            WHERE id="' . $_id . '"
            ';

        if ($conn->query($sql) === TRUE) {
            echo 'done';

        } else {

            echo "Error: " . $sql . "<br>" . $conn->error;
        }
        echo '<a href="index.php">blorf</a>';

        $conn->close();


    }
?>
