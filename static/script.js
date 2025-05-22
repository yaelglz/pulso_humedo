async function cargarDatos() {
    try {
        const respuesta = await fetch("/historial/");
        const datos = await respuesta.json();

        console.log(datos);

        const historialSensor1 = [];
        const historialSensor2 = [];
        const historialSensor3 = [];

        const humedad1 = [];
        const humedad2 = [];
        const humedad3 = [];
        const fechas = [];

        datos.forEach(dato => {
            historialSensor1.push(`<li><strong>💧 Sensor 1:</strong> ${dato.humedad1}% - <strong>Fecha:</strong> ${new Date(dato.fecha).toLocaleString()}</li>`);
            historialSensor2.push(`<li><strong>💧 Sensor 2:</strong> ${dato.humedad2}% - <strong>Fecha:</strong> ${new Date(dato.fecha).toLocaleString()}</li>`);
            historialSensor3.push(`<li><strong>💧 Sensor 3:</strong> ${dato.humedad3}% - <strong>Fecha:</strong> ${new Date(dato.fecha).toLocaleString()}</li>`);

            humedad1.push(dato.humedad1);
            humedad2.push(dato.humedad2);
            humedad3.push(dato.humedad3);
            fechas.push(new Date(dato.fecha).toLocaleString());
        });

        document.getElementById("historialSensor1").innerHTML = `<ul>${historialSensor1.join('')}</ul>`;
        document.getElementById("historialSensor2").innerHTML = `<ul>${historialSensor2.join('')}</ul>`;
        document.getElementById("historialSensor3").innerHTML = `<ul>${historialSensor3.join('')}</ul>`;

        const ultimos = fechas.slice(0, 10);
        const humedad1_ultimos = humedad1.slice(0, 10);
        const humedad2_ultimos = humedad2.slice(0, 10);
        const humedad3_ultimos = humedad3.slice(0, 10);

        actualizarGraficaHumedad("graficaSensor1", humedad1_ultimos, ultimos);
        actualizarGraficaHumedad("graficaSensor2", humedad2_ultimos, ultimos);
        actualizarGraficaHumedad("graficaSensor3", humedad3_ultimos, ultimos);

    } catch (error) {
        console.error("Error al cargar los datos: ", error);
    }
}

function actualizarGraficaHumedad(idGrafica, humedades, fechas) {
    const layout = {
        title: 'Humedad',
        xaxis: { title: 'Fecha' },
        yaxis: { title: 'Humedad (%)' },
        margin: { t: 40, b: 40, l: 50, r: 20 },
        paper_bgcolor: 'rgba(255, 255, 255, 0.7)',
        plot_bgcolor: 'rgba(255, 255, 255, 0.7)',
        font: { color: '#333' }
    };

    const trace = {
        x: fechas,
        y: humedades,
        type: 'scatter',
        mode: 'lines+markers',
        line: { color: '#4CAF50' },
        marker: { size: 8 }
    };

    Plotly.newPlot(idGrafica, [trace], layout, { displayModeBar: false });
}

setInterval(cargarDatos, 10000);
cargarDatos();
