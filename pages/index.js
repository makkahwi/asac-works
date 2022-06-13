import Head from "next/head";
import { useState } from "react";
import Footer from "../components/Footer";
import CreateForm from "../components/Form";
import Header from "../components/Header";
import ReportTable from "../components/Table";

export default function Home() {
  const [list, setList] = useState([]);

  const [action, setAction] = useState("create")

  const [formData, setFormData] = useState({})

  const onActionClick = (id, action) => {
    const data = list.find(data => data.id === id);

    action === "duplicate" ? (
      setFormData(data),
      setAction("duplicate")
    ) : action === "view" ? (
      setFormData(data),
      setAction("view")
    ) : action === "update" ? (
      setFormData(data),
      setAction("update")
    ) : action === "delete" && (
      setFormData(data),
      setAction("delete")
    )
  };

  const onActionSubmit = (data) => {
    (action === "duplicate" || action === "create") ? (
      setList(current => [...current, { ...data, id: list.length + 1 }]),
      setFormData({}),
      setAction("create")
    ) : action === "update" ? (
      setList(current => current.map(item => item.id !== formData.id ? item : formData )),
      setFormData({}),
        setAction("create")
    ) : action === "delete" && (
      setList(current => current.filter(item => item.id !== formData.id)),
      setFormData({}),
      setAction("create")
    )
  };

  const onReset = () => {
    setFormData({})
    setAction("create")
  };

  const onFormDataChange = (key, value) => {
    let newFormData = { ...formData }
    newFormData[key] = value
    setFormData(newFormData)
  };

  return (
    <>
      <Head>
        <title>Cookie Stand Admin - Suhaib Ahmad</title>
      </Head>

      <Header />

      <main className="py-10 px-10">
        <CreateForm onSubmit={onActionSubmit} action={action} data={formData} onChange={onFormDataChange} reset={onReset} length={list.length} />
        {list.length ? (<ReportTable data={list} onActionClick={onActionClick} />) : <h2 className="text-center pt-5">No Cookie Stands Available</h2>}
      </main>

      <Footer count={list.length} unique={list.reduce((final, item) => final.find(it => it.location === item.location) ? final : final = [...final, item], []).length} />
    </>


  )
}
