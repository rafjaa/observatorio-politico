Lula = [{
        key: "Candidato",
        values: [
            {"label" : "Agência Brasil" , "value" : -0.2249},
            {"label" : "G1" ,"value" : -0.0794},
            {"label" : "No Minuto" , "value" : 0.0172},
            {"label" : "O Tempo" , "value" : -0.1188},
            {"label" : "Politica Livre" , "value" : -0.1283}
        ]
    }
];

Haddad = [
    {
        key: "Candidato",
        values: [
            {"label" : "Agência Brasil" , "value" : 0.2204},
            {"label" : "G1" ,"value" : 0.3987},
            {"label" : "No Minuto" , "value" : -0.2246},
            {"label" : "O Tempo" , "value" : -0.1031},
            {"label" : "Politica Livre" , "value" : -0.1657}
        ]
    }
];

Ciro = [{
        key: "Candidato",
        values: [
            {"label" : "Agência Brasil" , "value" : -0.0236},
            {"label" : "G1" ,"value" : -0.4435},
            {"label" : "No Minuto" , "value" : 	0.3678},
            {"label" : "O Tempo" , "value" : 0.0161},
            {"label" : "Politica Livre" , "value" : -0.0864}
        ]
    }
];

Marina = [{
        key: "Candidato",
        values: [
            {"label" : "Agência Brasil" , "value" : -0.5383},
            {"label" : "G1" ,"value" : -0.2772},
            {"label" : "No Minuto" , "value" : -0.0347},
            {"label" : "O Tempo" , "value" : -0.245},
            {"label" : "Politica Livre" , "value" : -0.0355}
        ]
    }
];

Joaquim = [{
        key: "Candidato",
        values: [
            {"label" : "Agência Brasil" , "value" : -0.4323},
            {"label" : "G1" ,"value" : 0.2004},
            {"label" : "No Minuto" , "value" : -0.2407},
            {"label" : "O Tempo" , "value" : 0.1022},
            {"label" : "Politica Livre" , "value" : -0.1716}
        ]
    }
];

Doria = [{
        key: "Candidato",
        values: [
            {"label" : "Agência Brasil" , "value" : 0.166},
            {"label" : "G1" ,"value" : 0.0217},
            {"label" : "No Minuto" , "value" : 0.3713},
            {"label" : "O Tempo" , "value" : 0.0039},
            {"label" : "Politica Livre" , "value" : -0.1865}
        ]
    }
];

Bolsonaro = [{
        key: "Candidato",
        values: [
            {"label" : "Agência Brasil" , "value" : -0.6623},
            {"label" : "G1" ,"value" : -0.5398},
            {"label" : "No Minuto" , "value" : -0.1539},
            {"label" : "O Tempo" , "value" : -0.297},
            {"label" : "Politica Livre" , "value" : -0.3066}
        ]
    }
];

var testdata = [
    {key: "Lula", y: 3320},
    {key: "Haddad", y: 84},
    {key: "Ciro Gomes", y: 86},
    {key: "Marina", y: 189},
    {key: "Joquim Barbosa", y: 173},
    {key: "Doria", y: 446},
    {key: "Bolsonaro", y: 239}
];

Media = [{
        key: "Média Geral",
        values: [
            {"label" : "Lula" , "value" : -0.1199},
            {"label" : "Haddad" ,"value" : -0.0362},
            {"label" : "Ciro Gomes" , "value" : -0.0206},
            {"label" : "Marina" , "value" : -0.1152},
            {"label" : "Joaquim Barbosa" , "value" : -0.1528},
            {"label" : "Doria" , "value" : -0.0437},
            {"label" : "Bolsonaro" , "value" : -0.4032}
        ]
    }
];

nv.addGraph(function() {
    var chart = nv.models.discreteBarChart()
        .x(function(d) { return d.label })
        .y(function(d) { return d.value })
        .staggerLabels(true)
        //.staggerLabels(historicalBarChart[0].values.length > 8)
        .showValues(true)
        .duration(250)
        ;

    d3.select('.chart1 svg')
        .datum(Lula)
        .call(chart);
    nv.utils.windowResize(chart.update);
    return chart;
});

