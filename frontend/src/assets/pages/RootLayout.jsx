import { Outlet } from "react-router";
import Navbar from "../components/navbar";

export default function RootLayout() {
  return (
    <>
        <Navbar />
        <main>
            <Outlet />
        </main>
    </>
  )
}