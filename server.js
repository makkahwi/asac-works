const express = require('express');
const cors = require('cors');

const server = express();

const port = 5050;

const data = require("./assets/data/data.json");

server.use(cors());

function Movie({ title, poster_path, overview }) {
  this.title = title;
  this.poster_path = poster_path;
  this.overview = overview;
};

server.get('/', (req, res) => res.status(200).send(new Movie(data)));

server.get('/favorite', (req, res) => res.status(200).send("Welcome to Favorite Page"));

server.use((err, req, res, text) =>
  res.status(500).type('text/plain').send({
    "status": 500,
    "responseText": "Sorry, something went wrong"
  })
);

server.get('*', (req, res) => {
  return res.status(404).send("Requested page isn't found")
});

server.listen(port, () => {
  console.log(`Listining to server on port ${port}`)
});