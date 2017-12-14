/*
PMDB
Total: 4974
Lava Jato: 951

PT
Total: 4428
Lava Jato: 834

PSDB
Total: 3832
Lava Jato: 585
 */

LavaJato = [
    
    {
        key: 'Lava Jato',
        values: [
            {"label":"TEMER","value":987,"color":"#1F77B4"},
            {"label":"DILMA","value":546,"color":"#1F77B4"},
            {"label":"LULA","value":1041,"color":"#1F77B4"},
            {"label":"EDUARDO CUNHA","value":406,"color":"#1F77B4"},
            {"label":"AÉCIO NEVES","value":283,"color":"#1F77B4"},
            {"label":"DELCÍCIO DO AMARAL","value":171,"color":"#1F77B4"},
            {"label":"PMDB","value":951,"color":"#FF7F0E"},
            {"label":"PT","value":834,"color":"#FF7F0E"},
            {"label":"PSDB","value":585,"color":"#FF7F0E"}
        ]
    }
];

var SitesLavaJato = [
    {key: "Agência Brasil", y: 1117},
    {key: "G1", y: 1985},
    {key: "No Minuto", y: 168},
    {key: "O Tempo", y: 1782},
    {key: "Política Livre", y: 872}
];

nv.addGraph(function() {
    var chart = nv.models.discreteBarChart()
        .x(function(d) { return d.label })
        .y(function(d) { return d.value })


        .duration(250);
    d3.select('.chart1 svg')
        .datum(LavaJato)
        .call(chart);
    nv.utils.windowResize(chart.update);
    return chart;
});

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
        .datum(SitesLavaJato)
        .transition().duration(1200)
        .call(chart);
    nv.utils.windowResize(chart.update);
    return chart;
});
