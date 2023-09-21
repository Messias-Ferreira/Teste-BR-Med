function load_data_init() {

    let moeda = $("#moeda").children("option:selected").val()

    axios.get(
        '/consulta',
        {
            params: {
                "moeda": moeda
            }
        }
    )
        .then((response) => {

            let data = response.data

            let categorias = new Array()
            let cotacaoes = new Array()

            data.forEach(element => {
                categorias.push(
                    element.data
                )
                cotacaoes.push(element.cotacao)
            });

            chart.xAxis[0].setCategories(Array.from(categorias))
            chart.addSeries({
                name: moeda,
                data: cotacaoes
            })

        })
        .catch((err) => {
            console.log(err)
        })
}


const chart = Highcharts.chart('container', {

    title: {
        text: "Cotação do USD",
        align: 'left'
    },

    events: {
        load: load_data_init()
    },

    subtitle: {
        text: 'By Vat Comply. Source: <a href="https://www.vatcomply.com/" target="_blank">VAT</a>.',
        align: 'left'
    },

    yAxis: {
        title: {
            text: 'Valor da Moeda'
        }
    },

    xAxis: {
        categories: [],
    },

    legend: {
        layout: 'vertical',
        align: 'right',
        verticalAlign: 'middle'
    },

    series: null,

    responsive: {
        rules: [{
            condition: {
                maxWidth: 1000
            },
            chartOptions: {
                legend: {
                    layout: 'horizontal',
                    align: 'center',
                    verticalAlign: 'bottom'
                }
            }
        }]
    }

});

document.addEventListener('DOMContentLoaded', function () {
    chart
});




$("#submit").on("click", () => {
    let dt_inicio = $("#dataInicio").val()
    let dt_fim = $("#dataFim").val()
    let moeda = $("#moeda").children("option:selected").val()

    data_inicio = new Date(dt_inicio)
    data_fim = new Date(dt_fim)
    if (dt_inicio != "" && dt_fim != "") {
        let diff = Math.abs(data_inicio.getTime() - data_fim.getTime());
        let diffDays = Math.ceil(diff / (1000 * 3600 * 24)); 

        if (diffDays > 5) {
            alert("Escolher período no maximo de 5 dias ")
            return
        }
    }

    if (dt_inicio == "" || dt_fim == ""){
        alert("Preencha os dois campos datas")
    }

    axios.get(
        '/consulta',
        {
            params: {
                "dt_inicio": dt_inicio,
                "dt_fim": dt_fim,
                "moeda": moeda
            }
        }
    )
        .then((response) => {
            chart.series[0].remove()
            chart.xAxis[0].categories = []
            let data = response.data

            let categorias = new Array()
            let cotacaoes = new Array()

            data.forEach(element => {
                categorias.push(
                    element.data
                )
                cotacaoes.push(element.cotacao)
            });

            chart.xAxis[0].setCategories(Array.from(categorias))
            chart.addSeries({
                name: moeda,
                data: cotacaoes
            })
        })
        .catch((err) => {
            console.log(err)
        })

})
