import React, { useState } from 'react';
import { Button, Card, Col, Tooltip } from 'react-bootstrap';
import star from "../../../assets/images/icons/star.png";
import Modal from "../../modal";
import './style.css';

export default function Movie({ data, fav, addToFav, removeFromFav, all }) {
  const { Img, Body, Title, Text } = Card;

  const { id, title, poster_path, overview, release_date } = data;

  const [modal, setModal] = useState(false);

  return (
    <Col lg="2" sm="4" xs="6">
      <Card key={id}  >
        <Img variant="top" src={poster_path ? `https://image.tmdb.org/t/p/original/${poster_path}` : "https://executionconsulting.com/wp-content/uploads/2016/05/ef3-placeholder-image.jpg"} />

        <Body>
          <Title>
            {(all && fav) && <Tooltip >
              <img src={star} alt="" width={"15px"} />
              {' '}
            </Tooltip>}
            {title}
          </Title>

          <Text>
            {release_date ? release_date : "No Release Date"}
          </Text>

          <Text>
            {overview ? overview : "No overview Added"}
          </Text>

          <Button variant={fav ? "danger" : "success"} onClick={fav ? removeFromFav : addToFav} className="p-2 my-2 w-100">
            {fav ? "Remove From Favorites" : "Add To Favorites"}
          </Button>

          <Button variant="primary" onClick={() => setModal(true)} className="p-2 my-2 w-100">
            {"Show Details"}
          </Button>
        </Body>
      </Card>

      <Modal data={data} show={modal} close={() => setModal(false)} fav={fav} favClick={fav ? removeFromFav : addToFav} />
    </Col>
  );
}
