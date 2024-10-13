inputCep = document.getElementById('cep');

inputCep.addEventListener('keydown', (event) => {
    if (event.key === 'Enter' && inputCep.value !== 8) {
        event.preventDefault();
        
        // Invalida o cep digitado
        inputCep.value = '';
        inputCep.placeholder = 'O CEP deve ter 8 dígitos';
        let data = {erro: true};
        validData(data);
    }
});

inputCep.addEventListener('input', async (event) =>  {
    const cepValue = event.target.value;
    
    // Faz o fetch apenas quando o tamanho do cep digitado é igual a 8
    if (cepValue.length === 8) {
      const url = `https://viacep.com.br/ws/${cepValue}/json/`;

      fetch(url)
        .then(response => response.json())
        .then(data => {
                if (validData(data)) {
                    insertDataIntoHtml(data);
                    document.getElementById('number').focus();
                }
        })
        .catch(error => console.error('Erro:', error));
    }
});


function validData(data){
    const cepError = document.getElementById('cepError');
    const cep = document.getElementById('cep');

    // Mostra a div caso o cep seja inválido
    if (data.erro){
        cepError.classList.remove('hidden');
        cep.classList.add('input-cep-error');
        clearFormFields();
        return false;
    // Esconde a div
    } else {
        cepError.classList.add('hidden');
        cep.classList.remove('input-cep-error');
        return true;
    }
}

function clearFormFields() {
    // Seleciona todos os campos de entrada com base em seus IDs
    const fieldIds = ['logradouro', 'bairro', 'uf', 'localidade'];
    
    // Itera sobre cada ID e limpa o campo correspondente
    fieldIds.forEach(id => {
        document.getElementById(id).value = '';
    });
}


function insertDataIntoHtml(data){
    const fieldIds = ['logradouro', 'bairro', 'uf', 'localidade'];

    fieldIds.forEach(id => 
        document.getElementById(id).value = data[id]);
}