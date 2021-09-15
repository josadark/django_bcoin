var parent = document.getElementById("hoverParent");
parent.onmouseover=function(){alert('trigger!');}

var elements = document.getElementsByClassName("hoverParent")
for (var i = 0; i < elements.length; i++){
  elements[i].onmouseover=function(){elements[i].style.background="yellow";}
  elements[i].onmouseout=function(){elements[i].style.background="white";}
}

var tableRows = document.getElementsByTagName('tr');

for (var i = 0; i < tableRows.length; i += 1) {
  tableRows[i].addEventListener('mouseover', function(e){
  alert('moused over');
  });
  // or attachEvent, depends on browser
}
