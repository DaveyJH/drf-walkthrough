import React, { Component } from "react";
import css from "./css/NavBarSimple.module.css";

class NavBar extends Component {
  constructor(props) {
    super(props);
    this.state = {
      message: "Hello, guest!",
      buttonText: "log in",
    }
  }

  handleClick() {
    this.setState((prevState, props) => ({
      message: prevState.message === "Hello, guest!" ? "Welcome back, user!" : "Hello, guest!",
      buttonText: prevState.buttonText === "log out" ? "log in" : "log out",
    }));
  }


  render() {
    return (
      <div className = { css.NavBar }>
        <h1>My Gallery</h1>
        <div>
          <span>{ this.state.message }</span>
          <button onClick={ () => this.handleClick() }>{ this.state.buttonText }</button>
        </div>
      </div>
    );
  }
}

export default NavBar;