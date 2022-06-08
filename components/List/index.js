export default function List({ data }) {
  return (
    <div className="py-4">
      <table className="table-auto w-full text-center">
        <thead>
          <tr className="py-2 bg-orange-500">
            <th>#</th>
            <th>Location</th>
            <th>Min Customers per Hour</th>
            <th>Max Customers per Hour</th>
            <th>Average Cookies Count per Sale</th>
          </tr>
        </thead>

        <tbody>
          {data?.map((item, i) => (
            <tr className={`h-20 ${i % 2 === 0 ? "bg-gray-100 hover:bg-white" : "hover:bg-gray-100"}`} key={i}>
              <td>{i + 1}</td>
              <td>{item.location}</td>
              <td>{item.minCustomers}</td>
              <td>{item.maxCustomers}</td>
              <td>{item.avgCookies}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}