///////////////////////////////////////////

nv.addGraph(function() {
    var chart = nv.models.discreteBarChart()
        .x(function(d) { return d.label })
        .y(function(d) { return d.value })
        .staggerLabels(true)
        //.staggerLabels(historicalBarChart[0].values.length > 8)
        .showValues(true)
        .duration(250)
        ;
    d3.select('.chart2 svg')
        .datum(Haddad)
        .call(chart);
    nv.utils.windowResize(chart.update);
    return chart;
});

////////////////////////////////////////

nv.addGraph(function() {
    var chart = nv.models.discreteBarChart()
        .x(function(d) { return d.label })
        .y(function(d) { return d.value })
        .staggerLabels(true)
        //.staggerLabels(historicalBarChart[0].values.length > 8)
        .showValues(true)
        .duration(250)
        ;
    d3.select('.chart3 svg')
        .datum(Ciro)
        .call(chart);
    nv.utils.windowResize(chart.update);
    return chart;
});

///////////////////////////////////////////

nv.addGraph(function() {
    var chart = nv.models.discreteBarChart()
        .x(function(d) { return d.label })
        .y(function(d) { return d.value })
        .staggerLabels(true)
        //.staggerLabels(historicalBarChart[0].values.length > 8)
        .showValues(true)
        .duration(250)
        ;
    d3.select('.chart4 svg')
        .datum(Marina)
        .call(chart);
    nv.utils.windowResize(chart.update);
    return chart;
});

///////////////////////////////////////////

nv.addGraph(function() {
    var chart = nv.models.discreteBarChart()
        .x(function(d) { return d.label })
        .y(function(d) { return d.value })
        .staggerLabels(true)
        //.staggerLabels(historicalBarChart[0].values.length > 8)
        .showValues(true)
        .duration(250)
        ;
    d3.select('.chart5 svg')
        .datum(Joaquim)
        .call(chart);
    nv.utils.windowResize(chart.update);
    return chart;
});

///////////////////////////////////////////

nv.addGraph(function() {
    var chart = nv.models.discreteBarChart()
        .x(function(d) { return d.label })
        .y(function(d) { return d.value })
        .staggerLabels(true)
        //.staggerLabels(historicalBarChart[0].values.length > 8)
        .showValues(true)
        .duration(250)
        ;
    d3.select('.chart6 svg')
        .datum(Doria)
        .call(chart);
    nv.utils.windowResize(chart.update);
    return chart;
});

///////////////////////////////////////////

nv.addGraph(function() {
    var chart = nv.models.discreteBarChart()
        .x(function(d) { return d.label })
        .y(function(d) { return d.value })
        .staggerLabels(true)
        //.staggerLabels(historicalBarChart[0].values.length > 8)
        .showValues(true)
        .duration(250)
        ;
    d3.select('.chart7 svg')
        .datum(Bolsonaro)
        .call(chart);
    nv.utils.windowResize(chart.update);
    return chart;
});

///////////////////////////////////////////

nv.addGraph(function() {
    var chart = nv.models.pieChart()
        .x(function(d) { return d.key })
        .y(function(d) { return d.y })
        .donut(true)
        .padAngle(.08)
        .cornerRadius(5)
        .id('donut1');
    chart.pie.donutLabelsOutside(true).donut(true);
    d3.select('.chart8 svg')
        .datum(testdata)
        .transition().duration(1200)
        .call(chart);
    nv.utils.windowResize(chart.update);
    return chart;
});

///////////////////////////////////////////

nv.addGraph(function() {
    var chart = nv.models.discreteBarChart()
        .x(function(d) { return d.label })
        .y(function(d) { return d.value })
        .staggerLabels(true)
        //.staggerLabels(historicalBarChart[0].values.length > 8)
        .showValues(true)
        .duration(250)
        ;
    d3.select('.chart9 svg')
        .datum(Media)
        .call(chart);
    nv.utils.windowResize(chart.update);
    return chart;
});
