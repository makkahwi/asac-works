import Head from "next/head";
import { useState } from "react";
import Footer from "../components/Footer";
import Form from "../components/Form";
import Header from "../components/Header";
import List from "../components/List";

export default function Home() {
  const [list, setList] = useState([
    {
      location: "Test 1",
      minCustomers: 1,
      maxCustomers: 2,
      avgCookies: 3
    }
  ]);

  const [action, setAction] = useState("create")

  const [data, setData] = useState({})

  const onAction = (id, action) => {
    action === "duplicate" ? (() => {
      setData(list[id])
      setAction("duplicate")
    }) : action === "view" ? (() => {
      setData(list[id])
      setAction("view")
    }) : action === "update" ? (() => {
      setData(list[id])
      setAction("update")
    }) : action === "delete" && (() => {
      setData(list[id])
      setAction("delete")
    })
  };

  const addToList = data => setList(current => [...current, data]);

  return (
    <>
      <Head>
        <title>Cookie Stand Admin - Suhaib Ahmad</title>
      </Head>

      <Header />

      <main className="py-10 px-10">
        <Form onSubmit={addToList} action={action} data={data} />
        <List data={list} onAction={onAction} />
      </main>

      <Footer />
    </>


  )
}
