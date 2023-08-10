import { render, screen, cleanup, fireEvent } from "@testing-library/react";
import renderer from "react-test-renderer";
import RestaurantDash from "../dashboard/RestaurantDashPage";
import userEvent from "@testing-library/user-event";
import { BrowserRouter } from "react-router-dom";
import ReactDOM from "react-dom";
import Button from "../../Button";
import DashList from "../../DashList";
import OrderInfo from "../dashboard/OrderInfo";
import RestaurantManager from "../dashboard/RestaurantManager";
import React, { useEffect } from "react";
import "@testing-library/jest-dom/extend-expect";

afterEach(() => {
  cleanup();
});

test("should render restaurant dashboard component", () => {
  render(
    <BrowserRouter>
      <RestaurantDash />
    </BrowserRouter>
  );
  const RegisterResElement = screen.queryByTestId("register-res");
  expect(RegisterResElement).toBeDefined();
});

test("Complete button renders", () => {
  render(
    <BrowserRouter>
      <RestaurantDash />
    </BrowserRouter>
  );
  const DriverDashButtons = screen.getAllByRole("button", { name: "Complete" });
  DriverDashButtons.forEach((element) => {
    expect(element).toBeEnabled();
  });
});

const MockList = [
  {
    id: 4,
    title: "Test Pizza",
    restaurant: "???",
    destination: "221B Baker Street",
  },
];

test("List of orders renders", () => {
  let manager = new RestaurantManager(27, 9689.25, 212);
  const { getByText } = render(
    <DashList itemList={MockList} component={OrderInfo} manager={manager} />
  );

  expect(getByText("Test Pizza")).toBeTruthy();
});

test("matches snapshot", () => {
  const tree = renderer.create(
    <BrowserRouter>
      <RestaurantDash />
    </BrowserRouter>
  );
  expect(tree).toMatchSnapshot();
});
