import UserProfile from './UserProfile'

const Navbar = () => {
  return (
    <div className="h-16 bg-white border-b border-slate-200 flex items-center justify-end px-8 shadow-sm">
      <UserProfile />
    </div>
  )
}

export default Navbar

