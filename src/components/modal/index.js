import React from 'react';
import { Button, Col, Image, Modal } from 'react-bootstrap/';
import './style.css';

export default function Modals({ data, show, close, fav, favClick }) {
  const { Header, Title, Body, Footer } = Modal;
  const { id, title, release_date, poster_path, overview } = data;

  return (
    <Modal show={show} onHide={close} key={id} >
      <Header closeButton>
        <Title>
          {title || "No title"}
        </Title>
      </Header>

      <Body>
        <Image variant="top" className='w-100' src={poster_path ? `https://image.tmdb.org/t/p/original/${poster_path}` : "https://executionconsulting.com/wp-content/uploads/2016/05/ef3-placeholder-image.jpg"} />
      </Body>

      <Body>
        {overview}
      </Body>

      <Footer>
        <Col>
          {`Release On ${release_date}`}
        </Col>

        <Col>
          <Button variant={fav ? "danger" : "success"} onClick={favClick}>
            {fav ? "Remove From Favorites" : "Add To Favorites"}
          </Button>
        </Col>
      </Footer>
    </Modal>
  );
}
