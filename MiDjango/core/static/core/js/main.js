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

// jquery de la plata en clp

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


const btnCart = document.querySelector(".container-cart-icon");
const containerCartProducts = document.querySelector(
  ".container-cart-products"
);

btnCart.addEventListener("click", () => {
  containerCartProducts.classList.toggle("hidden-cart");
});

/* ========================= */
const cartInfo = document.querySelector(".cart-product");
const rowProduct = document.querySelector(".row-product");

// Lista de todos los contenedores de productos
const productsList = document.querySelector(".container-items");

// Variable de arreglos de Productos
let allProducts = [];

const valorTotal = document.querySelector(".total-pagar");

const countProducts = document.querySelector("#contador-productos");

const cartEmpty = document.querySelector(".cart-empty");
const cartTotal = document.querySelector(".cart-total");

window.addEventListener("load", () => {
  const products = localStorage.getItem("products");
  if (products) {
    allProducts = JSON.parse(products);
    showHTML();
  }
});

productsList.addEventListener("click", (e) => {
  if (e.target.classList.contains("btn-add-cart")) {
    const product = e.target.parentElement;

    const infoProduct = {
      quantity: 1,
      title: product.querySelector("h2").textContent,
      price: product.querySelector("p").textContent,
    };

    const exits = allProducts.some(
      (product) => product.title === infoProduct.title
    );

    if (exits) {
      const products = allProducts.map((product) => {
        if (product.title === infoProduct.title) {
          product.quantity++;
          return product;
        } else {
          return product;
        }
      });
      allProducts = [...products];
    } else {
      allProducts = [...allProducts, infoProduct];
    }

    showHTML();
  }
});

rowProduct.addEventListener("click", (e) => {
  if (e.target.classList.contains("icon-close")) {
    const product = e.target.parentElement;
    const title = product.querySelector("p").textContent;

    allProducts = allProducts.filter((product) => product.title !== title);

    console.log(allProducts);

    showHTML();
  }
});

// Funcion para mostrar  HTML
const showHTML = () => {
  if (!allProducts.length) {
    cartEmpty.classList.remove("hidden");
    rowProduct.classList.add("hidden");
    cartTotal.classList.add("hidden");
  } else {
    cartEmpty.classList.add("hidden");
    rowProduct.classList.remove("hidden");
    cartTotal.classList.remove("hidden");
  }

  // Limpiar HTML
  rowProduct.innerHTML = "";

  let total = 0;
  let totalOfProducts = 0;

  allProducts.forEach((product) => {
    const containerProduct = document.createElement("div");
    containerProduct.classList.add("cart-product");

    containerProduct.innerHTML = `
            <div class="info-cart-product">
                <span class="cantidad-producto-carrito">${product.quantity}</span>
                <p class="titulo-producto-carrito">${product.title}</p>
                <span class="precio-producto-carrito">${product.price}</span>
            </div>
            <svg
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
                stroke-width="1.5"
                stroke="currentColor"
                class="icon-close"
            >
                <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    d="M6 18L18 6M6 6l12 12"
                />
            </svg>
        `;

    rowProduct.append(containerProduct);

    total = total + parseInt(product.quantity * product.price.slice(1));
    totalOfProducts = totalOfProducts + product.quantity;
  });

  valorTotal.innerText = `$${total}`;
  countProducts.innerText = totalOfProducts;
};

const saveProductsToLocalStorage = () => {
  localStorage.setItem("products", JSON.stringify(allProducts));
};

productsList.addEventListener("click", (e) => {
  // ...código anterior para agregar producto
  showHTML();
  saveProductsToLocalStorage();
});

rowProduct.addEventListener("click", (e) => {
  // ...código anterior para eliminar producto
  showHTML();
  saveProductsToLocalStorage();
});

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
