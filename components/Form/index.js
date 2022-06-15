import { locations, countries } from "../../data";

export default function Form({ onSubmit, action, onChange, data, reset }) {

  const onFormSubmit = e => {
    e.preventDefault();

    const data = {
      location: e.target.location.value,
      minimum_customers_per_hour: e.target.minimum_customers_per_hour.value,
      maximum_customers_per_hour: e.target.maximum_customers_per_hour.value,
      average_cookies_per_sale: e.target.average_cookies_per_sale.value,
    };

    onSubmit(data);
  }

  return (
    <div>
      <div className="md:grid md:grid-cols-2 md:gap-6">
        <div className="mt-5 md:mt-0 md:col-span-2">
          <form onSubmit={onFormSubmit}>
            <div className="shadow sm:rounded-md sm:overflow-hidden">
              <div className="px-4 py-5 bg-orange-500 space-y-6 sm:p-6">
                <h1 className="text-white text-xl text-center uppercase">{`${action} Data`}</h1>
                <div className="grid grid-cols-2 sm:col-span-12 gap-6">
                  <div>
                    <label className="block text-sm font-medium text-gray-700">Country</label>
                    <select required name="country" value={data?.country ? data?.country : data?.location ? countries.find(country => country.value === data?.location.split(", ")[1]).value : ""} onChange={e => onChange("country", e.target.value)} disabled={action === "view" || action === "delete"} className="mt-1 py-3 px-2 block w-full py-2 px-3 border border-gray-300 bg-white rounded-md shadow-sm focus:outline-none focus:ring-orange-500 focus:border-orange-500 sm:text-sm">
                      <option value={""}>{"Please Pick One..."}</option>

                      {countries.map((country, i) => (
                        <option value={country.value} key={i}>{country.title}</option>
                      ))}
                    </select>
                  </div>

                  <div>
                    <label className="block text-sm font-medium text-gray-700">Location</label>
                    <select required name="location" value={data?.location || ""} onChange={e => onChange("location", e.target.value)} disabled={action === "view" || action === "delete"} className="mt-1 py-3 px-2 block w-full py-2 px-3 border border-gray-300 bg-white rounded-md shadow-sm focus:outline-none focus:ring-orange-500 focus:border-orange-500 sm:text-sm">
                      <option value={""}>{"Please Pick One..."}</option>

                      {data.country ? (locations.filter(location => location.country === data.country).map((location, i) => (
                        <option value={location.value} key={i}>{location.title}</option>
                      ))) : (locations.map((location, i) => (
                        <option value={location.value} key={i}>{location.title}</option>
                      )))}
                    </select>
                  </div>
                </div>

                <div className="grid grid-cols-3 sm:col-span-12 gap-6">
                  <div>
                    <label className="block text-sm font-medium text-gray-700">Min Customers per Hour</label>
                    <input required type="number" disabled={action === "view" || action === "delete"} min={0} value={data?.minimum_customers_per_hour || 0} onChange={e => onChange("minimum_customers_per_hour", e.target.value)} name="minimum_customers_per_hour" className="mt-1 py-3 px-2 focus:ring-orange-500 focus:border-orange-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md" />
                  </div>

                  <div>
                    <label className="block text-sm font-medium text-gray-700">Max Customers per Hour</label>
                    <input required type="number" disabled={action === "view" || action === "delete"} min={0} value={data?.maximum_customers_per_hour || 0} onChange={e => onChange("maximum_customers_per_hour", e.target.value)} name="maximum_customers_per_hour" className="mt-1 py-3 px-2 focus:ring-orange-500 focus:border-orange-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md" />
                  </div>

                  <div>
                    <label className="block text-sm font-medium text-gray-700">Average Cookies Count per Sale</label>
                    <input required type="number" disabled={action === "view" || action === "delete"} min={0} value={data?.average_cookies_per_sale || 0} onChange={e => onChange("average_cookies_per_sale", e.target.value)} step={0.01} name="average_cookies_per_sale" className="mt-1 py-3 px-2 focus:ring-orange-500 focus:border-orange-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md" />
                  </div>
                </div>

                {(<div className="text-right">
                  <div className="inline-flex rounded-md shadow-sm" role="group">
                    <button type="button" onClick={reset} className="py-2 px-4 text-md font-medium text-white bg-yellow-500 rounded-l-lg border border-black hover:bg-yellow-700 focus:z-10 focus:ring-2 focus:ring-yellow-700 focus:bg-yellow-700 dark:bg-yellow-700 dark:border-yellow-600 dark:text-white dark:hover:text-white dark:hover:bg-yellow-600 dark:focus:ring-yellow-500 dark:focus:text-white">
                      Reset
                    </button>

                    {action !== "view" && (
                      <button type="submit" className="py-2 px-4 text-md font-medium text-white bg-green-500 rounded-r-md border border-black hover:bg-green-700 focus:z-10 focus:ring-2 focus:ring-green-700 focus:bg-green-700 dark:bg-green-700 dark:border-green-600 dark:text-white dark:hover:text-white dark:hover:bg-green-600 dark:focus:ring-green-500 dark:focus:text-white">
                        {
                          action === "create" ? "Create"
                            : action === "duplicate" ? "Create"
                              : action === "update" ? "Update"
                                : action === "delete" ? "Delete"
                                  : "Submit"
                        }
                      </button>
                    )}
                  </div>
                </div>)}
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
  )
}