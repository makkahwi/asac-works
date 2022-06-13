import { useState } from "react"
import Login from "../../components/Login"
import Registration from "../../components/Registration"
import Welcoming from "../../components/Welcoming"

export default function Landing() {

  const [reg, setReg] = useState(false)

  return (
    <div className="relative bg-white overflow-hidden h-min-screen">
      <div className="relative z-10 pb-8 bg-white sm:pb-16 md:pb-20 lg:max-w-2xl lg:w-full lg:pb-28 xl:pb-32">
        <svg className="hidden lg:block absolute right-0 inset-y-0 h-full w-48 text-white transform translate-x-1/2" fill="currentColor" viewBox="0 0 100 100" preserveAspectRatio="none" aria-hidden="true">
          <polygon points="50,0 100,0 50,100 0,100" />
        </svg>

        <div>
          <div className="relative p-1">
            <nav className="relative flex items-center justify-between sm:h-10 lg:justify-start" aria-label="Global">
              <div className="flex items-center flex-grow flex-shrink-0 lg:flex-grow-0" />
            </nav>
          </div>
        </div>

        <main className="mt-5 mx-auto max-w-7xl sm:mt-3 sm:px-7 md:mt-5 lg:mt-5 lg:px-7 xl:mt-7">
          <Welcoming />

          {reg ? (
            <Registration setReg={setReg} />
          ) : (
            <Login setReg={setReg} />
          )}


          <p className="mt-3 text-base text-gray-500 sm:mt-5 sm:max-w-xl sm:mx-auto md:mt-5 lg:mx-0 absolute bottom-5">
            By <a href="https://Suhaib.dev" target="_blank">Suhaib Ahmad</a>
          </p>
        </main>
      </div>

      <div className="lg:absolute lg:inset-y-0 lg:right-0 lg:w-1/2">
        <img className="h-56 w-full object-cover sm:h-72 md:h-96 lg:w-full lg:h-full absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2" src="https://scontent.famm5-1.fna.fbcdn.net/v/t39.30808-6/277805257_5680134048668909_2135372447598706414_n.jpg?_nc_cat=105&ccb=1-7&_nc_sid=36a2c1&_nc_ohc=LOOEZIUKxVgAX-duxjx&_nc_ht=scontent.famm5-1.fna&oh=00_AT9oNIlG0zBk8SY8cDwDGaFN6RAd1PBRhERzHHiCRMiRHQ&oe=62AC6736" alt="" />
      </div>
    </div>
  )
}