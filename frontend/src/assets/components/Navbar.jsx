import { NavLink } from "react-router";

export default function Navbar() {

    return (
        <header>
            <nav>
                <ul>
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
        </header>
    )
}