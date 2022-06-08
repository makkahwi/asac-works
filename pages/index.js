import Head from "next/head";
import Header from "../components/Header";
import Form from "../components/Form";
import Footer from "../components/Footer";

export default function Home() {

  return (
    <>
      <Head>
        <title>Cookie Stand Admin - Suhaib Ahmad</title>
      </Head>

      <Header />

      <main className="py-10 px-10">
        <Form />
      </main>

      <Footer />
    </>


  )
}
