<!DOCTYPE html>
<html>
<head>
<title>Em</title>
<style type="text/css">
	.queryin{
		margin: 0;
		padding: 8px 10px;
		font-family: Arial, Helvetica, sans-serif;
		font-size:14px;
		border:1px solid #000000; border-right:0px;
		border-top-left-radius: 5px 5px;
		border-bottom-left-radius: 5px 5px;
	}
	.button {
		margin: 0;
		padding: 8px 15px;
		font-family: Arial, Helvetica, sans-serif;
		font-size:14px;		
		text-align: center;
		color: #ffffff;
		background: #000000;
		border: solid 1px #000000; border-right:0px;
		border-top-right-radius: 15px 15px;
		border-bottom-right-radius: 15px 15px;
	}
	.center {
  		margin: 0 auto;
  		width: 300px;
    }
</style>
</head>
<body>
	<div id="tfheader" class="center">
		<br><br><br>
		<form action="eminem.php" method="post">	        
		    <input type="text" class="queryin" name="query"><input type="submit" name="submit1" value="query" class="button">
		</form>
		<br><br>
		<?php
			if (isset($_POST['submit1'])){
				$string = $_POST['query'];
				$res = exec("/usr/bin/python3 similar.py $string");
				$resarray = json_decode($res,true);
				print "top 10 matches for $string <br><br>";
				foreach ($resarray as list($a,$b)){
					print "$a : $b <br>";
				};
			}
			else{

			}
		?>
	</div>
</body>
</html>
