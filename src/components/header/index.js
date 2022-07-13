import React from 'react';
import { Container, Row, Col } from 'react-bootstrap';
import './style.css';

export default function Head() {

  return (
    <Container id="header" className="header min-vh-100 w-100 justify-content-md-center" fluid>
      <Row>
        <Col className='title'>
          Welcome to Suhaib's NetenFlix
        </Col>
      </Row>
    </Container>
  );
}
