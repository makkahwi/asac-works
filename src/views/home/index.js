import React from 'react';
import Movies from '../../components/moviesList';
import Header from '../../components/header';

export default function Home() {

  return (
    <main>
      <Header />

      <Movies />
    </main>
  );
}
