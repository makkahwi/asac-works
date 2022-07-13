import React from 'react';
import { Container } from 'react-bootstrap';
import Header from '../../components/header';

export default function Home() {

  return (
    <main>
      <Header />

      <Container className="w-100 justify-content-md-center my-5">
        <h2>
          Please pick a page to visit from Navigation Bar above
        </h2>
      </Container>
    </main>
  );
}
