import { render, screen, cleanup, fireEvent } from "@testing-library/react";
import renderer from "react-test-renderer";
import userEvent from "@testing-library/user-event";
import React, { useEffect } from "react";
import { BrowserRouter } from "react-router-dom";
import ReactDOM from "react-dom";
import Button from "../../Button";
import MenuPage from "../menu/MenuPage";
import "@testing-library/jest-dom/extend-expect";

afterEach(() => {
  cleanup();
});

const MockProp = {
  location: {
    state: {
      restaurantId: 1,
    },
  },
};

test("should render customer menu component", () => {
  render(
    <BrowserRouter>
      <MenuPage {...MockProp} />
    </BrowserRouter>
  );
  const MenuPageElement = screen.getByTestId("menu-page");
  expect(MenuPageElement).toBeDefined();
});

test("Add to Cart button renders", () => {
  render(
    <BrowserRouter>
      <MenuPage {...MockProp} />
    </BrowserRouter>
  );
  const CartButtonElement = screen.getAllByText("Add to Cart");
  expect(CartButtonElement).toBeDefined();
});

test("Add to Cart buttons are enabled", () => {
  render(
    <BrowserRouter>
      <MenuPage {...MockProp} />
    </BrowserRouter>
  );
  const CartButtonElements = screen.getAllByRole("button", {
    name: "Add to Cart",
  });

  CartButtonElements.forEach((element) => {
    expect(element).toBeEnabled();
  });
});

test("clicking checkout should go to the payments page", () => {
  render(
    <BrowserRouter>
      <MenuPage {...MockProp} />
    </BrowserRouter>
  );
  fireEvent.click(screen.getByText("Checkout"));
  const newURL = window.location.href;
  expect(newURL).toBe("http://localhost/payment");
});

test("matches snapshot", () => {
  const tree = renderer.create(
    <BrowserRouter>
      <MenuPage {...MockProp} />
    </BrowserRouter>
  );
  expect(tree).toMatchSnapshot();
});
