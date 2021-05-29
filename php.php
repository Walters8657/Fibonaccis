<?php
  function fib($n) {
    $f1 = 0;
    $f2 = 1;
    $i = 1;

    if ($n < 1) {
      return;
    }

    echo $f1, PHP_EOL;

    while ($i < $n) {
      echo $f2, PHP_EOL;

      $next = $f1 + $f2;
      $f1 = $f2;
      $f2 = $next;
      $i++;
    }
  }

  $num = readline("How many numbers do you want? ");

  fib($num);
?>