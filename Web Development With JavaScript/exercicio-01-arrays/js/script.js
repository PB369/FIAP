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

    botaoRemover.addEventListener("click", function(event){
        event.preventDefault();
        let conteudoTarefa = event.target.parentNode.textContent.split(" ");
        indiceTarefa = listaTarefas.indexOf(conteudoTarefa[0]);
        listaTarefas.splice(indiceTarefa, 1);
        event.target.parentNode.remove();
        console.log(listaTarefas);
    });
};


botaoCriar.addEventListener("click", function(event){
    event.preventDefault();
    let inputTarefa = document.querySelector("#nome-tarefa");
    listaTarefas.push(inputTarefa.value);
    criarTarefa(inputTarefa.value);
    console.log(listaTarefas);
    inputTarefa.value = "";
});
