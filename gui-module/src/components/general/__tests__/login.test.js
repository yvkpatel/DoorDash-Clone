import { render, screen, cleanup } from "@testing-library/react";
import renderer from "react-test-renderer";
import Login from "../login/Login";
import "@testing-library/jest-dom/extend-expect";

test("should render login component", () => {
  render(<Login />);
  const loginElement = screen.getByTestId("login-1");
  expect(loginElement).toBeInTheDocument();
});

test("should show three buttons", () => {
  render(<Login />);
  const customerElement = screen.getByTestId("customer-signup");
  const driverElement = screen.getByTestId("driver-signup");
  const restaurantElement = screen.getByTestId("restaurant-signup");
  expect(customerElement).toBeInTheDocument();
  expect(driverElement).toBeInTheDocument();
  expect(restaurantElement).toBeInTheDocument();
});

test("matches snapshot", () => {
  const tree = renderer.create(<Login />);
  expect(tree).toMatchSnapshot();
});
