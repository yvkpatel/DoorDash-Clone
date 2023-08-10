import { render, screen, cleanup, fireEvent } from "@testing-library/react";
import renderer from "react-test-renderer";
import DriverDash from "../dashboard/DriverDashPage";
import userEvent from "@testing-library/user-event";
import { BrowserRouter } from "react-router-dom";
import ReactDOM from "react-dom";
import Button from "../../Button";
import DashList from "../../DashList";
import React, { useEffect } from "react";
import DriverOrder from "../dashboard/DriverOrder";
import DriverManager from "../dashboard/DriverManager";
import "@testing-library/jest-dom/extend-expect";

afterEach(() => {
  cleanup();
});

test("should render driver dashboard component", () => {
  render(
    <BrowserRouter>
      <DriverDash />
    </BrowserRouter>
  );
  const DriverDashElement = screen.getByTestId("driver-dash");
  expect(DriverDashElement).toBeDefined();
});

test("List of restaurants renders", () => {
  render(
    <BrowserRouter>
      <DriverDash />
    </BrowserRouter>
  );
  const DriverDashElement = screen.getByTestId("dash-list");
  expect(DriverDashElement).toBeDefined();
});

test("Accept button renders", () => {
  render(
    <BrowserRouter>
      <DriverDash />
    </BrowserRouter>
  );
  const DriverDashElement = screen.getAllByRole("button", { name: "Accept" });
  expect(DriverDashElement).toBeDefined();
});

const mockRestaurant = {
  item: {
    id: "1",
    title: "Presidential Pizza",
    restaurant: "a",
    destination: "1600 Pennsylvania Avenue",
  },
  manager: {
    id: 4,
    income: 9.24,
    orders: 2,
    driverAcceptOrder(orderID) {
      console.log("Order ID: " + orderID);
    },
  },
};

test("Clicking the Accept button and going to the maps page", () => {
  render(
    <BrowserRouter>
      <DriverOrder {...mockRestaurant} />
    </BrowserRouter>
  );
  fireEvent.click(screen.getByText("Accept"));
  const newURL = window.location.href;
  expect(newURL).toBe("http://localhost/drivermap");
});

test("matches snapshot", () => {
  const tree = renderer.create(
    <BrowserRouter>
      <DriverDash />
    </BrowserRouter>
  );
  expect(tree).toMatchSnapshot();
});
