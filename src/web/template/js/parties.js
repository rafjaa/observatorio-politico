AgenciaBrasil = [
    {
        key: 'Notícias',
        "color": "#2CA02C",
        values: [
            {"label":"PT","value":933},
            {"label":"PSDB","value":644},
            {"label":"PMDB","value":877},
            {"label":"PP","value":191},
            {"label":"PDT","value":144},
            {"label":"DEM","value":225},
            {"label":"PSB","value":177}
        ]
    },
    {
        key: 'Polaridade',
        "color": "#D62728",
        values: [
            {"label":"PT","value":-0.2684},
            {"label":"PSDB","value":-0.1881},
            {"label":"PMDB","value":-0.218},
            {"label":"PP","value":-0.0984},
            {"label":"PDT","value":-0.1705},
            {"label":"DEM","value":-0.2944},
            {"label":"PSB","value":-0.1088}
        ]
    }
];

Globo = [
    {
        key: 'Notícias',
        "color":"#1F77B4",
        values: [
            {"label":"PT","value":729},
            {"label":"PSDB","value":879},
            {"label":"PMDB","value":1040},
            {"label":"PP","value":195},
            {"label":"PDT","value":101},
            {"label":"DEM","value":209},
            {"label":"PSB","value":161}
        ]
    },
    {
        key: 'Polaridade',
        "color":"#D62728",
        values: [
            {"label":"PT","value":-0.0253},
            {"label":"PSDB","value":-0.0821},
            {"label":"PMDB","value":-0.0625},
            {"label":"PP","value":0.0972},
            {"label":"PDT","value":0.0357},
            {"label":"DEM","value":0.0503},
            {"label":"PSB","value":-0.0928}
        ]
    }
];

NoMinuto = [
    {
        key: 'Notícias',
        "color": "#FF7F0E",
        values: [
            {"label":"PT","value":1250},
            {"label":"PSDB","value":620},
            {"label":"PMDB","value":971},
            {"label":"PP","value":204},
            {"label":"PDT","value":477},
            {"label":"DEM","value":853},
            {"label":"PSB","value":737}
        ]
    },
    {
        key: 'Polaridade',
        "color":"#D62728",
        values: [
            {"label":"PT","value":-0.0381},
            {"label":"PSDB","value":-0.0408},
            {"label":"PMDB","value":-0.0288},
            {"label":"PP","value":-0.0987},
            {"label":"PDT","value":0.1208},
            {"label":"DEM","value":0.0937},
            {"label":"PSB","value":0.1038}
        ]
    }
];

OTempo = [
    {
        key: 'Notícias',
        "color": "#AEC7E8",
        values: [
            {"label":"PT","value":969},
            {"label":"PSDB","value":995},
            {"label":"PMDB","value":1225},
            {"label":"PP","value":205},
            {"label":"PDT","value":99},
            {"label":"DEM","value":200},
            {"label":"PSB","value":195}
        ]
    },
    {
        key: 'Polaridade',
        "color":"#D62728",
        values: [
            {"label":"PT","value":-0.0623},
            {"label":"PSDB","value":-0.1342},
            {"label":"PMDB","value":-0.0643},
            {"label":"PP","value":-0.0981},
            {"label":"PDT","value":0.0055},
            {"label":"DEM","value":-0.2304},
            {"label":"PSB","value":-0.1318}
        ]
    }
];

PoliticaLivre = [
    {
        key: 'Notícias',
        "color": "#FF9896",
        values: [
            {"label":"PT","value":484},
            {"label":"PSDB","value":618},
            {"label":"PMDB","value":784},
            {"label":"PP","value":111},
            {"label":"PDT","value":46},
            {"label":"DEM","value":142},
            {"label":"PSB","value":101}
        ]
    },
    {
        key: 'Polaridade',
        "color":"#D62728",
        values: [
            {"label":"PT","value":-0.1914},
            {"label":"PSDB","value":-0.2533},
            {"label":"PMDB","value":-0.1376},
            {"label":"PP","value":-0.1264},
            {"label":"PDT","value":0.0355},
            {"label":"DEM","value":-0.1957},
            {"label":"PSB","value":-0.2791}
        ]
    }
];


var partidos = [
    {key: "PT", y: 4365},
    {key: "PSDB", y: 2682},
    {key: "PMDB", y: 3243},
    {key: "PP", y: 510},
    {key: "PDT", y: 464},
    {key: "DEM", y: 948},
    {key: "PSB", y: 951}
];

nv.addGraph(function() {
    var chart = nv.models.pieChart()
        .x(function(d) { return d.key })
        .y(function(d) { return d.y })
        .donut(true)
        .padAngle(.08)
        .cornerRadius(5)
        .id('donut1');
    chart.pie.donutLabelsOutside(true).donut(true);
    d3.select('.chart6 svg')
        .datum(partidos)
        .transition().duration(1200)
        .call(chart);
    nv.utils.windowResize(chart.update);
    return chart;
});


nv.addGraph(function() {
    var chart = nv.models.multiBarHorizontalChart()
        .x(function(d) { return d.label })
        .y(function(d) { return d.value })
        .showControls(false)
        .duration(250)
        .stacked(true);
    chart.yAxis.tickFormat(d3.format(',.2f'));
    d3.select('.chart1 svg')
        .datum(AgenciaBrasil)
        .call(chart);
    nv.utils.windowResize(chart.update);
    return chart;
});

nv.addGraph(function() {
    var chart = nv.models.multiBarHorizontalChart()
        .x(function(d) { return d.label })
        .y(function(d) { return d.value })
        .showControls(false)
        .duration(250)
        .stacked(true);
    chart.yAxis.tickFormat(d3.format(',.2f'));
    d3.select('.chart2 svg')
        .datum(Globo)
        .call(chart);
    nv.utils.windowResize(chart.update);
    return chart;
});

nv.addGraph(function() {
    var chart = nv.models.multiBarHorizontalChart()
        .x(function(d) { return d.label })
        .y(function(d) { return d.value })
        .showControls(false)
        .duration(250)
        .stacked(true);
    chart.yAxis.tickFormat(d3.format(',.2f'));
    d3.select('.chart3 svg')
        .datum(NoMinuto)
        .call(chart);
    nv.utils.windowResize(chart.update);
    return chart;
});

nv.addGraph(function() {
    var chart = nv.models.multiBarHorizontalChart()
        .x(function(d) { return d.label })
        .y(function(d) { return d.value })
        .showControls(false)
        .duration(250)
        .stacked(true);
    chart.yAxis.tickFormat(d3.format(',.2f'));
    d3.select('.chart4 svg')
        .datum(OTempo)
        .call(chart);
    nv.utils.windowResize(chart.update);
    return chart;
});

nv.addGraph(function() {
    var chart = nv.models.multiBarHorizontalChart()
        .x(function(d) { return d.label })
        .y(function(d) { return d.value })
        .showControls(false)
        .duration(250)
        .stacked(true);
    chart.yAxis.tickFormat(d3.format(',.2f'));
    d3.select('.chart5 svg')
        .datum(PoliticaLivre)
        .call(chart);
    nv.utils.windowResize(chart.update);
    return chart;
});
