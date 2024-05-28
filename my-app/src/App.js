import css from './App.module.css';
import Sidebar from './components/Sidebar';
import NavBarForm from './components/NavBarForm';
import ContentAPIHooks from './components/ContentAPI'

function App() {
  return (
    <div className={css.App}>
      <Sidebar />
      {/* <NavBar /> */}
      <NavBarForm />
      {/* <Content /> */}
      {/* <ContentAPI /> */}
      {/* <ContentHooks /> */}
      <ContentAPIHooks />
    </div>
  );
}

export default App;