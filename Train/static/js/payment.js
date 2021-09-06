function validate()
{
    var cardNo = document.getElementById("myInput").value;
    var securityNo = document.getElementById("pn").value;

    let cn=0;
    let sn=0;

    // Card number validation
    if(cardNo == "")
    {
      alert("Card number cannot be blank");
      cn=0;   
    }
    else if(cardNo.length != 16)
    {
      alert("Card number must be 16 digits");
      cn=0;    
    }
    else
    {
      cn=1;
    }

    //Security code validation
    if(securityNo == "")
    {
      alert("Security code cannot be blank");
      sn=0;   
    }
    else if(securityNo.length != 3)
    {
      alert("Security code be 4 digits");
      sn=0;    
    }
    else
    {
      sn=1;
    }

    if (cn==1 && sn==1)
    {
        return true;
    }
    else
    {
        return false;
    }
}