import Navbar from './components/Navbar'
import Login from './components/Login'
import Sidebar from './components/Sidebar'
import UserPage from './components/UserPage'

const App = () => {
  return (
    <div className="flex min-h-screen bg-slate-50 text-slate-800 font-sans">
      <Sidebar />
      <div className="flex-1 flex flex-col">
        <Navbar />
        <main className="flex-1 p-8 ">
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

