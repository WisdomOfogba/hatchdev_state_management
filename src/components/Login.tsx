import React from 'react'
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
            className="w-full bg-blue-600 hover:bg-blue-700 text-white font-medium py-2.5 px-4 rounded-lg transition-all duration-200 cursor-pointer active:scale-[0.98] shadow-sm mt-2"
          >
            Login
          </button>
        </form>
      </div>
    </div>
  )
}

export default Login
