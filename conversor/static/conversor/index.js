
let dados = null

$("#submit").on("click", (event) => {
    let dt_inicio = $("#dataInicio").val()
    let dt_fim = $("#dataFim").val()
    
    axios.post(
        '/consulta',
        {
            "dt_inicio":dt_inicio,
            "dt_fim": dt_fim
        }
    )
    .then((response) =>{
        dados = response.data
        console.log(dados)
    })
    .catch((err)=>{
        console.log(err)
    })
})