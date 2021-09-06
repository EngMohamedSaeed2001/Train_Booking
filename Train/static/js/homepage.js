function myFunction()
{
    var x = document.getElementById("myInput");
    if (x.type === "password") {
      x.type = "text";
    } else {
      x.type = "password";
    }
}

function validate()
{
    var username = document.getElementById("un").value;
    var password = document.getElementById("myInput").value;

    let u=0;
    let p=0;
    
    if (username == "")
    {
       alert("Username cannot be blank ");
       u=0;
    }
    else
    {
       u=1;
    }

    if (password == "")
    {
      alert("password cannot be blank");
      p=0;
    }
    else if(password.length<9)
    {
      alert("password cannot be less than 9 digits");
      p=0;
    }
    else
    {
      p=1;
    }
    if (u==1 && p==1 )
    {
        return true;
    }
    else
    {
        return false;
    }

}