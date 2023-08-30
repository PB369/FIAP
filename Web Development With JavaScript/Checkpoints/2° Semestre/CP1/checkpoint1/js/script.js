let nomeTarefa = document.querySelector("#nome-tf");
let descricaoTarefa = document.querySelector("#descricao-tf");
let autorTarefa = document.querySelector("#autor-tf");
let departamentoTarefa = document.querySelector("#departamento-tf");
let importanciaTarefa = document.querySelector("#importancia-tf");
let valorTarefa = document.querySelector("#valor-tf");
let duracaoTarefa = document.querySelector("#duracao-tf");

let botaoCriar = document.querySelector("#botaoCriar");

let areaTarefas = document.querySelector("#area-tarefas");

let tarefas = [];


botaoCriar.addEventListener("click", function(event){
    event.preventDefault();
    
    let tarefa = {
        nome: nomeTarefa.value,
        descricao: descricaoTarefa.value,
        autor: autorTarefa.value,
        departamento: departamentoTarefa.value,
        importancia: importanciaTarefa.value,
        valor: valorTarefa.value,
        duracao: duracaoTarefa.value,
    }
    tarefas.push(tarefa);

    nomeTarefa.value = "";
    descricaoTarefa.value = "";
    autorTarefa.value = "";
    departamentoTarefa.value = "";
    importanciaTarefa.value = "";
    valorTarefa.value = "";
    duracaoTarefa.value = "";

    criarTarefa(tarefas);

});

function criarTarefa(tarefas){
    areaTarefas.innerHTML = "";

    tarefas.forEach(tarefa => {
        let trTarefa = document.createElement("tr");
        trTarefa.classList.add("tarefa");
        areaTarefas.appendChild(trTarefa);
    
        let tdTarefaNome = document.createElement("td");
        tdTarefaNome.textContent = tarefa.nome;
        trTarefa.appendChild(tdTarefaNome);
    
        let tdTarefaDescricao = document.createElement("td");
        tdTarefaDescricao.textContent = tarefa.descricao;
        trTarefa.appendChild(tdTarefaDescricao);
    
        let tdTarefaAutor = document.createElement("td");
        tdTarefaAutor.textContent = tarefa.autor;
        trTarefa.appendChild(tdTarefaAutor);
    
        let tdTarefaDepartamento = document.createElement("td");
        tdTarefaDepartamento.textContent = tarefa.departamento;
        trTarefa.appendChild(tdTarefaDepartamento);
    
        let tdTarefaImportancia = document.createElement("td");
        tdTarefaImportancia.textContent = tarefa.importancia;
        trTarefa.appendChild(tdTarefaImportancia);
    
        let tdTarefaValor = document.createElement("td");
        tdTarefaValor.textContent = tarefa.valor;
        trTarefa.appendChild(tdTarefaValor);
        
        let tdTarefaDuracao = document.createElement("td");
        tdTarefaDuracao.textContent = tarefa.duracao;
        trTarefa.appendChild(tdTarefaDuracao);

        let botaoRemover = document.createElement("button");
        botaoRemover.textContent = "X";
        botaoRemover.classList.add("botao-remover");
        trTarefa.appendChild(botaoRemover);
        
        botaoRemover.addEventListener("click", (evt)=>{
            evt.preventDefault();
            evt.target.parentNode.remove();
            tarefas.splice(tarefas.indexOf(tarefa), 1);
            console.log(tarefas);
        })
    })
}

let botaoOrdenar = document.querySelector("#ordenar-tarefas");
botaoOrdenar.addEventListener("click", (evt)=>{
    evt.preventDefault();

    tarefas.sort((tarefa1, tarefa2) => {
        if(tarefa1.importancia < tarefa2.importancia){
            return -1;
        }
        if(tarefa1.importancia > tarefa2.importancia){
            return 1;
        }
        return 0;
    })

    while(areaTarefas.firstChild){
        areaTarefas.removeChild(areaTarefas.firstChild);
    };

    criarTarefa(tarefas);
})
