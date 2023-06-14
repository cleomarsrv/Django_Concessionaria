var index = 0;
var divImagem = document.getElementById("imagem");

var todasImagensHtml = document.getElementById("todasImagens");
var todasImagens = todasImagensHtml.value.split(",");

function exibirImagem() {
    divImagem.src = todasImagens[index]
    index = (index + 1) % todasImagens.length;
}

exibirImagem()
setInterval(exibirImagem, 2000)
