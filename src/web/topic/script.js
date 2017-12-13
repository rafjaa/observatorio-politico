var span_n_topicos = document.querySelector('#span_n_topicos');
var main = document.querySelector('main');
var range = document.querySelector('#range');
var faixa_topicos = {"5": [[["reforma", 2.02], ["proposta", 1.87], ["projeto", 1.81], ["senado", 1.63], ["c\u00e2mara", 1.61]], [["lula", 2.93], ["ex-presidente", 2.9], ["odebrecht", 1.76], ["moro", 1.7], ["lava", 1.53]], [["temer", 4.8], ["presidente", 2.9], ["den\u00fancia", 2.82], ["c\u00e2mara", 1.83], ["michel", 1.7]], [["dilma", 1.44], ["eleitoral", 1.35], ["governo", 1.23], ["partido", 1.2], ["rio", 1.1]], [["stf", 2.37], ["ministro", 2.17], ["supremo", 1.95], ["a\u00e9cio", 1.84], ["fachin", 1.55]]], "7": [[["reforma", 2.12], ["proposta", 1.69], ["governo", 1.66], ["projeto", 1.64], ["previd\u00eancia", 1.36]], [["ex-presidente", 1.93], ["odebrecht", 1.77], ["federal", 1.74], ["lava", 1.55], ["jato", 1.54]], [["c\u00e2mara", 2.46], ["deputados", 2.08], ["comiss\u00e3o", 1.92], ["vota\u00e7\u00e3o", 1.83], ["cunha", 1.8]], [["temer", 5.53], ["presidente", 2.9], ["den\u00fancia", 1.97], ["michel", 1.96], ["governo", 1.57]], [["stf", 2.47], ["ministro", 2.26], ["a\u00e9cio", 2.17], ["supremo", 1.94], ["senador", 1.72]], [["lula", 5.4], ["ex-presidente", 2.21], ["moro", 1.68], ["presidente", 1.61], ["dilma", 1.21]], [["eleitoral", 1.68], ["partido", 1.47], ["prefeito", 1.31], ["candidato", 1.3], ["natal", 1.26]]], "14": [[["projeto", 1.59], ["lei", 1.29], ["governo", 1.26], ["bilh\u00f5es", 1.11], ["estados", 1.04]], [["janot", 2.84], ["joesley", 2.34], ["procurador", 2.13], ["jbs", 1.84], ["geral", 1.7]], [["c\u00e2mara", 2.62], ["deputados", 2.3], ["vota\u00e7\u00e3o", 2.04], ["den\u00fancia", 2.03], ["comiss\u00e3o", 1.94]], [["temer", 5.7], ["presidente", 3.03], ["michel", 2.0], ["governo", 1.93], ["planalto", 1.52]], [["ministro", 2.91], ["stf", 2.69], ["supremo", 2.07], ["tribunal", 1.56], ["decis\u00e3o", 1.49]], [["lula", 5.49], ["ex-presidente", 2.06], ["moro", 1.65], ["presidente", 1.43], ["in\u00e1cio", 1.08]], [["natal", 1.75], ["prefeito", 1.49], ["partido", 1.32], ["candidato", 1.24], ["psb", 1.08]], [["a\u00e9cio", 4.36], ["senador", 3.38], ["psdb", 2.26], ["neves", 2.14], ["senado", 1.48]], [["eleitoral", 3.71], ["tse", 2.74], ["elei\u00e7\u00f5es", 1.43], ["campanha", 1.18], ["candidatos", 1.12]], [["odebrecht", 4.14], ["ex-presidente", 1.11], ["milh\u00f5es", 1.08], ["empresa", 1.05], ["campanha", 0.91]], [["dilma", 3.74], ["impeachment", 3.01], ["presidenta", 2.43], ["rousseff", 1.72], ["processo", 1.51]], [["federal", 1.8], ["ex-presidente", 1.71], ["pris\u00e3o", 1.7], ["opera\u00e7\u00e3o", 1.52], ["cunha", 1.5]], [["reforma", 4.13], ["previd\u00eancia", 2.83], ["proposta", 1.27], ["maia", 1.15], ["aposentadoria", 0.97]], [["veja", 3.25], ["coment\u00e1rio", 3.23], ["jornal", 2.9], ["dez", 2.54], ["reportagem", 1.22]]], "9": [[["reforma", 2.13], ["proposta", 1.68], ["projeto", 1.64], ["governo", 1.61], ["previd\u00eancia", 1.36]], [["ex-presidente", 1.9], ["odebrecht", 1.85], ["federal", 1.61], ["opera\u00e7\u00e3o", 1.48], ["lava", 1.47]], [["c\u00e2mara", 2.72], ["deputados", 2.3], ["comiss\u00e3o", 1.91], ["vota\u00e7\u00e3o", 1.89], ["deputado", 1.84]], [["temer", 5.56], ["presidente", 2.87], ["michel", 1.97], ["den\u00fancia", 1.69], ["governo", 1.55]], [["dilma", 4.06], ["impeachment", 2.59], ["presidenta", 2.28], ["rousseff", 1.81], ["processo", 1.42]], [["lula", 5.4], ["ex-presidente", 2.19], ["moro", 1.83], ["presidente", 1.46], ["in\u00e1cio", 1.06]], [["eleitoral", 1.45], ["natal", 1.45], ["prefeito", 1.39], ["candidato", 1.32], ["partido", 1.21]], [["a\u00e9cio", 4.29], ["senador", 3.39], ["psdb", 2.28], ["neves", 2.11], ["senado", 1.6]], [["stf", 2.63], ["ministro", 2.62], ["supremo", 2.08], ["tribunal", 1.8], ["fachin", 1.48]]], "15": [[["projeto", 2.32], ["senado", 1.77], ["proposta", 1.76], ["texto", 1.73], ["pec", 1.34]], [["ministro", 2.8], ["stf", 2.65], ["supremo", 2.06], ["decis\u00e3o", 1.61], ["tribunal", 1.6]], [["den\u00fancia", 4.08], ["ccj", 2.09], ["contra", 1.53], ["deputados", 1.37], ["parecer", 1.37]], [["temer", 5.29], ["presidente", 2.8], ["governo", 2.14], ["michel", 1.91], ["planalto", 1.52]], [["dilma", 3.68], ["impeachment", 3.03], ["presidenta", 2.47], ["rousseff", 1.7], ["processo", 1.43]], [["lula", 5.55], ["ex-presidente", 2.15], ["moro", 1.68], ["presidente", 1.43], ["in\u00e1cio", 1.09]], [["natal", 1.53], ["rio", 1.39], ["estado", 1.3], ["prefeito", 1.26], ["grande", 1.09]], [["a\u00e9cio", 4.46], ["senador", 3.18], ["psdb", 2.43], ["neves", 2.19], ["senado", 1.09]], [["eleitoral", 3.6], ["tse", 2.84], ["campanha", 1.54], ["elei\u00e7\u00f5es", 1.31], ["chapa", 1.25]], [["janot", 2.63], ["joesley", 2.49], ["procurador", 1.98], ["jbs", 1.93], ["batista", 1.69]], [["maia", 3.43], ["c\u00e2mara", 2.34], ["deputado", 1.95], ["partido", 1.84], ["dem", 1.61]], [["odebrecht", 2.06], ["ex-presidente", 1.83], ["lava", 1.58], ["jato", 1.56], ["opera\u00e7\u00e3o", 1.51]], [["reforma", 4.03], ["previd\u00eancia", 2.95], ["governo", 1.07], ["anos", 1.04], ["idade", 1.03]], [["veja", 3.25], ["coment\u00e1rio", 3.24], ["jornal", 2.9], ["dez", 2.54], ["reportagem", 1.22]], [["cunha", 5.38], ["eduardo", 2.07], ["conselho", 1.18], ["deputado", 1.15], ["funaro", 1.09]]], "13": [[["projeto", 1.65], ["lei", 1.32], ["governo", 1.24], ["bilh\u00f5es", 1.11], ["estados", 1.04]], [["janot", 2.84], ["joesley", 2.35], ["procurador", 2.12], ["jbs", 1.84], ["geral", 1.7]], [["c\u00e2mara", 2.63], ["deputados", 2.31], ["den\u00fancia", 2.09], ["vota\u00e7\u00e3o", 2.02], ["comiss\u00e3o", 1.92]], [["temer", 5.68], ["presidente", 3.02], ["michel", 1.99], ["governo", 1.94], ["planalto", 1.52]], [["ministro", 2.91], ["stf", 2.69], ["supremo", 2.07], ["tribunal", 1.56], ["decis\u00e3o", 1.49]], [["lula", 5.49], ["ex-presidente", 2.06], ["moro", 1.65], ["presidente", 1.43], ["in\u00e1cio", 1.08]], [["natal", 1.75], ["prefeito", 1.49], ["partido", 1.3], ["candidato", 1.23], ["psb", 1.07]], [["a\u00e9cio", 4.35], ["senador", 3.38], ["psdb", 2.26], ["neves", 2.14], ["senado", 1.49]], [["eleitoral", 3.71], ["tse", 2.74], ["elei\u00e7\u00f5es", 1.43], ["campanha", 1.19], ["candidatos", 1.12]], [["odebrecht", 4.14], ["ex-presidente", 1.11], ["milh\u00f5es", 1.08], ["empresa", 1.05], ["campanha", 0.91]], [["dilma", 3.73], ["impeachment", 3.01], ["presidenta", 2.43], ["rousseff", 1.71], ["processo", 1.5]], [["federal", 1.8], ["ex-presidente", 1.7], ["pris\u00e3o", 1.7], ["opera\u00e7\u00e3o", 1.52], ["cunha", 1.48]], [["reforma", 4.13], ["previd\u00eancia", 2.83], ["proposta", 1.26], ["maia", 1.16], ["aposentadoria", 0.97]]], "2": [[["temer", 2.33], ["presidente", 2.19], ["governo", 2.02], ["c\u00e2mara", 2.02], ["deputados", 1.51]], [["ex-presidente", 2.55], ["federal", 1.98], ["lula", 1.86], ["lava", 1.65], ["jato", 1.64]]], "11": [[["c\u00e2mara", 2.08], ["vota\u00e7\u00e3o", 1.97], ["comiss\u00e3o", 1.94], ["deputados", 1.77], ["proposta", 1.69]], [["ex-presidente", 1.86], ["odebrecht", 1.83], ["federal", 1.55], ["lava", 1.53], ["jato", 1.53]], [["temer", 5.05], ["den\u00fancia", 2.96], ["presidente", 2.75], ["michel", 1.76], ["contra", 1.24]], [["governo", 2.21], ["reforma", 1.34], ["previd\u00eancia", 1.17], ["brasil", 1.1], ["bilh\u00f5es", 1.03]], [["stf", 2.72], ["ministro", 2.65], ["supremo", 2.15], ["tribunal", 1.63], ["fachin", 1.5]], [["lula", 5.41], ["ex-presidente", 2.2], ["moro", 1.84], ["presidente", 1.44], ["in\u00e1cio", 1.06]], [["natal", 1.76], ["prefeito", 1.47], ["partido", 1.34], ["candidato", 1.23], ["psb", 1.12]], [["a\u00e9cio", 4.39], ["senador", 3.15], ["psdb", 2.4], ["neves", 2.16], ["senado", 1.11]], [["eleitoral", 3.49], ["tse", 2.8], ["campanha", 1.46], ["elei\u00e7\u00f5es", 1.28], ["chapa", 1.22]], [["dilma", 3.8], ["impeachment", 3.04], ["presidenta", 2.47], ["rousseff", 1.75], ["processo", 1.42]], [["cunha", 5.3], ["eduardo", 1.97], ["deputado", 1.37], ["conselho", 1.22], ["c\u00e2mara", 1.09]]], "4": [[["reforma", 2.04], ["proposta", 1.83], ["projeto", 1.78], ["senado", 1.67], ["c\u00e2mara", 1.61]], [["ex-presidente", 2.57], ["lula", 1.99], ["federal", 1.97], ["lava", 1.8], ["jato", 1.79]], [["temer", 4.32], ["den\u00fancia", 2.76], ["presidente", 2.72], ["c\u00e2mara", 1.63], ["michel", 1.56]], [["dilma", 1.55], ["eleitoral", 1.33], ["governo", 1.3], ["partido", 1.27], ["prefeito", 1.04]]], "3": [[["governo", 1.7], ["reforma", 1.44], ["projeto", 1.33], ["proposta", 1.28], ["c\u00e2mara", 1.05]], [["ex-presidente", 2.72], ["lula", 2.17], ["federal", 1.93], ["lava", 1.74], ["jato", 1.73]], [["temer", 4.01], ["presidente", 2.73], ["den\u00fancia", 2.58], ["c\u00e2mara", 1.83], ["michel", 1.46]]], "10": [[["c\u00e2mara", 1.89], ["proposta", 1.88], ["projeto", 1.82], ["vota\u00e7\u00e3o", 1.77], ["comiss\u00e3o", 1.73]], [["ex-presidente", 1.95], ["odebrecht", 1.67], ["federal", 1.64], ["lava", 1.52], ["jato", 1.51]], [["temer", 4.83], ["den\u00fancia", 3.14], ["presidente", 2.69], ["michel", 1.69], ["c\u00e2mara", 1.41]], [["governo", 2.29], ["brasil", 1.25], ["pa\u00eds", 1.04], ["reforma", 1.01], ["bilh\u00f5es", 0.97]], [["stf", 2.73], ["ministro", 2.65], ["supremo", 2.15], ["tribunal", 1.63], ["fachin", 1.52]], [["lula", 5.44], ["ex-presidente", 2.2], ["moro", 1.77], ["presidente", 1.49], ["in\u00e1cio", 1.08]], [["natal", 1.79], ["prefeito", 1.46], ["partido", 1.36], ["candidato", 1.26], ["psb", 1.15]], [["a\u00e9cio", 4.35], ["senador", 3.17], ["psdb", 2.43], ["neves", 2.14], ["senado", 1.16]], [["eleitoral", 3.34], ["tse", 2.8], ["campanha", 1.55], ["chapa", 1.29], ["dilma", 1.26]], [["impeachment", 2.98], ["dilma", 2.91], ["cunha", 2.44], ["presidenta", 2.06], ["processo", 1.88]]], "12": [[["proposta", 1.9], ["projeto", 1.89], ["c\u00e2mara", 1.78], ["comiss\u00e3o", 1.75], ["vota\u00e7\u00e3o", 1.74]], [["janot", 2.53], ["joesley", 2.51], ["jbs", 1.95], ["procurador", 1.94], ["batista", 1.71]], [["temer", 4.65], ["den\u00fancia", 3.22], ["presidente", 2.66], ["c\u00e2mara", 1.62], ["michel", 1.59]], [["governo", 2.23], ["brasil", 1.19], ["reforma", 1.12], ["previd\u00eancia", 1.03], ["bilh\u00f5es", 1.02]], [["ministro", 2.74], ["stf", 2.68], ["supremo", 2.09], ["tribunal", 1.62], ["decis\u00e3o", 1.61]], [["lula", 5.58], ["ex-presidente", 2.15], ["moro", 1.66], ["presidente", 1.48], ["in\u00e1cio", 1.1]], [["natal", 1.82], ["prefeito", 1.46], ["partido", 1.28], ["candidato", 1.23], ["psb", 1.13]], [["a\u00e9cio", 4.34], ["senador", 3.19], ["psdb", 2.45], ["neves", 2.13], ["senado", 1.14]], [["eleitoral", 3.47], ["tse", 2.8], ["campanha", 1.5], ["elei\u00e7\u00f5es", 1.26], ["chapa", 1.23]], [["dilma", 3.8], ["impeachment", 3.11], ["presidenta", 2.51], ["rousseff", 1.76], ["processo", 1.47]], [["cunha", 5.26], ["eduardo", 1.95], ["deputado", 1.41], ["conselho", 1.23], ["c\u00e2mara", 1.13]], [["odebrecht", 1.93], ["ex-presidente", 1.89], ["lava", 1.58], ["jato", 1.57], ["opera\u00e7\u00e3o", 1.53]]], "6": [[["reforma", 2.08], ["proposta", 1.87], ["projeto", 1.8], ["texto", 1.59], ["c\u00e2mara", 1.57]], [["ex-presidente", 1.85], ["federal", 1.79], ["odebrecht", 1.71], ["lava", 1.58], ["jato", 1.57]], [["temer", 4.77], ["den\u00fancia", 2.9], ["presidente", 2.85], ["c\u00e2mara", 1.76], ["michel", 1.69]], [["eleitoral", 1.37], ["partido", 1.3], ["dilma", 1.22], ["governo", 1.18], ["prefeito", 1.12]], [["stf", 2.34], ["a\u00e9cio", 2.2], ["ministro", 2.09], ["senador", 1.9], ["supremo", 1.84]], [["lula", 5.42], ["ex-presidente", 2.28], ["moro", 1.81], ["presidente", 1.57], ["in\u00e1cio", 1.09]]], "8": [[["reforma", 2.15], ["proposta", 1.78], ["projeto", 1.72], ["governo", 1.56], ["texto", 1.42]], [["ex-presidente", 1.92], ["odebrecht", 1.79], ["federal", 1.69], ["lava", 1.52], ["jato", 1.52]], [["c\u00e2mara", 2.45], ["deputados", 2.07], ["cunha", 1.9], ["comiss\u00e3o", 1.86], ["vota\u00e7\u00e3o", 1.74]], [["temer", 5.59], ["presidente", 2.9], ["michel", 1.97], ["den\u00fancia", 1.89], ["governo", 1.6]], [["ministro", 2.69], ["stf", 2.54], ["supremo", 2.0], ["tribunal", 1.82], ["julgamento", 1.4]], [["lula", 5.41], ["ex-presidente", 2.22], ["moro", 1.71], ["presidente", 1.59], ["dilma", 1.11]], [["eleitoral", 1.57], ["natal", 1.31], ["prefeito", 1.28], ["candidato", 1.25], ["partido", 1.2]], [["a\u00e9cio", 4.31], ["senador", 3.37], ["psdb", 2.31], ["neves", 2.12], ["senado", 1.54]]]}


