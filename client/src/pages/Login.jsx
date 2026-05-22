import { useContext, useState } from "react";
import {api_url} from "../config.json"
import {toast} from "react-hot-toast"
import { AuthContext } from "../context/AuthContext";

function Login() {
   const {login} = useContext(AuthContext)

  const [email, setEmail] = useState()
  const [password, setPassword] = useState()


  const formSubmit = (e)=>{
    e.preventDefault()
    
    login(email, password)
    

  }


  return (
    <section className="mx-auto max-w-md">
      <h1 className="text-3xl font-bold text-slate-950">Login</h1>

      <form onSubmit={formSubmit} className="mt-6 space-y-4 rounded-lg border border-slate-200 bg-white p-6">
        <div>
          <label htmlFor="email" className="block text-sm font-medium text-slate-700">
            Email
          </label>
          <input
            onChange={e => setEmail(e.target.value)} value={email}
            type="email"
            className="mt-2 w-full rounded-md border border-slate-300 px-3 py-2 outline-none focus:border-slate-900 focus:ring-2 focus:ring-slate-200"
            placeholder="you@example.com"
          />
        </div>

        <div>
          <label htmlFor="password" className="block text-sm font-medium text-slate-700">
            Password
          </label>
          <input
             onChange={e => setPassword(e.target.value)} value={password}
            type="password"
            className="mt-2 w-full rounded-md border border-slate-300 px-3 py-2 outline-none focus:border-slate-900 focus:ring-2 focus:ring-slate-200"
            placeholder="Enter password"
          />
        </div>

        <button
          type="submit"
          className="w-full rounded-md bg-slate-900 px-4 py-2 text-sm font-semibold text-white hover:bg-slate-700"
        >
          Login
        </button>
      </form>
    </section>
  );
}

export default Login;
