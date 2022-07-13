import React from 'react';
import { Button, ButtonGroup, Col, Form, Image, Modal, Row } from 'react-bootstrap/';

export default function Modals({ data, show, close, fav, addToFav, updateFav, deleteFav }) {
  const { Header, Title, Body, Footer } = Modal;
  const { Control } = Form;
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
        <Col style={{ textAlign: "justify" }}>
          {overview}
        </Col>

        <Col className="pt-4" style={{ textAlign: "right" }}>
          {release_date ? `${release_date > new Date() ? "To be released" : "Released"} on ${release_date}` : "No Release Date"}
        </Col>
      </Body>

      <Footer>
        <Row className='w-100'>
          <h5>Comment</h5>

          <Col xs="12" className='my-2'>
            <p style={{ textAlign: "justify" }}>
              {data.comment || <small>{"No Comment Was Added Yet"}</small>}
            </p>
          </Col>

          <Col xs="12" className='my-2'>
            <Form onSubmit={e => { e.preventDefault(); if (!fav) { addToFav({ id, comment: e.target.comment.value }) } else { updateFav({ id, comment: e.target.comment.value }) }; }}>
              <Control name="comment" type="textarea" placeholder='Add Comment As You Mark The Movie as Fav' />

              <div style={{ textAlign: "right" }}>
                {fav ? (
                  <ButtonGroup>
                    <Button variant={"warning"} type="submit" className='my-3'>
                      {"Edit Favorite"}
                    </Button>

                    <Button variant={"danger"} type="submit" className='my-3' onClick={deleteFav}>
                      {"Delete From Favorites"}
                    </Button>
                  </ButtonGroup>
                ) : (
                  <Button variant={fav ? "danger" : "success"} type="submit" className='my-3'>
                    {"Add To Favorites"}
                  </Button>
                )}
              </div>
            </Form>
          </Col>
        </Row>
      </Footer>
    </Modal >
  );
}
