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

