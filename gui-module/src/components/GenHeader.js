// General Header to be displayed on Login/Register pages

import logo from "./resources/logo-header.png";

const GenHeader = () => {
  return (
    <header className="header">
      <img className="logo" src={logo} alt="YUMI Logo" />
    </header>
  );
};

GenHeader.defaultProps = {
  title: "YUMI",
};

export default GenHeader;
