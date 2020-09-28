const telefono=document.getElementById("id_telefono")
const nombre = document.getElementById('id_first_name')
const apellido = document.getElementById('id_last_name')
const dni = document.getElementById('id_dni')
var validartelefono= /^\d{10}$/
var viejotelefono=document.getElementById("id_telefono").value
if (document.getElementById('id_dni')!=null){
var viejodni = document.getElementById('id_dni').value
}

telefono.addEventListener("change",(event)=>{
    vtelefono=document.getElementById("id_telefono").value
    if(vtelefono.trim() == '' || isNaN(vtelefono) || !validartelefono.test(vtelefono) || vtelefono.length > 15){
        alert('Debe un valor de Telefono valido')
        document.getElementById("id_telefono").value=viejotelefono
        document.getElementById("id_telefono").focus()
    }  
        })

if (nombre!=null){
nombre.addEventListener("change",(event)=>{
    vnombre=document.getElementById("id_first_name").value
    if(vnombre.trim() == '' || !isNaN(vnombre) || vnombre.length > 35){
        alert('Debe ingresar el Nombre')
        document.getElementById("id_first_name").value=""
        document.getElementById("id_first_name").focus()
            }
        })
}
if (apellido!=null){
apellido.addEventListener("change",(event)=>{
    vapellido=document.getElementById("id_last_name").value
    if (vapellido.trim() == '' || !isNaN(vapellido) || vapellido.length > 35){
        alert('Debe ingresar el Apellido')
        document.getElementById("id_last_name").value=""
        document.getElementById("id_last_name").focus()
    }  
        })
}
if (document.getElementById('id_dni')!=null){
dni.addEventListener("change",(event)=>{
    vdni=document.getElementById("id_dni").value
    if(vdni.trim() == '' || isNaN(vdni) || vdni.length > 9){
        alert('Debe un valor de Dni valido')
        document.getElementById("id_dni").value=viejodni
        document.getElementById("id_dni").focus()
    }  
        })
}