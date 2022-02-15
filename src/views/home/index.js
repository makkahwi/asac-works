import React from 'react';
import '../../assets/css/style.css';
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
