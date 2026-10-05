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
    <div className="flex min-h-screen bg-slate-50 text-slate-800 font-sans">
      <Sidebar />
      <div className="flex-1 flex flex-col">
        <Navbar />
        <main className="flex-1 p-8 overflow-y-auto">
          <div className="max-w-4xl mx-auto space-y-6">
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
    <div className="h-screen w-64 bg-white border-r border-slate-200 flex flex-col justify-between p-6">
      <div>
        <UserProfile />
      </div>
      <button 
        onClick={handleLogout} 
        className="w-full bg-slate-900 hover:bg-slate-800 text-white font-medium py-2.5 px-4 rounded-lg transition-colors duration-200 shadow-sm"
      >
        Logout
      </button>
    </div>
  )
}

export default Sidebar
"""

navbar_tsx = """import React from 'react'
import UserProfile from './UserProfile'

const Navbar = () => {
  return (
    <div className="h-16 bg-white border-b border-slate-200 flex items-center justify-end px-8 shadow-sm">
      <UserProfile />
    </div>
  )
}

export default Navbar
"""

user_page_tsx = """import React from 'react'

const UserPage = () => {
  return (
    <div className="bg-white rounded-xl shadow-sm border border-slate-100 p-6 text-slate-700 font-medium">
      UserPage
    </div>
  )
}

export default UserPage
"""

user_profile_tsx = """import React from 'react'
import { useSelector } from 'react-redux'
import type { RootState } from '../redux/store'

const UserProfile = () => {
  const user = useSelector((state: RootState) => state.user)
  return (
    <div className="flex flex-col gap-1 text-sm text-slate-600">
      {user.name && user.email ? (
        <>
          <p>Name: {user.name}</p>
          <p>Email: {user.email}</p>
        </>
      ) : (
        <p className="text-slate-500 italic">No user logged in</p>
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
      // Perform login logic here
      console.log('Logging in with:', { name, email })
      dispatch(setUser({ name, email }))
    }
  }

  return (
    <div className="bg-white rounded-xl shadow-sm border border-slate-100 p-8 max-w-md">
      <h2 className="text-xl font-semibold text-slate-800 mb-6">Welcome Back, Please Login to Continue</h2>

      <div>
        <form onSubmit={(e) => handleSubmit(e)} className="space-y-5">
          <div className="space-y-1.5">
            <label htmlFor="name" className="block text-sm font-medium text-slate-700">Full Name</label>
            <input 
              id="name" 
              name="name" 
              value={name} 
              type="text" 
              onChange={(e) => setName(e.target.value)} 
              required 
              placeholder="Enter your full name" 
              className="w-full px-4 py-2.5 rounded-lg border border-slate-200 bg-slate-50 focus:bg-white focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-all text-sm text-slate-800 placeholder-slate-400"
            />
          </div>
          <div className="space-y-1.5">
            <label htmlFor="email" className="block text-sm font-medium text-slate-700">Email</label>
            <input 
              id="email" 
              name="email" 
              value={email} 
              type="email" 
              onChange={(e) => setEmail(e.target.value)} 
              required 
              placeholder="Enter your email" 
              className="w-full px-4 py-2.5 rounded-lg border border-slate-200 bg-slate-50 focus:bg-white focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-all text-sm text-slate-800 placeholder-slate-400"
            />
          </div>
          <button 
            type="submit"
            className="w-full bg-blue-600 hover:bg-blue-700 text-white font-medium py-2.5 px-4 rounded-lg transition-colors duration-200 shadow-sm mt-2"
          >
            Login
          </button>
        </form>
      </div>
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

print("Patched all components with sleek styling!")
