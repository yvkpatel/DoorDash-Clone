/*<!DOCTYPE html>
<html>
<body>

<h2>Creating an Object from a JSON Literal</h2>
<p id="demo"></p>

<script>
*/


function makePayJSON(a,b,c,d,e,f)
{
var obj = new Object();
//TODO change obj items to all required things
obj.ccv = a;
obj.card_number = b;
obj.expiry = c;
obj.name = d;
obj.total = e;
obj.postal_code = f;


//make JSON string
var JSONstring = JSON.stringify(obj, null, 2);

//print (just for testing)
alert(JSONstring);

//return the string
return JSONstring;
}

//makePayJSON(1,2,"three","Joe",100,"A1A1A1");
getPayInfo(1,2,"three","Joe",100,"A1A1A1");
/*
</script>

</body>
</html>
*/