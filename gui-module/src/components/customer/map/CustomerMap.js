import React from "react";
import map from "../../resources/map_filler_image.jpeg";

const CustomerMap = () => {
  return (
    <div>
      <img
        src={map}
        alt="YUMI Logo"
        style={{
          height: "70vh",
          width: "90vw",
          resizeMode: "contain",
        }}
      />
    </div>
  );
};

export default CustomerMap;
