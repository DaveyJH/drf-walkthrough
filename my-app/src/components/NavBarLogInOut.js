import React from 'react'

const NavBarLogInOut = (props) => {
  return (
    <div>
      { props.isLoggedIn
        ? (
          <form action="">
            <label htmlFor="username">Username:</label>
            <input type="text" name="username" id="username" />
            <label htmlFor="password">Password:</label>
            <input type="text" name="username" id="username" />
            <button type="submit" onClick={ props.handleClick }>Submit</button>
          </form>
        )
        : (
          <button onClick={ props.handleClick }>Login</button>
        )
      }
    </div>
  )
}

export default NavBarLogInOut;