const express = require('express');
const cors = require('cors');

const server = express();

const port = 5050;

server.use(cors());

function Movie({ title, poster_path, overview }) {
  this.title = title;
  this.poster_path = poster_path;
  this.overview = overview;
};

const haveData = query => (
  (query.title && query.poster_path && query.overview) ? true : false
);

server.get('/', (req, res) => (
  (haveData(req.query)) ? (
    res.status(200).send(new Movie(req.query))
  ) : (
    res.status(400).send("The data format isn't correct")
  )
));

server.get('/favorite', (req, res) => {
  return res.status(200).send("Welcome to Favorite Page")
});

server.get('/500', (req, res) => {
  return res.status(500).send("Sorry, something went wrong")
});

server.get('*', (req, res) => {
  return res.status(404).send("Rquested page isn't found")
});

server.listen(port, () => {
  console.log(`Listining to server on port ${port}`)
});