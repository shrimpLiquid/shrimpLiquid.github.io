console.log("sand");
function GO(){
    console.log("sand");
    document.getElementById("allofit").remove();



  // create a new div element
  newDiv = document.createElement("script");

  newDiv.src = "https://kitao.dev/pyxel/2.9.9/pyxel.js"

  document.body.append(newDiv);
  
//   newDiv = document.createElement("pyxel-run");

//   newDiv.name="sand.py";
//   newDiv.root=".";

  document.body.append(document.createRange().createContextualFragment('<pyxel-run root="." name="sand.py"></pyxel-run>'));

addElement();


}