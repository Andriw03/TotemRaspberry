console.log('entro al script');
const Gpio = require("onoff").Gpio;
const pushBottonIn = new Gpio(23,"in","both");
const pushBottonOut = new Gpio(24, "in","both");
const entrada = document.getElementByID('btnEntrada');
pushBottonIn.watch(( err , value ) =>{
  console.log("chao uwu");
  if(err){
    console.log("hay un error uwu", err);
    return;
  }
  
})
pushBottonOut.watch(function( err , value )  {
  console.log("hola");
  if(err){
    console.log("hay un error uwu", err);
    return;
  }
  
});
entrada.addEventListener('click',()=>{
    console.log('se clickeo entrada');
    
});