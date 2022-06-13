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
      setAction("duplicate"),
      window.scrollTo({ top: 0, left: 0, behavior: 'smooth' })
    ) : action === "view" ? (
      setFormData(data),
      setAction("view"),
      window.scrollTo({ top: 0, left: 0, behavior: 'smooth' })
    ) : action === "update" ? (
      setFormData(data),
      setAction("update"),
      window.scrollTo({ top: 0, left: 0, behavior: 'smooth' })
    ) : action === "delete" && (
      setFormData(data),
      setAction("delete"),
      window.scrollTo({ top: 0, left: 0, behavior: 'smooth' })
    )
  };

  const onActionSubmit = (data) => {
    (action === "duplicate" || action === "create") ? (
      setList(current => [...current, { ...data, id: list.length + 1 }]),
      setFormData({}),
      setAction("create"),
      document.getElementById(`data${list.length}`)?.scrollIntoView({ behavior: 'smooth' })
    ) : action === "update" ? (
      setList(current => current.map(item => item.id !== formData.id ? item : formData)),
      setFormData({}),
      setAction("create"),
      document.getElementById(`data${formData.id}`).scrollIntoView({ behavior: 'smooth' })
    ) : action === "delete" && (
      setList(current => current.filter(item => item.id !== formData.id)),
      setFormData({}),
      setAction("create"),
      document.getElementById(`data${formData.id - 1}`).scrollIntoView({ behavior: 'smooth' })
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
