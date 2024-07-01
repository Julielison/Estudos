import flags from "./model/flags.js";

function generateHTML() {
  let classe = document.querySelector(".row");
  flags.forEach((obj) => {
    let html = `<div class="flag col-2 my-2 text-center">
                    <img src="${obj.image}" alt="${obj.name}">
                    <p>${obj.name}</p>
                </div>`;
    classe.insertAdjacentHTML("beforeend", html);
  });
}
generateHTML();