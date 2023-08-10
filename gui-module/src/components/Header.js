// Common Header dosplayed after Login with Logout and Setting buttons

import logo from "./resources/logo-header.png";
import Button from "./Button";
import { Link } from "react-router-dom";

const Header = () => {
  const notify = () => {
    // For debugging purposes only. REMOVE LATER.
    console.log("You've been notified. Congrats.");
  };

  return (
    <header className="header">
      <img className="logo" src={logo} alt="YUMI Logo" />
      <a
        className="accSettings"
        href="https://developer.mozilla.org/en-US/docs/Web/CSS"
      >
        Account Settings
      </a>
      <Link to="/">
        <Button text="Logout" color="#2DB6F0" onClick={notify} />
      </Link>
    </header>
  );
};

Header.defaultProps = {
  title: "YUMI",
};

export default Header;
