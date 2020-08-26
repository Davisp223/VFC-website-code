<?php
if (isset($_POST['signup-submit'])) {
    require 'https://virtualfarmingcommunity.com/Connect.php';

 $username = $_post['username'];
 $email = $_post['email'];
 $password = $_post['password'];
 $passwordrepeat = $_post['passwordrepeat'];
 
 if (empty($username) || empty($email) || empty($password) || empty($passwordrepeat)) {

    exit();
  }
 
   else {
     
   $sql = "SELECT username FROM users WHERE username=?";
   $stmt = mysqli_stmt_init($conn);
   if (!mysqli_stmt_prepare($stmt, $sql)){
    header( "location: https://virtualfarmingcommunity.com/Signup.html?sqlerror");
    exit();
   } 
  else {
    mysqli_stmt_bind_param($stmt, "s", $username);
    mysqli_stmt_execute($stmt);
    mysqli_stmt_store_results($stmt);
    $resultCheck = mysqli_stmt_num_rows($stmt);
    if ($resultCheck > 0){
        header( "location: https://virtualfarmingcommunity.com/Signup.html?User-taken");
        exit();
    }
    else {
        $sql = "INSERT INTO users (username, email, password) VALUES(?, ?, ?)";
        $stmt = mysqli_stmt_init($conn);
        if (!mysqli_stmt_prepare($stmt, $sql)){
            header( "location: https://virtualfarmingcommunity.com/Signup.html?sqlerror");
            exit();
           } 
           else {
               $hashedpassword = password_hash($password, PASSWORD_DEFAULT);
            mysqli_stmt_bind_param($stmt, "sss", $username, $email, $hashedpassword);
            mysqli_stmt_execute($stmt);

            header( "location: https://virtualfarmingcommunity.com/VFC-login.html");
            exit();
            
     }
    }
   }
  }
 }
 
 

 else{
    header( "location: https://virtualfarmingcommunity.com/Signup.html?failed");
            exit();
 }



