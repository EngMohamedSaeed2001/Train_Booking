function validate ()
{
    var trpid = document.getElementById("ti").value;
    var trnid = document.getElementById("tri").value;
    var scity = document.getElementById("sc").value;
    var dcity = document.getElementById("dc").value;
    var tdate = document.getElementById("d").value;
    var aseats = document.getElementById("avs").value;
    

    let i=0;
    let ti=0;
    let s=0;
    let d=0;
    let td=0;
    let as=0;



    if(trpid == "")
    {
      alert("Trip Id cannot be blank");
      i=0;   
    }
    else if(trpid.length != 4)
    {
      alert("Id must be 4 digits");
      i=0;    
    }
    else
    {
      i=1;
    }

    if (scity == "")
    {
       alert("Source city cannot be blank ");
       s=0;
    }
    else
    {
       s=1;
    }

    if (dcity == "")
    {
       alert("Destination city cannot be blank ");
       d=0;
    }
    else
    {
       d=1;
    }

    if (tdate == "")
    {
        alert("Trip date cannot be blank ");
        td=0;
    }
    else if (tdate.getDay()<32 && tdate.getDay() <0)
    {
        alert("Trip day should be between 1 and 31 ");
        td=0;
    }
    else if (tdate.getMonth()<13 && tdate.getMonth() <0)
    {
        alert("Trip month should be between 1 and 12 ");
        td=0;
    }
    else if (tdate.getFullYear()>2020)
    {
        alert("Trip month should be in the current year or above ");
        td=0;
    }
    else 
    {
        td=1;
    }

    if(aseats == "")
    {
      alert("Number of seats cannot be blank");
      as=0;   
    }
    else if(aseats.length < 5 )
    {
      alert("Id cannot be more than 4 digits");
      as=0;    
    }
    else
    {
      as=1;
    }
    if(trnid == "")
    {
      alert("Train Id cannot be blank");
      ti=0;   
    }
    else if(trnid.length != 4)
    {
      alert("Id must be 4 digits");
      ti=0;    
    }
    else
    {
      ti=1;
    }

    if (i==1 && s==1 && d==1 && as==1 && td==1 && ti==1)
    {
        return true;
    }
    else
    {
        return false;
    }
}