window.onload = function () {
  var btn = document.getElementById('control_01')
  var path = document.getElementById('path-input')
  var btn_file = document.getElementById('control_02')
  var btn_directory = document.getElementById('control_03')
  var dz = document.getElementById('myDropzone')
  path.style.visibility = "hidden";
  btn.addEventListener("click", () => {
    if (this.checked) {
      path.style.visibility = "visible";
      dz.style.visibility = "hidden";
    }
    else {
      path.style.visibility = "hidden";
    }
  });
  btn_file.addEventListener("click", () => {
    if (this.checked) {
      path.style.visibility = "hidden";
      dz.style.visibility = "visible";

    }
    else {
      path.style.visibility = "visible";
      dz.style.visibility = "hidden";

    }
  });
  btn_directory.addEventListener("click", () => {
    if (this.checked) {
      path.style.visibility = "hidden";
      dz.style.visibility = "visible";

    }
    else {
      path.style.visibility = "visible";
      dz.style.visibility = "hidden";

    }
  });
};
