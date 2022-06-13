import { faCopy, faEdit, faEye, faTrash } from "@fortawesome/free-solid-svg-icons"
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome"
import { hourly_sales, hours } from "../../data"

export default function List({ data, onActionClick }) {
  return (
    <div className="py-4">
      <table className="table-auto w-full text-center">
        <thead>
          <tr className="py-2 bg-orange-500">
            <th rowSpan={2}>#</th>
            <th rowSpan={2}>Location</th>
            <th rowSpan={2}>Min Customers per Hour</th>
            <th rowSpan={2}>Max Customers per Hour</th>
            <th rowSpan={2}>Average Cookies Count per Sale</th>
            <th colSpan={hours.length + 1}>Hourly Sales</th>
            <th rowSpan={2}>Actions</th>
          </tr>

          <tr className="py-2 bg-orange-500">
            {hours.map((hour, i) => (<th key={i}>{hour}</th>))}
            <th>Total Location Sale</th>
          </tr>
        </thead>

        <tbody>
          {data?.map((item, i) => (
            <tr className={`h-20 ${i % 2 === 0 ? "bg-gray-100 hover:bg-white" : "hover:bg-gray-100"}`} key={i} id={`data${item.id}`}>
              <td>{i + 1}</td>
              <td><a href={`https://www.google.com/maps/search/${item.location.replace(" ", "+")}`} target="_blank" className="text-orange-500 underline">{item.location}</a></td>
              <td>{item.minCustomers}</td>
              <td>{item.maxCustomers}</td>
              <td>{item.avgCookies}</td>
              {hourly_sales.map((sales, i) => (<td key={i}>{sales}</td>))}
              <td>{hourly_sales.reduce((total, sales) => total += sales, 0)}</td>
              <td>
                <div className="inline-flex rounded-md shadow-sm" role="group">
                  <div className="grid grid-cols-2 p-2 text-sm ">
                    <FontAwesomeIcon type="button" onClick={() => onActionClick(item.id, "duplicate")} className="m-3 text-green-500" icon={faCopy} />

                    <FontAwesomeIcon type="button" onClick={() => onActionClick(item.id, "view")} className="m-3 text-blue-500" icon={faEye} />

                    <FontAwesomeIcon type="button" onClick={() => onActionClick(item.id, "update")} className="m-3 text-orange-500" icon={faEdit} />

                    <FontAwesomeIcon type="button" onClick={() => onActionClick(item.id, "delete")} className="m-3 text-red-500" icon={faTrash} />
                  </div>
                </div>
              </td>
            </tr>
          ))}
        </tbody>

        <tfoot>
          <tr className="py-3 bg-orange-500">
            <th colSpan={5}>
              Totals
            </th>
            {hourly_sales.map((sales, i) => (<th key={i}>{sales * data.length}</th>))}
            <th>{hourly_sales.reduce((total, sales) => total += (sales * data.length), 0)}</th>
            <th></th>
          </tr>
        </tfoot>
      </table>
    </div>
  )
}