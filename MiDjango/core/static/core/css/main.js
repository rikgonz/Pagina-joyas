//	Jquery del dolar

$(document).ready(function () {
  $.get("https://mindicador.cl/api", function (data) {
    $("#dolar-valor").html(data.dolar.valor);
  });
});

// jquery del euro

$(document).ready(function () {
  $.get("https://mindicador.cl/api", function (data) {
    $("#euro-valor").html(data.euro.valor);
  });
});

/*// jquery de la plata en clp

$(document).ready(function () {
  $.get(
    "https://api.metalpriceapi.com/v1/latest?api_key=d83dbb92608e38b208b48b68d64507d8&base=CLP&currencies=XAG",
    function (data) {
      $("#plata-valor").html(data.rates.XAG);
    }
  );
});

// jquery de la plata en usd

$(document).ready(function () {
  $.get(
    "https://api.metalpriceapi.com/v1/latest?api_key=d83dbb92608e38b208b48b68d64507d8&base=USD&currencies=XAG",
    function (data) {
      $("#plata-valor2").html(data.rates.XAG);
    }
  );
});
*/

// Example starter JavaScript for disabling form submissions if there are invalid fields
(() => {
  "use strict";

  // Fetch all the forms we want to apply custom Bootstrap validation styles to
  const forms = document.querySelectorAll(".needs-validation");

  // Loop over them and prevent submission
  Array.from(forms).forEach((form) => {
    form.addEventListener(
      "submit",
      (event) => {
        if (!form.checkValidity()) {
          event.preventDefault();
          event.stopPropagation();
        }

        form.classList.add("was-validated");
      },
      false
    );
  });
})();

// modal

const myModal = document.getElementById("myModal");
const myInput = document.getElementById("myInput");

myModal.addEventListener("shown.bs.modal", () => {
  myInput.focus();
});
