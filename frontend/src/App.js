import VehicleList from './components/VehicleList.js';
import SuperUserList from './components/SuperUserList.js';
import './App.css';

var x = 0;
function App() {
  return (
    <div className="App">
      {x?<VehicleList/>:<SuperUserList/>}
      
    </div>
  )
}
export default App;