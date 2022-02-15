import React from 'react';
import '../../assets/css/style.css';
import Tours from '../tours/Tours';
import Header from '../../components/header/Header';

export default function Home() {

  return (
    <main>
      <Header />

      <Tours />
    </main>
  );
}
