import { Outlet } from "react-router";
import Navbar from "../components/navbar";

export default function RootLayout() {
  return (
    <>
        <Navbar />
        <main className="max-w-(--sp-container) w-full px-8 sm:px-0">
            <Outlet />
        </main>
    </>
  )
}