import { NavLink } from "react-router-dom";

export default function Logo() {
  return (
    <NavLink to="/" className="text-sm font-bold focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-primary/60 rounded">
      Icon
    </NavLink>
  );
}