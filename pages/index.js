import Head from "next/head";
import Header from "../components/Header";
import Cookies from "./Cookies";
import Landing from "./Landing";

export default function Home() {
  const JWT = "";

  return (
    <>
      <Head>
        <title>Cookie Stand Admin - Suhaib Ahmad</title>
      </Head>

      <Header />

      {JWT.length ? (
        <Cookies />
      ) : (
        <Landing />
      )}

    </>


  )
}
