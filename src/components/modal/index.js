import React from 'react';
import { Button, Col, Form, Image, Modal, Row } from 'react-bootstrap/';

export default function Modals({ data, show, close, fav, addComment, favClick, comments }) {
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
        <Col>
          {overview}
        </Col>

        <Col className="pt-4">
          {`Release On ${release_date}`}
        </Col>
      </Body>

      <Footer>
        <Row className='w-100'>
          <h5>Comments</h5>

          <Col xs="12" className='my-2'>
            {comments ? comments.map((comment, i) => (
              <p key={i}>
                {comment}
              </p>
            )) : <small>{"No Comments Added Yet"}</small>}
          </Col>

          <Col xs="12" className='my-2'>
            <Form onSubmit={e => { e.preventDefault(); addComment(id, e.target.comment.value); favClick(); }}>
              <Control name="comment" type="textarea" placeholder='Add Comment As You Mark The Movie as Fav' />

              <Button variant={fav ? "danger" : "success"} type="submit" className='my-3'>
                {fav ? "Remove From Favorites" : "Add To Favorites"}
              </Button>
            </Form>
          </Col>
        </Row>
      </Footer>
    </Modal >
  );
}
