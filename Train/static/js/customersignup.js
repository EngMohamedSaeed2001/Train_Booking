function validate()
{
    var username = document.getElementById("un").value;
    var password = document.getElementById("myInput").value;
    var phone = document.getElementById("pn").value;
    var email = document.getElementById("E-Mail").value;
    var hcity = document.getElementById("city").value;

    var u=0;
    var p=0;
    var ph=0;
    var e=0;
    var c=0;

    // username validation
    if (username == "")
    {
       alert("Username cannot be blank ");
       u=0;
    }
    else
    {
       u=1;
    }

    //password validation 
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
    // phone number validation
    if (phone == "")
    {
      alert("Phone number cannot be blank");
      ph=0;
    }
    else if(phone.length<11)
    {
      alert("phone number cannot be less than 11 digits");
      ph=0;
    }
    else
    {
      ph=1;
    }
    if(email == "")
    {
      alert("Email cannot be blank");
      e=0;
    }
    else if(email.indexOf('@')<3||email.lastIndexOf('.')>=email.length-2)
    {
      alert("Invalid email");
      e=0;
    }
    else
    {
      e=1;
    }
    if (hcity == "")
    {
       alert("Home city cannot be blank ");
       c=0;
    }
    else
    {
       c=1;
    }
    if (u==1 && c==1 && p==1 && ph==1 && e==1)
    {
        return true;
    }
    else
    {
        return false;
    }


    


}