import sys

def patch_file(filename, content):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

app_tsx = """import Navbar from './components/Navbar'
import Login from './components/Login'
import Sidebar from './components/Sidebar'
import UserPage from './components/UserPage'

const App = () => {
  return (
    <div className="flex min-h-screen bg-[#f4f4f0] font-sans text-black">
      <Sidebar />
      <div className="flex-1 flex flex-col">
        <Navbar />
        <main className="flex-1 p-8">
          <div className="max-w-3xl mx-auto space-y-8">
            <UserPage />
            <Login /> 
          </div>
        </main>
      </div>
    </div>
  )
}

export default App
"""

sidebar_tsx = """import UserProfile from './UserProfile'
import { useDispatch } from 'react-redux'
import { logoutUser } from '../redux/user/userSlice'

const Sidebar = () => {
  const dispatch = useDispatch()

  const handleLogout = () => {
    dispatch(logoutUser())
  }

  return (
    <aside className="w-64 bg-[#5CE1E6] border-r-4 border-black p-6 flex flex-col justify-between">
      <div>
        <div className="text-3xl font-black mb-8 border-b-4 border-black pb-4 uppercase tracking-tighter">
          Dashboard
        </div>
        <UserProfile />
      </div>
      <button 
        onClick={handleLogout} 
        className="w-full bg-[#FF5757] hover:bg-[#ff3838] hover:-translate-y-1 transition-transform border-4 border-black text-black font-black uppercase py-3 px-4 shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] hover:shadow-[6px_6px_0px_0px_rgba(0,0,0,1)] active:translate-y-1 active:shadow-[0px_0px_0px_0px_rgba(0,0,0,1)]"
      >
        Logout
      </button>
    </aside>
  )
}

export default Sidebar
"""

navbar_tsx = """import UserProfile from './UserProfile'

const Navbar = () => {
  return (
    <nav className="h-24 bg-[#FFDE59] border-b-4 border-black flex items-center justify-between px-8">
      <h1 className="text-2xl font-black uppercase tracking-tight bg-white border-4 border-black px-4 py-1 shadow-[4px_4px_0px_0px_rgba(0,0,0,1)]">HatchDev</h1>
      <div className="bg-white border-4 border-black px-4 py-2 shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] font-bold">
        <UserProfile />
      </div>
    </nav>
  )
}

export default Navbar
"""

user_page_tsx = """const UserPage = () => {
  return (
    <div className="bg-white border-4 border-black p-6 shadow-[8px_8px_0px_0px_rgba(0,0,0,1)] mb-8">
      <h2 className="text-3xl font-black uppercase mb-4 tracking-tighter bg-[#FFDE59] inline-block px-2 border-2 border-black">User Dashboard</h2>
      <p className="text-lg font-bold border-l-4 border-[#5CE1E6] pl-4 py-2 bg-gray-50">
        Welcome to the neo-brutalist state management demo!
      </p>
    </div>
  )
}

export default UserPage
"""

user_profile_tsx = """import { useSelector } from 'react-redux'
import type { RootState } from '../redux/store'

const UserProfile = () => {
  const user = useSelector((state: RootState) => state.user)
  return (
    <div className="flex flex-col gap-2 text-sm font-bold">
      {user.name && user.email ? (
        <>
          <div className="flex items-center gap-2">
            <span className="bg-black text-white px-2 py-0.5 uppercase text-xs shadow-[2px_2px_0px_0px_rgba(0,0,0,0.3)]">Name</span>
            <span>{user.name}</span>
          </div>
          <div className="flex items-center gap-2">
            <span className="bg-black text-white px-2 py-0.5 uppercase text-xs shadow-[2px_2px_0px_0px_rgba(0,0,0,0.3)]">Email</span>
            <span>{user.email}</span>
          </div>
        </>
      ) : (
        <span className="uppercase text-black font-black bg-[#FF5757] px-2 py-1 border-2 border-black inline-block shadow-[2px_2px_0px_0px_rgba(0,0,0,1)]">Not Logged In</span>
      )}
    </div>
  )
}

export default UserProfile
"""

login_tsx = """import React from 'react'
import { useDispatch } from 'react-redux'
import { setUser } from '../redux/user/userSlice'

const Login = () => {
  const [name, setName] = React.useState('')
  const [email, setEmail] = React.useState('')
  const dispatch = useDispatch()

  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault()
    if (name && email) {
      dispatch(setUser({ name, email }))
    }
  }

  return (
    <div className="bg-[#b8e994] border-4 border-black p-8 shadow-[8px_8px_0px_0px_rgba(0,0,0,1)]">
      <h2 className="text-3xl font-black uppercase mb-6 tracking-tighter bg-white inline-block px-4 py-2 border-4 border-black shadow-[4px_4px_0px_0px_rgba(0,0,0,1)]">
        Login Portal
      </h2>
      <p className="font-bold text-lg mb-6">Welcome Back, Please Login to Continue</p>

      <form onSubmit={handleSubmit} className="space-y-6">
        <div className="space-y-2">
          <label htmlFor="name" className="block font-black uppercase text-lg">Full Name</label>
          <input 
            id="name" 
            name="name" 
            value={name} 
            type="text" 
            onChange={(e) => setName(e.target.value)} 
            required 
            placeholder="Enter your full name" 
            className="w-full bg-white border-4 border-black p-3 font-bold placeholder:text-gray-400 focus:outline-none focus:ring-4 focus:ring-[#FFDE59] transition-shadow shadow-[4px_4px_0px_0px_rgba(0,0,0,1)]"
          />
        </div>
        
        <div className="space-y-2">
          <label htmlFor="email" className="block font-black uppercase text-lg">Email</label>
          <input 
            id="email" 
            name="email" 
            value={email} 
            type="email" 
            onChange={(e) => setEmail(e.target.value)} 
            required 
            placeholder="Enter your email" 
            className="w-full bg-white border-4 border-black p-3 font-bold placeholder:text-gray-400 focus:outline-none focus:ring-4 focus:ring-[#FFDE59] transition-shadow shadow-[4px_4px_0px_0px_rgba(0,0,0,1)]"
          />
        </div>
        
        <button 
          type="submit"
          className="w-full bg-[#FFDE59] hover:bg-[#f6d03d] hover:-translate-y-1 transition-transform border-4 border-black text-black font-black uppercase py-4 text-xl shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] hover:shadow-[6px_6px_0px_0px_rgba(0,0,0,1)] active:translate-y-1 active:shadow-[0px_0px_0px_0px_rgba(0,0,0,1)]"
        >
          Login
        </button>
      </form>
    </div>
  )
}

export default Login
"""

patch_file('src/App.tsx', app_tsx)
patch_file('src/components/Sidebar.tsx', sidebar_tsx)
patch_file('src/components/Navbar.tsx', navbar_tsx)
patch_file('src/components/UserPage.tsx', user_page_tsx)
patch_file('src/components/UserProfile.tsx', user_profile_tsx)
patch_file('src/components/Login.tsx', login_tsx)

print("Patched all components!")
