import React, { useEffect, useState } from 'react';
import { Col, Container, Row, Spinner } from 'react-bootstrap';
import MoviesApi from "../../../api/tmdbData";
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
    <Container id="allMovies" className="min-vh-100 w-100 justify-content-md-center my-5">
      <h1 className='py-5 my-5'>
        All Movies
      </h1>

      <Row>
        {loading ? (
          <Col className="text-center" xs="12">
            <Spinner animation="border" variant="dark" />
          </Col>
        ) : (
          moviesList?.length ? (
            <Listing
              list={moviesList}
              favs={favs}
              comments={comments}
              addToFavs={addToFavs}
              removeFromFav={removeFromFav}
              addComment={addComment}
              all
            />
          ) : <Col className="text-center pb-5 mb-5">{"No Movies Retrieved"}</Col>
        )}
      </Row>
    </Container>
  );
}
