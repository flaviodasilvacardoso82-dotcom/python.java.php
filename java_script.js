let valor = null
if (valor) {
    console.log('is True')
}
else{
    console.log('is false')
}

let arrays = [1, 2, 3, 4, 5, 6, 7, 8, 9];
arrays.push(1);

console.log('OLA MUNDO')

let vba = true

const nome_do_modulo = require('node:readline')

const entrada_terminal = nome_do_modulo.createInterface({
    input: process.stdin,
    output: process.stdout
})

entrada_terminal.question('Digite seu nome: ', (nome) => {
    console.log(nome)

    entrada_terminal.close()
})

for (const valorArray of arrays) {
    console.log(valorArray);
}
