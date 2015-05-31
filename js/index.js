$(function(){
    $.ajax({
        type:'GET',
        url: 'relatos/relatos.html',
        success:parseArquivoDeRelatos
    })
})

function parseArquivoDeRelatos(arquivo){
    var tokens, data, titulo, relatoBianca, relatoIsrael, imagem;
    var contador = 0

    for(let linha of arquivo.split('\n')){
        if(linha.startsWith('-') || linha.trim() == '')
            continue;
        contador++
        if(contador == 1) {
            tokens = linha.split(' - ')
            data = tokens[0]
            titulo = tokens[1]
            imagem = titulo.substring(titulo.indexOf('{') + 1, titulo.indexOf('}'))
            titulo = titulo.substring(0, titulo.indexOf('{'))
        }
        else if(contador == 2)
            relatoBianca = linha
        else if(contador == 3) {
            relatoIsrael = linha
            contador = 0
            $('#timeline').append(gerarHtmlDoRelato(data, titulo, relatoBianca, relatoIsrael, imagem))
        }
    }
}

function gerarHtmlDoRelato(data, titulo, bianca, israel, imagem){
    let relato = `
    <div style="margin-top: 20px;">
        <div>
            <h5>
                <div style="background-color: #fff; border-radius: 10px; padding: 10px; width: 300px; margin: auto">
                    <strong>${data}</strong><br>${titulo}
                </div>
            </h5>
        </div>
        <div>
            <div style="float: left; width: 100px">
                <img src="img/bianca_avatar.png" class="avatar-frame">
            </div>
            <p class="chat-bubble left" style="margin-left: 130px">
                ${bianca}
            </p>
        </div>
        <div>
            <div style="float: right; width: 100px">
                <img src="img/israel_avatar.png" class="avatar-frame">
            </div>
            <p class="chat-bubble right" style="margin-right: 130px">
                ${israel}
            </p>
         </div>
         <div>
             <img src="img/${imagem}" class="imagem">
         </div>
    </div>
    `;
    return relato;
}
