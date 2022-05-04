window.onload = function () {
  var btn = document.getElementById('control_01')
  var btn_file = document.getElementById('control_02')
  var dz = document.getElementById('myDropzone')
  dz.style.visibility = "hidden";
  btn.addEventListener("click", () => {
    if (this.checked) {
      dz.style.visibility = "visible";
    }
    else {
      dz.style.visibility = "hidden";
    }
  });
  btn_file.addEventListener("click", () => {
    if (this.checked) {
      dz.style.visibility = "hidden";

    }
    else {
      dz.style.visibility = "visible";
    }
  });
};
