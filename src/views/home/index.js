import React from 'react';
import '../../assets/css/style.css';
import Tours from '../../components/tours';
import Header from '../../components/header';

export default function Home() {

  return (
    <main>
      <Header />

      <Tours />
    </main>
  );
}
