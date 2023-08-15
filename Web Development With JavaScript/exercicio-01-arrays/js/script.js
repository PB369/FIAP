let botaoCriar = document.querySelector("#botaoCriar");
let listaTarefasUl = document.querySelector("#lista-de-tarefas");
let listaTarefas = [];

function criarTarefa(novaTarefa){
    let tarefa = document.createElement("li");
    tarefa.textContent = novaTarefa;
    let botaoRemover = document.createElement("button");
    botaoRemover.textContent = " X ";
    botaoRemover.classList.add("botaoRemover");
    tarefa.appendChild(botaoRemover);
    listaTarefasUl.appendChild(tarefa);

    console.log(listaTarefas);
    botaoRemover.addEventListener("click", removerTarefa);
};

function removerTarefa(event, conteudoTarefa) {
    event.preventDefault();
    event.target.parentNode.remove();
    indiceTarefa = listaTarefas.indexOf(conteudoTarefa);
    listaTarefas.splice(indiceTarefa, 1);
    console.log(listaTarefas);
};

botaoCriar.addEventListener("click", function(event){
    event.preventDefault();
    let inputTarefa = document.querySelector("#nome-tarefa");
    listaTarefas.push(inputTarefa.value);
    criarTarefa(inputTarefa.value);
    inputTarefa.value = "";
});
