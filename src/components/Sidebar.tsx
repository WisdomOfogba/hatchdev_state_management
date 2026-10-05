import UserProfile from './UserProfile'
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
        className="w-full bg-slate-900 hover:bg-slate-800 text-white font-medium py-2.5 px-4 rounded-lg transition-all duration-200 cursor-pointer active:scale-[0.98] shadow-sm"
      >
        Logout
      </button>
    </div>
  )
}

export default Sidebar
