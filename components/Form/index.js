export default function Form({ onSubmit, action, data }) {
  const locations = [
    { title: "Please Pick One...", value: "" },
    { title: "Amman", value: "Amman" },
    { title: "Irbid", value: "Irbid" },
    { title: "Aqaba", value: "Aqaba" },
    { title: "Ma'an", value: "Ma'an" }
  ];

  const onFormSubmit = e => {
    e.preventDefault();

    const data = {
      location: e.target.country.value,
      minCustomers: e.target.minCustomers.value,
      maxCustomers: e.target.maxCustomers.value,
      avgCookies: e.target.avgCookies.value,
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
                <div>
                  <label className="block text-sm font-medium text-gray-700">Location</label>
                  <select required name="country" disabled={action === "view"} className="mt-1 py-3 px-2 block w-full py-2 px-3 border border-gray-300 bg-white rounded-md shadow-sm focus:outline-none focus:ring-orange-500 focus:border-orange-500 sm:text-sm">
                    {locations.map((location, i) => (
                      <option value={location.value} key={i} selected={location.value === data?.location}>{location.title}</option>
                    ))}
                  </select>
                </div>

                <div className="grid grid-cols-3 sm:col-span-12 gap-6">
                  <div>
                    <label className="block text-sm font-medium text-gray-700">Min Customers per Hour</label>
                    <input required type="number" disabled={action === "view"} min={0} defaultValue={data?.minCustomers} name="minCustomers" className="mt-1 py-3 px-2 focus:ring-orange-500 focus:border-orange-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md" />
                  </div>

                  <div>
                    <label className="block text-sm font-medium text-gray-700">Max Customers per Hour</label>
                    <input required type="number" disabled={action === "view"} min={0} defaultValue={data?.maxCustomers} name="maxCustomers" className="mt-1 py-3 px-2 focus:ring-orange-500 focus:border-orange-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md" />
                  </div>

                  <div>
                    <label className="block text-sm font-medium text-gray-700">Average Cookies Count per Sale</label>
                    <input required type="number" disabled={action === "view"} min={0} defaultValue={data?.avgCookies} step={0.01} name="avgCookies" className="mt-1 py-3 px-2 focus:ring-orange-500 focus:border-orange-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md" />
                  </div>
                </div>

                {(<div className="text-right">
                  <button type="submit" className="inline-flex justify-center py-2 px-4 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-orange-700 hover:bg-orange-900 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-orange-500">
                    {
                      action === "create" ? "Create"
                        : action === "duplicate" ? "Create"
                          : action === "view" ? "Reset"
                            : action === "update" ? "Update"
                              : action === "delete" ? "Delete"
                                : "Submit"
                    }
                  </button>
                </div>)}
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
  )
}