import { faCopy, faEdit, faEye, faTrash } from "@fortawesome/free-solid-svg-icons"
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome"

export default function List({ data, onAction }) {
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
            <th>Actions</th>
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
              <td>
                <div className="inline-flex rounded-md shadow-sm" role="group">
                  <button type="button" onClick={() => onAction(item.id || i, "duplicate")} className="py-2 px-4 text-xs font-medium text-white bg-green-500 rounded-l-lg border border-green-200 hover:bg-green-700 focus:z-10 focus:ring-2 focus:ring-green-700 focus:bg-green-700 dark:bg-green-700 dark:border-green-600 dark:text-white dark:hover:text-white dark:hover:bg-green-600 dark:focus:ring-green-500 dark:focus:text-white">
                    <FontAwesomeIcon icon={faCopy} />
                  </button>

                  <button type="button" onClick={() => onAction(item.id || i, "view")} className="py-2 px-4 text-xs font-medium text-white bg-blue-500 border-t border-b border-blue-200 hover:bg-blue-700 focus:z-10 focus:ring-2 focus:ring-blue-700 focus:bg-blue-700 dark:bg-blue-700 dark:border-blue-600 dark:text-white dark:hover:text-white dark:hover:bg-blue-600 dark:focus:ring-green-500 dark:focus:text-white">
                    <FontAwesomeIcon icon={faEye} />
                  </button>

                  <button type="button" onClick={() => onAction(item.id || i, "update")} className="py-2 px-4 text-xs font-medium text-dark bg-yellow-500 border-t border-b border-yellow-200 hover:bg-yellow-700 focus:z-10 focus:ring-2 focus:ring-yellow-700 focus:bg-yellow-700 dark:bg-yellow-700 dark:border-yellow-600 dark:text-white dark:hover:text-white dark:hover:bg-yellow-600 dark:focus:ring-yellow-500 dark:focus:text-white">
                    <FontAwesomeIcon icon={faEdit} />
                  </button>

                  <button type="button" onClick={() => onAction(item.id || i, "delete")} className="py-2 px-4 text-xs font-medium text-white bg-red-500 rounded-r-md border border-red-200 hover:bg-red-700 focus:z-10 focus:ring-2 focus:ring-red-700 focus:bg-red-700 dark:bg-red-700 dark:border-red-600 dark:text-white dark:hover:text-white dark:hover:bg-red-600 dark:focus:ring-red-500 dark:focus:text-white">
                    <FontAwesomeIcon icon={faTrash} />
                  </button>
                </div>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}