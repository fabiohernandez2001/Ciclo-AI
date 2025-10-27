import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import { createBrowserRouter, RouterProvider } from 'react-router'
import RootLayout from './pages/RootLayout'
import Homepage from './pages/home'
import Champions from './pages/champions'
import Tierlists from './pages/tierlists'
import Error from './pages/error'
import { QueryClient, QueryClientProvider } from '@tanstack/react-query'

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

const queryClient = new QueryClient()

function App() {

  return (
    <QueryClientProvider client={queryClient}>
      <RouterProvider router={router} />
    </QueryClientProvider>
  )
}

export default App
