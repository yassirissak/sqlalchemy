import { createContext, useEffect } from "react";
import { useState } from "react";
import {api_url} from "../config.json"
import {toast} from "react-hot-toast"
import { useNavigate } from "react-router-dom";


export const AuthContext = createContext();


export const AuthProvider = ({children}) =>{

    const nav = useNavigate()

    const [access_token, setAuthToken] = useState( ()=>localStorage.getItem("accessToken") )
    const [current_user, setCurrentUser] = useState()
// all functions that are shared by your app

// LOGIN
  const login = (email, password)=>{
    
    fetch(`${api_url}/login`, {
      method: 'POST',
      body: JSON.stringify({
          email,
          password,
      }),
      headers: {
        'Content-type': 'application/json; charset=UTF-8',
      },
    })
      .then((response) => response.json())
      .then((res) => {
        if(res.access_token){
            localStorage.setItem("accessToken", res.access_token)
            setAuthToken(res.access_token)

            nav("/")
          console.log(res)
          toast.success("Logged in successfully")
        }
        else if(res.error){
          toast.error(res.error)
        }
        else{
          toast.error("Something went wrong")
        }

      }
        
      
      );


  }


//   FETCH CURRENT USER
   function getCurrentUser(){
       fetch(`${api_url}/current_user`, {
        method:"GET", 
        headers: {
            'Content-type': 'application/json; charset=UTF-8',
            "Authorization": `Bearer ${access_token}`
        }
       })
        .then((response) => response.json())
        .then((data) => {
            if(data.email){
                setCurrentUser(data)
            }
            
     });

   }

   useEffect(()=>{
    if(access_token){
        getCurrentUser()
    }
    
   }, [access_token])

//    LOGOUT
function logout() {
    fetch(`${api_url}/logout`, {
        method:"DELETE", 
        headers: {
            "Authorization": `Bearer ${access_token}`
        }
       })
        .then((response) => response.json())
        .then((res) => {
            if(res.success){
                toast.success("Logout success")
                localStorage.removeItem("accessToken")
                setAuthToken(null)
                setCurrentUser(null)

                nav("\login")
            }
            else{
                toast.error("failed to logout")
            }
            
     });
    
}


console.log(access_token, "xxx")

const context_data ={
  login,
  access_token,
  current_user,
  logout
}

return (
    <AuthContext.Provider value={context_data}>
        {children}
    </AuthContext.Provider>
)


}