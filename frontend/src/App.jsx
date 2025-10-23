import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import { createBrowserRouter, RouterProvider } from 'react-router'
import RootLayout from './assets/pages/RootLayout'
import Homepage from './assets/pages/home'
import Champions from './assets/pages/champions'
import Tierlists from './assets/pages/tierlists'
import Error from './assets/pages/error'

  const router = createBrowserRouter([
    {
      path: '/', 
      element: <RootLayout />,
      errorElement: <Error />,
      children: [
        {
          index: true,
          element: <Homepage />
        },
        {
          path: "champions",
          element: <Champions />
        },
        {
          path: "tierlists",
          element: <Tierlists />
        }

      ]
    },
  ])

function App() {

  return (
    <RouterProvider router={router} />
  )
}

export default App
