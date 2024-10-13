import Produto from './produto.js'
document.addEventListener('DOMContentLoaded', function() {

// Array para armazenar os produtos cadastrados
let produtos = [];

// Referências aos elementos do DOM
const formSection = document.getElementById('form-section');
const listSection = document.getElementById('list-section');
const productForm = document.getElementById('product-form');
const productList = document.getElementById('product-list').getElementsByTagName('tbody')[0];


// Adiciona o event listener para o botão "Cadastrar Novo Produto"
const newProductButton = document.getElementById('new-product-button');
newProductButton.addEventListener('click', showForm);


// Função para exibir o formulário de cadastro
function showForm() {
    formSection.classList.remove('hidden');
    listSection.classList.add('hidden');
}

// Função para exibir a listagem de produtos
function showList() {
    formSection.classList.add('hidden');
    listSection.classList.remove('hidden');
    renderProductList();
}

// Evento de envio do formulário
productForm.addEventListener('submit', function(event) {
    event.preventDefault();

    const nome = document.getElementById('product-name').value;
    const descricao = document.getElementById('product-description').value;
    const valor = parseFloat(document.getElementById('product-value').value);
    const disponivel = document.getElementById('product-available').value;

    // Adiciona o novo produto ao array
    produtos.push(new Produto(nome, descricao, valor, disponivel));

    // Limpa o formulário
    productForm.reset();

    // Exibe a listagem após o cadastro
    showList();
});

// Função para renderizar a listagem de produtos
function renderProductList() {
    // Ordena os produtos por valor, do menor para o maior
    produtos.sort((a, b) => a.valor - b.valor);

    // Limpa a listagem anterior
    productList.innerHTML = '';

    // Adiciona cada produto na tabela
    produtos.forEach(produto => {
        const row = document.createElement('tr');
        row.innerHTML = `<td>${produto.nome}</td><td>R$ ${produto.valor.toFixed(2)}</td>`;
        productList.appendChild(row);
    });
}

// Exibe o formulário inicialmente
showForm();
});