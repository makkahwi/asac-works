import Head from "next/head";
import { useState } from "react";
import Footer from "../components/Footer";
import Form from "../components/Form";
import Header from "../components/Header";
import List from "../components/List";

export default function Home() {
  const [list, setList] = useState([
    {
      location: "Amman",
      minCustomers: 5,
      maxCustomers: 6,
      avgCookies: 7
    }
  ]);

  const addToList = data => setList(current => [...current, data]);

  return (
    <>
      <Head>
        <title>Cookie Stand Admin - Suhaib Ahmad</title>
      </Head>

      <Header />

      <main className="py-10 px-10">
        <Form onSubmit={addToList} />
        <List data={list} />
      </main>

      <Footer />
    </>


  )
}
