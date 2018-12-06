/* When the user clicks on the button, 
toggle between hiding and showing the dropdown content */
function myFunction5() {
    document.getElementById("myDropdownsecteur5").classList.toggle("showsecteur");
}
function myFunction4() {
    document.getElementById("myDropdownsecteur4").classList.toggle("showsecteur");
}
function myFunction3() {
    document.getElementById("myDropdownsecteur3").classList.toggle("showsecteur");
}
function myFunction2() {
    document.getElementById("myDropdownsecteur2").classList.toggle("showsecteur");
}
function myFunction1() {
    document.getElementById("myDropdownsecteur").classList.toggle("showsecteur");
}

// Close the dropdown menu if the user clicks outside of it
window.onclick = function(event) {
  if (!event.target.matches('.dropbtnsecteur')) {

    var dropdowns = document.getElementsByClassName("dropdownsecteur-content");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('showsecteur')) {
        openDropdown.classList.remove('showsecteur');
      }
    }
  }
}