import React from 'react';
import Header from '../../components/header';
import Footer from '../../components/footer';
import Tours from '../../components/tours';
import '../../assets/css/style.css';

export default function Home() {

  return (
    <main>
      <Header />

      <Tours />

      <Footer />
    </main>
  );
}
