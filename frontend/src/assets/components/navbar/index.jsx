import { NavLink } from "react-router";
import Button from "../UI/Button";
import { IoMenu } from "react-icons/io5";
import { IoMdClose } from "react-icons/io";
import { useEffect, useRef, useState } from "react";
import Logo from "./Logo";

const navItems = [
    { label: "Home", to: "/" },
    { label: "Champions", to: "/champions" },
    { label: "Tierlists", to: "/tierlists" }
];

const MOBILE_MENU_ID = "navbar-mobile-menu";

const navLinkClasses = ({ isActive }) => [
    "text-sm font-medium transition-colors",
    isActive ? "text-primary" : "text-text-primary hover:text-primary"
].join(" ");

function NavLinks({ orientation = "horizontal", onNavigate }) {
    const isHorizontal = orientation === "horizontal";
    const listClasses = isHorizontal
        ? "flex items-center gap-8"
        : "flex flex-col gap-4";

    return (
        <ul className={listClasses}>
            {navItems.map(({ label, to }) => (
                <li key={to}>
                    <NavLink
                        to={to}
                        className={navLinkClasses}
                        onClick={onNavigate}
                        end={to === "/"}
                    >
                        {label}
                    </NavLink>
                </li>
            ))}
        </ul>
    );
}


export default function Navbar() {

    const [isOpen, setIsOpen] = useState(false);
    const triggerRef = useRef(null)
    const closeBtnRef = useRef(null)

    useEffect(() => {
        if (isOpen) {
            document.body.classList.add("overflow-hidden");
            closeBtnRef.current?.focus();
        } else {
            document.body.classList.remove("overflow-hidden");
        }
        }, [isOpen]);

    const closeMenu = () => {
        triggerRef.current?.focus();
        setIsOpen(false);
    };
    return (
        <header className=" max-w-(--sp-container) w-full ">
            <div className="hidden sm:flex sticky place-content-between top-0 bg-[#202020] py-4 px-8 rounded-full mx-auto mb-8 shadow-lg shadow-black/30">
                {/* Desktop Navbar */}
                <div className="flex place-content-start gap-8 items-center">
                    <Logo />
                    <nav aria-label="Primary">
                        <NavLinks />
                    </nav>
                </div>    
                <div className="flex items-center justify-center">
                    <Button>Login</Button>
                </div>
            </div>

            <div className="sm:hidden">
                {/* Mobile Navbar */}
                <div className="sticky top-0 z-50 flex place-content-between bg-[#202020] py-4 px-8 mx-auto mb-8 shadow-lg shadow-black/30">
                    <p className="text-sm font-bold">Icon</p>
                    <button
                        type="button" 
                        aria-label={isOpen ? "Close menu" : "Open menu"}
                        aria-expanded={isOpen}
                        aria-controls={MOBILE_MENU_ID}
                        onClick={() => setIsOpen(true)}
                        className="flex items-center"
                        ref={triggerRef}
                    >
                        <IoMenu size={28} />
                    </button>
                </div>

                {/* Overlay oscurecido */}
                {isOpen && (
                    <div
                        role="presentation"
                        className="fixed inset-0 z-40 bg-black/40 backdrop-blur-sm backdrop-saturate-150 transition-opacity"
                        onClick={closeMenu}
                    />
                )}
                {/* Sidebar deslizable */}
                <nav
                    id={MOBILE_MENU_ID}
                    className={[
                    "fixed top-0 right-0 z-50 h-dvh w-3/4 max-w-xs bg-[#202020] p-6 shadow-lg shadow-black/30 transition-transform",
                    isOpen ? "translate-x-0" : "translate-x-full"
                    ].join(" ")}
                    role="dialog"
                    aria-modal="true"
                    aria-hidden={!isOpen}
                    
                >
                    <div className="flex justify-end mb-8">
                        <button
                            type="button"
                            aria-label="Close menu"
                            onClick={closeMenu}
                            className="flex items-center"
                            ref={closeBtnRef} 
                        >
                            <IoMdClose size={28} />
                        </button>
                    </div>
                    <NavLinks orientation="vertical" onNavigate={closeMenu} />
                    <div className="mt-6">
                        <Button onClick={closeMenu}>Login</Button>
                    </div>
                </nav>
            </div>
        </header>
    )
}