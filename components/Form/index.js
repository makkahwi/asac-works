export default function Form() {
  const locations = [
    { title: "Please Pick One..." },
    { title: "Amman", value: "amman" },
    { title: "Irbid", value: "irbid" },
    { title: "Aqaba", value: "aqaba" },
    { title: "Ma'an", value: "maan" }
  ];

  return (
    <div>
      <div className="md:grid md:grid-cols-2 md:gap-6">
        <div className="mt-5 md:mt-0 md:col-span-2">
          <form onSubmit={""}>
            <div className="shadow sm:rounded-md sm:overflow-hidden">
              <div className="px-4 py-5 bg-orange-500 space-y-6 sm:p-6">
                <div>
                  <label className="block text-sm font-medium text-gray-700">Location</label>
                  <select name="country" className="mt-1 py-3 px-2 block w-full py-2 px-3 border border-gray-300 bg-white rounded-md shadow-sm focus:outline-none focus:ring-orange-500 focus:border-orange-500 sm:text-sm">
                    {locations.map(location => (
                      <option value={location.value}>{location.title}</option>
                    ))}
                  </select>
                </div>

                <div className="grid grid-cols-3 sm:col-span-12 gap-6">
                  <div>
                    <label className="block text-sm font-medium text-gray-700">Min Customers per Hour</label>
                    <input type="number" min={0} name="minCustomers" className="mt-1 py-3 px-2 focus:ring-orange-500 focus:border-orange-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md" />
                  </div>

                  <div>
                    <label className="block text-sm font-medium text-gray-700">Max Customers per Hour</label>
                    <input type="number" min={0} name="maxCustomers" className="mt-1 py-3 px-2 focus:ring-orange-500 focus:border-orange-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md" />
                  </div>

                  <div>
                    <label className="block text-sm font-medium text-gray-700">Average Cookies Count per Sale</label>
                    <input type="number" min={0} name="avgCookies" className="mt-1 py-3 px-2 focus:ring-orange-500 focus:border-orange-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md" />
                  </div>
                </div>

                <div className="text-right">
                  <button type="submit" className="inline-flex justify-center py-2 px-4 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-orange-700 hover:bg-orange-900 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-orange-500">
                    Submit
                  </button>
                </div>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
  )
}