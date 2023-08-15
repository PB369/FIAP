let botaoCriar = document.querySelector("#botaoCriar");
let listaTarefasUl = document.querySelector("#lista-de-tarefas");
let listatarefas = [];

function criarTarefa(novaTarefa){
    let tarefa = document.createElement("li");
    tarefa.textContent = novaTarefa;
    let botaoRemover = document.createElement("button");
    botaoRemover.textContent = " X ";
    botaoRemover.classList.add("botaoRemover");
    tarefa.appendChild(botaoRemover);
    listaTarefasUl.appendChild(tarefa);

    botaoRemover.addEventListener("click", removerTarefa);
};

function removerTarefa(event) {
    event.preventDefault();
    event.target.parentNode.remove();
};

botaoCriar.addEventListener("click", function(event){
    event.preventDefault();
    let inputTarefa = document.querySelector("#nome-tarefa");
    listatarefas.push(inputTarefa.value);
    criarTarefa(inputTarefa.value);
    inputTarefa.value = "";
});
