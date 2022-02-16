import React, { useEffect, useState } from 'react';
import { Col, Container, Row, Spinner } from 'react-bootstrap';
import MoviesApi from "../../../api/movies";
import Listing from "../listing";

export default function MoviesList() {

  const [moviesList, setMoviesList] = useState([]);
  const [comments, setComments] = useState({});
  const [loading, setLoading] = useState(false);
  const [favs, setFavs] = useState(JSON.parse(localStorage.getItem("favs")) || []);

  useEffect(() => {
    setLoading(true);
    MoviesApi.getAll()
      .then(res => {
        setMoviesList(res);
      })
      .catch(e => {
        setMoviesList([]);
        console.log(e)
      })
      .finally(() => {
        setLoading(false);
      })
  }, [])

  const addToFavs = id => {
    const newFavs = [...favs, id]
    setFavs(newFavs);
    localStorage.setItem("favs", JSON.stringify(newFavs));
  };

  const removeFromFav = id => {
    const newFavs = favs.filter(movie => movie !== id);
    setFavs(newFavs);
    removeComments(id);
    localStorage.setItem("favs", JSON.stringify(newFavs));
  };

  const addComment = (id, comment) => {
    let newComments = { ...comments };
    if (comment?.length) { newComments[id] ? newComments[id] = [...newComments[id], comment] : newComments[id] = [comment] };
    setComments(newComments);
  };

  const removeComments = id => {
    let newComments = { ...comments };
    newComments[id] = undefined;
    setComments(newComments);
  };

  useEffect(() => console.log(comments), [comments]);

  return (
    <Container id="favMovies" className="w-100 justify-content-md-center my-5">
      <h1 className='py-5 my-5'>
        Fav Movies
      </h1>

      <Row>
        {loading ? (
          <Col className="text-center" xs="12">
            <Spinner animation="border" variant="dark" />
          </Col>
        ) : (
          favs?.length ? (
            <Listing
              list={moviesList.filter(movie => favs.indexOf(movie.id) >= 0)}
              favs={favs}
              comments={comments}
              addToFavs={addToFavs}
              removeFromFav={removeFromFav}
              addComment={addComment}
            />
          ) : <Col className="text-center pb-5 mb-5">{"No Fav Movies"}</Col>
        )}
      </Row>
    </Container>
  );
}
