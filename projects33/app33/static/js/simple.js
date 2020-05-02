function f1()
{
 var en=document.getElementById("e").value
  var ka=document.getElementById("k").value
   var hi=document.getElementById("h").value
    var so=document.getElementById("s").value
     var sos=document.getElementById("ss").value
     var mat=document.getElementById("m").value
     var to=document.getElementById("t")
    var z= parseInt(en)+parseInt(ka)+parseInt(hi)+parseInt(so)+parseInt(sos)+parseInt(mat)
    to.innerHTML= "TOTAL MARK="+z
}
function f2()
{
     var en=document.getElementById("e").value
  var ka=document.getElementById("k").value
   var hi=document.getElementById("h").value
    var so=document.getElementById("s").value
     var sos=document.getElementById("ss").value
     var mat=document.getElementById("m").value
    var pe=document.getElementById("p")
    var x=((parseInt(en)+parseInt(ka)+parseInt(hi)+parseInt(so)+parseInt(sos)+parseInt(mat))/6)
    pe.innerText=x
}