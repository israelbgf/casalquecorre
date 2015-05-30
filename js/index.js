$(function(){
    $.ajax({
        type:'GET',
        url: 'relatos/relatos.html',
        success:parseArquivoDeRelatos
    })
})

function parseArquivoDeRelatos(arquivo){
    var tokens, data, titulo, relatoBianca, relatoIsrael;
    var contador = 0

    for(let linha of arquivo.split('\n')){
        if(linha.startsWith('-') || linha.trim() == '')
            continue;
        contador++
        if(contador == 1) {
            tokens = linha.split(' - ')
            data = tokens[0]
            titulo = tokens[1]
        }
        else if(contador == 2)
            relatoBianca = linha
        else if(contador == 3) {
            relatoIsrael = linha
            contador = 0
            $('#timeline').append(gerarHtmlDoRelato(data, titulo, relatoBianca, relatoIsrael))
        }
    }
}

function gerarHtmlDoRelato(data, titulo, bianca, israel){
    let relato = `
    <div style="margin-top: 50px">
        <div class="row" style="margin-bottom: 15px">
            <h5>
                <div style="background-color: #fff; border-radius: 10px; padding: 10px; width: 300px; margin: auto">
                    <strong>${data}</strong><br>${titulo}
                </div>
            </h5>
        </div>
        <div class="row">
            <img style="float: left; margin-top: 30px" src="img/bianca_avatar.png" class="avatar-frame">
            <blockquote style="float: left; width: 80%; margin: 0; margin-left: 30px" class="balao-bianca">
                ${bianca}
            </blockquote>
        </div>
        <div class="row" style="margin-top: 30px">
            <img style="border-radius: 10px;" class="borda" src="img/corrida.png" width="280">
            <img style="float: right; margin-top: 20px; margin-left: 30px" src="img/israel_avatar.png" class="avatar-frame">
            <blockquote style="float: right; width: 50%; margin: 0; margin-left: 30px" class="balao-israel">
                ${israel}
            </blockquote>
        </div>
    </div>
    `;
    return relato;
}
