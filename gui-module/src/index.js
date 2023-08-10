import React from "react";
import ReactDOM from "react-dom";
import "./index.css";
import App from "./App";
import reportWebVitals from "./reportWebVitals";
import { BrowserRouter } from "react-router-dom";
import {Elements} from "@stripe/react-stripe-js";
import {loadStripe} from "@stripe/stripe-js";


const stripepromise = loadStripe("pk_test_51Jm5EMCEjyrCg9Bgh93sT083n5KoDfYJUQIXZFFF1NJuAkJWQahYY7EuPUOQEP4p9dG4YpCSlBI8peIIkUTlwryR00kdRkVWlC");
ReactDOM.render(
  <BrowserRouter>
    <React.StrictMode>
      <Elements stripe = {stripepromise}>
      <App />
      </Elements>
    </React.StrictMode>
  </BrowserRouter>,
  document.getElementById("root")
);

reportWebVitals();
