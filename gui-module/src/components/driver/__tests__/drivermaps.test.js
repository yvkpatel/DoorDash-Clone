import { render, screen, cleanup, fireEvent } from "@testing-library/react";
import React, { useEffect } from "react";
import { BrowserRouter } from "react-router-dom";
import renderer from "react-test-renderer";
import userEvent from "@testing-library/user-event";
import ReactDOM from "react-dom";
import Button from "../../Button";
import DriverMapsPage from "../map/DriverMapsPage";
import DriverDash from "../dashboard/DriverDashPage";
import "@testing-library/jest-dom/extend-expect";

afterEach(() => {
  cleanup();
});

test("should render driver menu component", () => {
  render(
    <BrowserRouter>
      <DriverMapsPage />
    </BrowserRouter>
  );
  const DriverMapsPageElement = screen.getByTestId("driver-map");
  expect(DriverMapsPageElement).toBeDefined();
});

test("Pick Order button is enabled after maps page renders", () => {
  render(
    <BrowserRouter>
      <DriverMapsPage />
    </BrowserRouter>
  );

  expect(screen.getByRole("button", { name: "Pick Order" })).toBeEnabled();
});

test("Deliver Order button is disabled after maps page renders", () => {
  render(
    <BrowserRouter>
      <DriverMapsPage />
    </BrowserRouter>
  );

  expect(screen.getByRole("button", { name: "Deliver Order" })).toBeDisabled();
});

test("After Pick Order button is clicked, it is disabled and Deliver Order button is enabled", () => {
  render(
    <BrowserRouter>
      <DriverMapsPage />
    </BrowserRouter>
  );

  userEvent.click(screen.getByText("Pick Order"));
  expect(screen.getByRole("button", { name: "Pick Order" })).toBeDisabled();
  expect(screen.getByRole("button", { name: "Deliver Order" })).toBeEnabled();
});

test("After Deliver Order button is clicked, go back to driver dashboard", () => {
  render(
    <BrowserRouter>
      <DriverMapsPage />
    </BrowserRouter>
  );
  fireEvent.click(screen.getByText("Pick Order"));
  fireEvent.click(screen.getByText("Deliver Order"));
  const newURL = window.location.href;
  console.log(newURL);
  expect(newURL).toBe("http://localhost/driver-dash");
});

test("matches snapshot", () => {
  const tree = renderer.create(
    <BrowserRouter>
      <DriverMapsPage />
    </BrowserRouter>
  );
  expect(tree).toMatchSnapshot();
});
