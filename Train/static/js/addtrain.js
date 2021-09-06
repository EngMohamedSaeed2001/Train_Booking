
function check ()
{
    var tname = document.getElementById("trname").value;
    var tid = document.getElementById("trnid").value;
    var nseats = document.getElementById("nos").value;
    var carr = document.getElementById("carriages").value;
    

    let i=0;
    let tn=0;
    let n=0;
    let c=0;


    if (tname == "")
    {
       alert("Train name cannot be blank ");
       
       tn=0;

    }
    else
    {
       tn=1;
    }

   /* if(tid == "")
    {
      alert("Train Id cannot be blank");
      i=0;   
    }
    else if(tid.length != 4)
    {
      alert("Id must be 4 digits");
      i=0;    
    }
    else
    {
      i=1;
    }

    if(nseats == "")
    {
      alert("Number of seats cannot be blank");
      n=0;   
    }
    else if(nseats.length < 5 )
    {
      alert("Number of seats cannot be more than 4 digits");
      n=0;    
    }
    else
    {
      n=1;
    }

    if(carr == "")
    {
      alert("carriages cannot be blank");
      c=0;   
    }
    else if(carr.length < 5 )
    {
      alert("Carriages cannot be more than 4 digits");
      c=0;    
    }
    else
    {
      c=1;
    }*/

    if (tn==1 && i==1 && n==1 && c==1)
    {
        return true;
    }
    else
    {
        return false;
    }
}