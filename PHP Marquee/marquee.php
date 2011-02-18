<!DOCTYPE html>
<html>
    <head>
        <title><3</title>
        <style type="text/css">
        <!--/* Edit this */-->
        marquee {
            z-index:2;
            position:absolute;
            font-family:Times;
            font-size:36pt;
            color:#FF0000;
        }
        </style>
    </head>
    <body>
    <?php
    // Edit these
    $times_to_spam = 10;
    $text = "&lt;3";
    // 
    function marquee($var0) {
        echo "<marquee style=\"left:" . rand(0,150) . "; top:" . rand(0,115) . "; height:" . rand(0,500) . ";\" scrollamount=\"". rand(0,10) . "\" direction=\"down\">" . $var0 . "</marquee>\n";
    }
    for( $i = 0; $i < $times_to_spam; $i++ ) {
        marquee($text);
    }
    ?>
    </body>
</html>