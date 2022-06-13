import Head from "next/head";
import Header from "../components/Header";
import Cookies from "./Cookies";

export default function Landing() {
  return (
    <>
      <Head>
        <title>Cookie Stand Admin - Suhaib Ahmad</title>
      </Head>

      <Header />

      <Cookies />
    </>


  )
}
