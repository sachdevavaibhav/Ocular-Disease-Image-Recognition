import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <form action="/action_page.php">
        <input type="file" id="myFile" name="filename"/>
        <input type="submit"/>
      </form>
    </div>
  );
}

export default App;
