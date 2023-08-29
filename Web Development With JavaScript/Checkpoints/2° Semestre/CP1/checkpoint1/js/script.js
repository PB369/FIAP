// let botaoCriar = document.querySelector("#botaoCriar");
// let tabelaTarefas = document.querySelector("#tabela-de-tarefas");
// let listaTarefas = [];

// function criarTarefa(novaTarefa){
//     let tarefa = document.createElement("li");
//     tarefa.textContent = novaTarefa;
//     let botaoRemover = document.createElement("button");
//     botaoRemover.textContent = " X ";
//     botaoRemover.classList.add("botaoRemover");
//     tarefa.appendChild(botaoRemover);
//     listaTarefasUl.appendChild(tarefa);

//     botaoRemover.addEventListener("click", function(event){
//         event.preventDefault();
//         let conteudoTarefa = event.target.parentNode.textContent.split(" ");
//         indiceTarefa = listaTarefas.indexOf(conteudoTarefa[0]);
//         listaTarefas.splice(indiceTarefa, 1);
//         event.target.parentNode.remove();
//         console.log(listaTarefas);
//     });
// };


// botaoCriar.addEventListener("click", function(event){
//     event.preventDefault();
//     let inputTarefa = document.querySelector("#nome-tarefa");
//     listaTarefas.push(inputTarefa.value);
//     criarTarefa(inputTarefa.value);
//     console.log(listaTarefas);
//     inputTarefa.value = "";
// });

let nomeTarefa = document.querySelector("#nome-tf");
let descricaoTarefa = document.querySelector("#descricao-tf");
let autorTarefa = document.querySelector("#autor-tf");
let departamentoTarefa = document.querySelector("#departamento-tf");
let importanciaTarefa = document.querySelector("#importancia-tf");
let valorTarefa = document.querySelector("#valor-tf");

let botaoCriar = document.querySelector("#botaoCriar");

let areaTarefas = document.querySelector("#area-tarefas");

botaoCriar.addEventListener("click", function(event){
    event.preventDefault();

    let trTarefa = document.createElement("tr");
    areaTarefas.appendChild(trTarefa);

    let tdTarefaNome = document.createElement("td");
    tdTarefaNome.textContent = nomeTarefa.value;
    trTarefa.appendChild(tdTarefaNome);

    let tdTarefaDescricao = document.createElement("td");
    tdTarefaDescricao.textContent = descricaoTarefa.value;
    trTarefa.appendChild(tdTarefaDescricao);

    let tdTarefaAutor = document.createElement("td");
    tdTarefaAutor.textContent = autorTarefa.value;
    trTarefa.appendChild(tdTarefaAutor);

    let tdTarefaDepartamento = document.createElement("td");
    tdTarefaDepartamento.textContent = departamentoTarefa.value;
    trTarefa.appendChild(tdTarefaDepartamento);

    let tdTarefaImportancia = document.createElement("td");
    tdTarefaImportancia.textContent = importanciaTarefa.value;
    trTarefa.appendChild(tdTarefaImportancia);

    let tdTarefaValor = document.createElement("td");
    tdTarefaValor.textContent = valorTarefa.value;
});