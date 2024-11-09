import Todocard from './components/Todocard'
import Todoinput from './components/Todoinput'

function App() {

  return (
    <main>
      <Todoinput />
      <Todocard name="Exercise for 1 hour" />
      <Todocard name="eat" />
      <Todocard name="go for a walk" />
    </main>
  )
}

export default App
