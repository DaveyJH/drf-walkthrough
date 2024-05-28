import React, { Component } from "react";
import css from "./css/NavBarForm.module.css";
import NavBarLogInOut from "./NavBarLogInOut";

class NavBarForm extends Component {
  constructor(props) {
    super(props);
    this.state = {
      isLoggedIn: false,
    }
  }

  handleClick = () => {
    this.setState((prevState) => ({
      isLoggedIn: !prevState.isLoggedIn,
    }));
  }


  render() {
    return (
      <div className = { css.NavBar }>
        <h1>My Gallery</h1>
        <div>
          <NavBarLogInOut 
            handleClick={ this.handleClick }
            isLoggedIn={ this.state.isLoggedIn }
          />
        </div>
      </div>
    );
  }
}

export default NavBarForm;