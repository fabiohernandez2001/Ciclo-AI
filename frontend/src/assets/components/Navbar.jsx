import { NavLink } from "react-router";
import Button from "./UI/Button";
import { IoMenu } from "react-icons/io5";
import { useState } from "react";


export default function Navbar() {

    const [isOpen, setIsOpen] = useState(false);


    return (
        <header className=" max-w-(--sp-container) w-full ">
            <div className="hidden sm:flex sticky place-content-between top-0 bg-[#202020] py-4 px-8 rounded-full mx-auto mb-8 shadow-lg shadow-black/30">
                <div className="flex place-content-start gap-8">
                    <div>
                        <h1 className="text-xl font-bold">Icon</h1>
                    </div>
                    <nav className="flex items-center">
                        <ul className="flex place-content-center gap-8">
                            <li>
                                <NavLink to="/">Home</NavLink>
                            </li>
                            <li>
                                <NavLink to="/champions">Champions</NavLink>
                            </li>
                            <li>
                                <NavLink to="/tierlists">Tierists</NavLink>
                            </li>
                        </ul>
                    </nav>
                </div>    
                <div className="flex items-center justify-center">
                    <Button>Login</Button>
                </div>
            </div>
            <div className="flex sm:hidden sticky place-content-between top-0 bg-[#202020] ">
                asdmad
            </div>
            {/** 
            
            */}
            
        </header>
    )
}