$(document).ready(function(){

    var atualiza = function(){
        var n_topicos = range.value;
        span_n_topicos.textContent = n_topicos;
        var topicos = faixa_topicos[n_topicos];

        main.innerHTML = '';

        for(var i=0; i < parseInt(n_topicos); i++){

            main.innerHTML += '\
                <section class="topic">\
                    <p contenteditable="true">Tópico ' + (i + 1) + '</p>\
                    <div>\
                        <canvas id="chart_' + i + '"></canvas>\
                    </div>\
                </section>';            
        }

        for(var i=0; i < parseInt(n_topicos); i++){
            var termos = [];
            var pesos = [];

            for(var j=0; j < 5; j++){
                termos.push(topicos[i][j][0]);
                pesos.push(topicos[i][j][1]);
            }

            var ctx = document.getElementById('chart_' + i).getContext('2d');

            var data = {
                datasets: [{
                    data: pesos,
                    backgroundColor: [
                        'rgba(54, 162, 235, 0.7)',
                        'rgba(75, 192, 192, 0.7)',
                        'rgba(255, 205, 86, 0.7)',
                        'rgba(255, 159, 64, 0.7)',
                        'rgba(255, 99, 132, 0.7)'            
                    ]
                }],

                // These labels appear in the legend and in the tooltips when hovering different arcs
                labels: termos
            };

            new Chart(ctx, {
                data: data,
                type: 'polarArea',
                options: {
                    responsive: true,
                    legend: {
                        position: 'right',
                    }
                }
            });

        }
    }

    range.onchange = function(){
        atualiza();
    };

    // Incia exibindo 6 tópicos
    range.value = 3;
    atualiza();
});