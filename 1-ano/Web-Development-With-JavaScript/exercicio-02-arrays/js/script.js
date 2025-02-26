let salarios = [1235, 1450, 1622, 1792, 1980, 2050, 2344, 3000, 3480, 4100];

// Filtrando os salarios menores e maiores e calculando o aumento salarial:
let menoresSalarios = salarios.filter(salario => salario<=2000);

let mais15 = menoresSalarios.map(menoresSalarios => (menoresSalarios * 0.15) + menoresSalarios);

let maioresSalarios = salarios.filter(salario => salario>2000);

let mais10 = maioresSalarios.map(maioresSalarios => (maioresSalarios * 0.10) + maioresSalarios);


// Exibindo no console os resultados obtidos acima:
console.log(`Os salários menores que 2000 são estes: ${menoresSalarios}`);
console.log(`Estes salários com um aumento de 15% ficaram assim: ${mais15}`);

console.log("\n");

console.log(`Os salários maiores que 2000 são estes: ${maioresSalarios}`);
console.log(`Estes salários com um aumento de 10% ficaram assim: ${mais10}`);

console.log("\n");

let novosSalarios = [...mais10, ...mais15];

// Realizando uma nova seleção dos novos salários maiores que 2500:
let topSalarios = novosSalarios.filter(salario => salario>2500);
console.log(`Os salários maiores que 2500 (considerando o aumento) são estes: ${novosSalarios}`);

// Fazendo a soma dos salários maiores que 2500:
let somaTopSalarios = topSalarios.reduce((somatoria, salarioAtual) => somatoria + salarioAtual);
console.log(`A soma destes salários maiores é ${somaTopSalarios}`);