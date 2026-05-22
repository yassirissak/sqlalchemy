import { BrowserRouter, Route, Routes } from "react-router-dom";
import { Toaster } from "react-hot-toast";
import Navbar from "./components/Navbar.jsx";
import Home from "./pages/Home.jsx";
import AddPost from "./pages/AddPost.jsx";
import Profile from "./pages/Profile.jsx";
import Login from "./pages/Login.jsx";
import Register from "./pages/Register.jsx";
import { AuthProvider } from "./context/AuthContext.jsx";

function App() {
  return (
    <div className="min-h-screen">
        <AuthProvider>
            <Navbar />
            <main className="mx-auto w-full max-w-5xl px-4 py-8 sm:px-6 lg:px-8">
              <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/add-post" element={<AddPost />} />
                <Route path="/profile" element={<Profile />} />
                <Route path="/login" element={<Login />} />
                <Route path="/register" element={<Register />} />
              </Routes>
            </main>

            <Toaster position="top-center" />
        </AuthProvider>
    </div>
  );
}

export default App;
