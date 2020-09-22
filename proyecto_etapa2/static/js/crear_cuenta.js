
const label=document.querySelector("ul#id_titulo li label").textContent
var cont=0
document.querySelectorAll("ul#id_titulo li input").forEach(function(elem){
        elem.addEventListener("change",(event)=>{
            var x = document.createElement("input");
            x.setAttribute("type", "text");
            var 
            if(elem.checked){

                document.querySelector(".nummatri").appendChild(x); 
            }else{
               
            }    
        })

    })
   



