console.log("sand");
function GO(){
    console.log("sand");
    document.getElementById("allofit").remove();



  
//   newDiv = document.createElement("pyxel-run");

//   newDiv.name="sand.py";
//   newDiv.root=".";

  document.body.append(document.createRange().createContextualFragment('<pyxel-run root="." name="sand.py"></pyxel-run>'));

addElement();


}