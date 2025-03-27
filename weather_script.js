const apiKey = 'edbb179dec6ea980536ff3bc1c8b9bda';
const city = 'London'; // Cambia esto a la ciudad que desees

async function getWeather(city) {
    const url = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric`;

    try {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error('Error al recuperar los datos del clima');
        }
        const data = await response.json();
        console.log(`El clima en ${city} es:`);
        console.log(`Temperatura: ${data.main.temp}C`);
        console.log(`Humedad: ${data.main.humidity}%`);
        console.log(`Descripción: ${data.weather[0].description}`);
    } catch (error) {
        console.error('Error:', error);
    }
}

getWeather(city);