const express = require('express');
const app = express();
const port = 8050;

app.use(express.json());

app.get('/', (req, res) => {
  res.send('<h1>Root NodeJS route</h1>');
});

app.get('/hello', (req, res) => {
  res.send('<h1>Hello World</h1>');
});

app.get('/time', (req, res) => {
  const timezone = req.query.timezone || 'UTC';
  const date = new Date().toLocaleString('en-US', { timeZone: timezone });
  res.send(`<h1>Current time in ${timezone}: ${date}</h1>`);
});

app.get('/color', (req, res) => {
  const color = req.query.color || 'blue';
  res.send(`<h1 style="color:${color}">This text is ${color}</h1>`);
});

app.get('/animal', (req, res) => {
  const animal = req.query.animal || 'dog';
  res.send(`<h1>Your favorite animal is: ${animal}</h1>`);
});

app.get('/sport', (req, res) => {
  const sport = req.query.sport || 'soccer';
  res.send(`Favorite sport: ${sport}`);
});

app.get('/school', (req, res) => {
  const school = req.query.name || 'MIT';
  res.send(`School name is: ${school}`);
});

app.get('/car', (req, res) => {
  const make = req.query.make || 'Tesla';
  res.send(`Car make: ${make}`);
});

app.get('/header', (req, res) => {
  const apiKey = req.header('x-api-key');
  if (apiKey === 'secret123') {
    res.send('Header API key accepted');
  } else {
    res.status(403).send('Forbidden: Invalid API key');
  }
});

app.post('/body', (req, res) => {
  const message = req.body.message;
  if (!message) {
    return res.status(400).send('Please send a JSON body with a "message" field');
  }
  res.send(`You sent: ${message}`);
});

app.listen(port, () => {
  console.log(`Server running on http://localhost:${port}`);
});