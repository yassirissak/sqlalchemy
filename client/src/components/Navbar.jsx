import { useContext } from "react";
import { NavLink } from "react-router-dom";
import { AuthContext } from "../context/AuthContext";

const linkClass = ({ isActive }) =>
  `rounded-md px-3 py-2 text-sm font-medium transition ${
    isActive
      ? "bg-slate-900 text-white"
      : "text-slate-700 hover:bg-slate-100 hover:text-slate-950"
  }`;

function Navbar() {
   const {current_user, logout} = useContext(AuthContext)

  return (
    <nav className="border-b border-slate-200 bg-white">
      <div className="mx-auto flex w-full max-w-5xl flex-col gap-4 px-4 py-4 sm:flex-row sm:items-center sm:justify-between sm:px-6 lg:px-8">
        <NavLink to="/" className="text-xl font-bold text-slate-950">
          BlogApp
        </NavLink>

        <div className="flex flex-wrap gap-2">
          <NavLink to="/" className={linkClass}>
            Home
          </NavLink>
          { current_user && current_user.email ?
          <>
          <NavLink to="/add-post" className={linkClass}>
            Add post
          </NavLink>
          <NavLink to="/profile" className={linkClass}>
            Profile({current_user && current_user.username})
          </NavLink>
          <NavLink onClick={()=>logout()} className={linkClass}>
            Logout
          </NavLink>
          </>:
          <>
           <NavLink to="/register" className={linkClass}>
             Register
          </NavLink>
        
          <NavLink to="/login" className={linkClass}>
            Login
          </NavLink>
          </>
          }
        </div>
      </div>
    </nav>
  );
}

export default Navbar;
